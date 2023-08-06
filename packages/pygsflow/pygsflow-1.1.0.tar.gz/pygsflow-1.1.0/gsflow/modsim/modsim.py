import numpy as np
import pandas as pd
import os
import inspect
from ..utils.gsflow_io import _warning
import flopy as fp

try:
    import shapefile
except ImportError:
    shapefile = None

try:
    import pycrs
except ImportError:
    pycrs = None


class Modsim(object):
    """
    Class to handle creating MODSIM inputs
    for the MODSIM-GSFLOW coupled modeling option
    in GSFLOW.

    Parameters
    ----------
    model : gsflow.GsflowModel instance or gsflow.modflow.Modflow instance
    other : str or None
        include can be used to add an optional sfr field (ex. strhc1) to the
        stream vector shapefile.

    Examples
    --------

    >>> import gsflow
    >>> gsf = gsflow.GsflowModel.load_from_file("gsflow.control")
    >>> modsim = gsflow.modsim.Modsim(gsf)
    >>> modsim.write_modsim_shapefile("myshp.shp")

    """

    def __init__(self, model, other=None):
        from ..gsflow import GsflowModel
        from ..modflow import Modflow

        if isinstance(model, (Modflow, fp.modflow.Modflow)):
            self.parent = model
            self.mf = model
        else:
            self.parent = model
            self.mf = self.parent.mf
        if other is not None:
            other = other.lower()
        self._other = other
        self._sfr = self.mf.get_package("SFR")
        self._lak = self.mf.get_package("LAK")
        self._ag = self.mf.get_package("AG")
        self._ready = True

        if self.mf is None:
            self._ready = False

        if self._sfr is None:
            self._ready = False

        self._nearest = True
        self._sfr_nearest = False

    @property
    def sfr_segs(self):
        """
        Returns a list of the SFR segments

        """
        if not self._ready:
            return ()
        else:
            reach_data = self._sfr.reach_data
            segs = []
            for rec in reach_data:
                segs.append(rec.iseg)

            segs = list(set(segs))
            return sorted(segs)

    @property
    def lake_segs(self):
        """
        Returns a list of the lake numbers connected to SFR segments

        """
        if not self._ready:
            return ()
        elif self._lak is None:
            return ()
        else:
            seg_data = self._sfr.segment_data
            lakes = []
            for per, recarray in seg_data.items():
                for rec in recarray:
                    if rec.iupseg < 0:
                        lakes.append(rec.iupseg)
                    if rec.outseg < 0:
                        lakes.append(rec.outseg)

            lakes = list(set(lakes))
            return sorted(lakes)

    @property
    def sfr_topology(self):
        """
        Returns a list of SFR topology objects for writing to shapefile

        """
        sfr_topo = []
        for seg in self.sfr_segs:
            sfr_topo.append(
                _SfrTopology(
                    self._sfr, self.mf, seg, self._sfr_nearest, self._other
                )
            )

        return sfr_topo

    @property
    def lake_topology(self):
        """
        Returns a list of LAK topology objects for writing to shapefile

        """
        lake_topo = []
        for lake in self.lake_segs:
            lake_topo.append(
                _LakTopology(self._lak, self.mf, lake, self._nearest)
            )

        return lake_topo

    def __set_spillway_flag(self, flag, sfr_topology):
        """
        Flips the sfr topology flag based on user supplied
        flag.

        Parameters
        ----------
        flag : str or list
            "elev" for elevation rules
            "flow" for flow rules
            list of segments to flip certain segments
        sfr_topology : list
            list of _SfrTopology instances

        Returns
        -------
        sfr_topology : list
            list of _SfrTopology instances

        """
        temp = []
        if isinstance(flag, list):
            for sfr in sfr_topology:
                if sfr.attributes.iseg in flag:
                    sfr.attributes.spill_flg = 1
                else:
                    pass
                temp.append(sfr)

        else:
            res_connect = []
            for ix, sfr in enumerate(sfr_topology):
                if sfr.attributes.iupseg < 0:
                    res_connect.append(ix)

            t = []
            for i in res_connect:
                sfr = sfr_topology[i]

                for j in res_connect:
                    sfr2 = sfr_topology[j]
                    if sfr.attributes.iseg == sfr2.attributes.iseg:
                        continue
                    elif sfr.attributes.iupseg == sfr2.attributes.iupseg:
                        if sfr.attributes.outseg == sfr2.attributes.outseg:
                            if flag.lower() == "elev":
                                if sfr.attributes.elev > sfr2.attributes.elev:
                                    sfr.attributes.spill_flg = 1
                                else:
                                    pass
                            if flag.lower() == "flow":
                                if sfr.attributes.flow == 0:
                                    sfr.attributes.spill_flg = 1
                                else:
                                    pass

                t.append(sfr)

            for ix, sfr in enumerate(sfr_topology):
                if ix in res_connect:
                    temp.append(t.pop(0))
                else:
                    temp.append(sfr)

        return temp

    def __set_ag_diversion(self, sfr_topology):
        """
        Method to set a flag for ag diversion or not ag diversion

        Parameters
        ----------
        sfr_topology: __Sfr_Topology object

        Returns
        -------
            __Sfr_Topology object
        """
        if self._ag is None:
            return sfr_topology

        ag_segments = self._ag._segment_list(ignore_ponds=True)

        temp = []
        for sfr in sfr_topology:
            if sfr.attributes.iseg in ag_segments:
                sfr.attributes.ag_diversion = 1

            temp.append(sfr)

        return temp

    def write_modsim_shapefile(
        self,
        shp=None,
        epsg=None,
        flag_spillway=False,
        nearest=True,
        sfr_nearest=False,
        flag_ag_diversion=False,
    ):
        """
        Method to create a modsim compatible
        shapefile from GSFLOW model inputs (SFR, LAK)
        package.

        Parameters
        ----------
        shp : str
            optional shapefile name, if none
            will be written in gsflow directory using
            the model name.
        epsg : int
            epsg projection projection code, if none will epsg from
            flopy modelgrid
        flag_spillway : bool, str, list
            if flag_spillway is indicated then MODSIM will change
            the spill_flg attribute to one. This can be accomplished
            by one of three methods.

            1.) flag_spillway="elev", the code will search for spillways
            from reservoirs based on elevation rules
            2.) flag_spillway="flow", the code will search for spillways
            from reservoirs based on flow rules
            3.) flag_spillway=[3, 4, 5, ...] a user supplied list of SFR
            segments can be supplied to flag spillways
        nearest : bool
            if nearest is True, lak topology will connect to the nearest
            SFR reaches based on the segment they are connected to. If False
            lak topology will connect to the start or end of the Segment based
            on iupseg and outseg
        sfr_nearest : bool
            if sfr_nearest is True, sfr topology will connect using the
            distance equation. If False topology will connect to the start
            or end of the Segment based on iupseg and outseg
        flag_ag_diversion : bool
            if flag_ag_diversion is True, code will check if SFR segments are
            agricultural diversions and then flag the diversions.

        """
        import requests

        if not self._ready:
            return

        if shapefile is None:
            msg = "Pyshp must be installed to write MODSIM shapefile"
            _warning(msg, inspect.getframeinfo(inspect.currentframe()))
            return

        if shp is None:
            ws = self.parent.control.model_dir
            t = self._sfr.file_name[0].split(".")
            t = ".".join(t[:-1])
            name = t + "_modsim.shp"
            shp = os.path.join(ws, name)

        self._nearest = nearest
        self._sfr_nearest = sfr_nearest

        sfr_topology = self.sfr_topology
        lake_topology = self.lake_topology

        if flag_spillway:
            sfr_topology = self.__set_spillway_flag(
                flag_spillway, sfr_topology
            )

        if flag_ag_diversion:
            sfr_topology = self.__set_ag_diversion(sfr_topology)

        w = shapefile.Writer(shp)
        w.shapeType = 3
        w.field("ISEG", "N")
        w.field("IUPSEG", "N")
        w.field("OUTSEG", "N")
        w.field("SPILL_FLG", "N")
        if self._other is not None:
            w.field(self._other.upper(), "N", decimal=5)
        if flag_ag_diversion:
            w.field("AG_FLG", "N")

        for sfr in sfr_topology:
            w.line(sfr.polyline)
            attributes = sfr.attributes
            if self._other is None and not flag_ag_diversion:
                w.record(
                    attributes.iseg,
                    attributes.iupseg,
                    attributes.outseg,
                    attributes.spill_flg,
                )
            elif self._other is not None and not flag_ag_diversion:
                w.record(
                    attributes.iseg,
                    attributes.iupseg,
                    attributes.outseg,
                    attributes.spill_flg,
                    attributes.other,
                )
            elif self._other is None and flag_ag_diversion:
                w.record(
                    attributes.iseg,
                    attributes.iupseg,
                    attributes.outseg,
                    attributes.spill_flg,
                    attributes.ag_diversion,
                )

            else:
                w.record(
                    attributes.iseg,
                    attributes.iupseg,
                    attributes.outseg,
                    attributes.spill_flg,
                    attributes.other,
                    attributes.ag_diversion,
                )

        for lake in lake_topology:
            for ix, attributes in enumerate(lake.attributes):
                w.line([lake.polyline[ix]])
                if self._other is None:
                    w.record(
                        attributes.iseg,
                        attributes.iupseg,
                        attributes.outseg,
                        attributes.spill_flg,
                    )
                else:
                    w.record(
                        attributes.iseg,
                        attributes.iupseg,
                        attributes.outseg,
                        attributes.spill_flg,
                        attributes.other,
                    )
        try:
            w.close()
        except AttributeError:
            pass

        if epsg is None:
            epsg = self.mf.modelgrid.epsg
            if epsg is None:
                msg = "EPSG code not found, skipping prj file"
                _warning(msg, inspect.getframeinfo(inspect.currentframe()))
                return
        epsg = int(epsg)
        ws = os.path.abspath(os.path.dirname(__file__))
        cache = os.path.join(ws, "epsg_to_wkt.dat")
        dfepsg = pd.read_csv(cache, delimiter="\t")
        wkt = None
        if dfepsg.size != 0:
            if epsg in dfepsg.epsg.values:
                wkt = dfepsg.loc[dfepsg.epsg == epsg, "wkt"].values[0]

        prj = shp[:-4] + ".prj"
        if wkt is None:
            url = f"https://spatialreference.org/ref/epsg/{epsg}/esriwkt/"

            try:
                r = requests.get(url, verify=False)
                wkt = r.text
                if not wkt:
                    return
            except:
                msg = f"WKT {epsg} not found, skipping prj file"
                _warning(msg, inspect.getframeinfo(inspect.currentframe()))
                return

            d = {"epsg": epsg, "wkt": wkt}
            dfepsg = dfepsg.append(d, ignore_index=True)
            dfepsg.to_csv(cache, sep="\t", index=False)

        with open(prj, "w") as foo:
            foo.write(wkt)


class _LakTopology(object):
    """
    Object that creates lake centroids and
    defines the topology/connectivity of
    the LAK file to the SFR object

    Parameters
    ----------
    lak : flopy.modflow.ModflowLak object
    model : flopy.modflow.Modflow or gsflow.modflow.Modflow
    lakeno : int
        lake number
    nearest : bool
        defaults to True, creates a connection to nearest node
        if False creates connection to the last reach
    """

    def __init__(self, lak, model, lakeno, nearest=True):
        self._parent = model
        self._lak = lak
        self._sfr = self._parent.get_package("SFR")
        self._mg = self._parent.modelgrid
        self._xv = self._mg.xvertices
        self._yv = self._mg.yvertices
        self._lakeno = lakeno
        self._centroid = None
        self._connections = None
        self._polyline = None
        self._attributes = None
        self._ij = None
        self._nearest = nearest

    @property
    def lakeno(self):
        return self._lakeno

    @property
    def centroid(self):
        if self._centroid is None:
            self._set_lake_centroid()
        return self._centroid

    @property
    def connections(self):
        if self._connections is None:
            self._set_lake_connectivity()
        return self._connections

    @property
    def polyline(self):
        if self._polyline is None:
            self._set_polyline()
        return self._polyline

    @property
    def attributes(self):
        if self._attributes is None:
            self._set_lake_connectivity()
        return self._attributes

    def _set_lake_centroid(self):
        """
        Method to calculate the geometric
        centroid of a lake

        """
        # get a 3d array of lak locations
        lakes = self._lak.lakarr.array

        lakeno = self.lakeno
        if lakeno < 0:
            lakeno *= -1

        verts = []
        for lake3d in lakes:
            if len(lake3d.shape) == 3:
                t = np.where(lake3d == lakeno)
                i = list(t[1])
                j = list(t[2])
                ij = list(zip(i, j))
                for i, j in ij:
                    verts += self._mg.get_cell_vertices(i, j)

        if verts:
            verts = np.array(list(set(verts))).T
            xc = np.mean(verts[0])
            yc = np.mean(verts[1])
            self._centroid = (xc, yc)
        else:
            self._centroid = None

    def _set_lake_connectivity(self):
        """
        Method to define lake connections to
        the sfr network. Will be used to
        define polylines and topology

        """
        if self._sfr is None:
            return

        lakeno = self.lakeno
        if lakeno > 0:
            lakeno *= -1

        cseg = []
        attrs = []
        for per, recarray in self._sfr.segment_data.items():
            for rec in recarray:
                if rec.nseg in cseg:
                    continue
                else:
                    if rec.iupseg == lakeno:
                        cseg.append(rec.nseg)
                        attrs.append(_Attributes(lakeno, outseg=rec.nseg))
                    elif rec.outseg == lakeno:
                        cseg.append(rec.nseg)
                        attrs.append(_Attributes(lakeno, iupseg=rec.nseg))

        temp = []
        for seg in cseg:
            if seg not in temp:
                temp.append(seg)

        cseg = temp

        ij = []
        reach_data = self._sfr.reach_data
        reach_data.sort(axis=0, order=["iseg", "ireach"])
        for seg in cseg:
            temp = []
            for rec in reach_data:
                if rec.iseg == seg:
                    temp.append((rec.i, rec.j))

            ij.append(temp)

        # now we use the distance equation to connect to
        # the closest....
        if self._nearest:
            verts = []
            for conn in ij:
                tverts = []
                dist = []
                for i, j in conn:
                    xv = self._mg.xcellcenters[i, j]
                    yv = self._mg.ycellcenters[i, j]
                    tverts.append((xv, yv))
                    a = (xv - self.centroid[0]) ** 2
                    b = (yv - self.centroid[1]) ** 2
                    c = np.sqrt(a + b)
                    dist.append(c)

                if tverts:
                    vidx = dist.index(np.min(dist))
                    verts.append(tverts[vidx])
        else:
            verts = []
            for ix, conn in enumerate(ij):
                if attrs[ix].outseg == 0:
                    i, j = conn[-1]
                else:
                    i, j = conn[0]
                xv = self._mg.xcellcenters[i, j]
                yv = self._mg.ycellcenters[i, j]
                verts.append((xv, yv))

        if verts:
            self._connections = verts
            self._attributes = attrs

        else:
            self._connections = None
            self._attributes = None

    def _set_polyline(self):
        """
        Method to create and set the polyline input
        for pyshp

        """
        if self.connections is None:
            return
        if self.centroid is None:
            return

        polyline = []
        for ix, conn in enumerate(self.connections):
            if self.attributes[ix].iupseg == 0:
                part = [list(self.centroid), list(conn)]
            else:
                part = [list(conn), list(self.centroid)]

            polyline.append(part)

        self._polyline = polyline


class _SfrTopology(object):
    """
    Object that creates lake centroids and
    defines the topology/connectivity of
    a sfr segment

    Parameters
    ----------
    sfr : flopy.modflow.ModflowSfr object
    model : flopy.modflow.Modflow or gsflow.modflow.Modflow object
    iseg : int
        sfr segment number
    nearest : bool
        method to determine whether topology is calculated via distance eq.
        default is False
    other : str or None
        include can be used to add an optional sfr field (ex. strhc1) to the
        stream vector shapefile.
    other_val : int, float, or None
        other_val can be used to add an optional value to the shapefile for
        each SFR segment.

    """

    def __init__(self, sfr, model, iseg, nearest=False, other=None):
        self._sfr = sfr
        self._parent = model
        self._iseg = iseg
        self._other = other
        self._nearest = nearest
        self._mg = self._parent.modelgrid
        self._xv = self._mg.xvertices
        self._yv = self._mg.yvertices
        self._connections = None
        self._polyline = None
        self._attributes = None
        self._ij = None

    @property
    def iseg(self):
        return self._iseg

    @property
    def ij(self):
        if self._ij is None:
            self._set_attributes()
        return self._ij

    @property
    def connections(self):
        if self._connections is None:
            self._set_sfr_connectivity()
        return self._connections

    @property
    def polyline(self):
        if self._polyline is None:
            self._set_polyline()
        return [self._polyline]

    @property
    def attributes(self):
        if self._attributes is None:
            self._set_attributes()
        return self._attributes

    def _set_sfr_connectivity(self):
        """
        Method to get and set the the sfr
        connectivity and get the centroid of
        the upstream or downstream segment
        for shapefile exporting

        """
        if self._sfr is None:
            return

        outseg = self.attributes.outseg
        iupseg = self.attributes.iupseg

        ijup = []
        ijout = []
        irchup = []
        irchout = []
        for rec in self._sfr.reach_data:
            if rec.iseg == iupseg:
                ijup.append([rec.i, rec.j])
                irchup.append(rec.ireach)
            elif rec.iseg == outseg:
                ijout.append([rec.i, rec.j])
                irchout.append(rec.ireach)
            else:
                pass

        if self._nearest:
            updist = []
            for i, j in ijup:
                a = (i - self.ij[0]) ** 2
                b = (j - self.ij[1]) ** 2
                c = np.sqrt(a + b)
                updist.append(c)

            outdist = []
            for i, j in ijout:
                a = (i - self.ij[0]) ** 2
                b = (j - self.ij[1]) ** 2
                c = np.sqrt(a + b)
                outdist.append(c)
        else:
            updist = irchup
            outdist = irchout

        if updist:
            if self._nearest:
                upidx = updist.index(np.min(updist))
                ijup = [ijup[upidx]]
            else:
                upidx = updist.index(np.max(updist))
                ijup = [ijup[upidx]]

        if outdist:
            outix = outdist.index(np.min(outdist))
            ijout = [ijout[outix]]

        vup = ()
        for i, j in ijup:
            xv = self._mg.xcellcenters[i, j]
            yv = self._mg.ycellcenters[i, j]
            vup = (xv, yv)

        vout = ()
        for i, j in ijout:
            xv = self._mg.xcellcenters[i, j]
            yv = self._mg.ycellcenters[i, j]
            vout = (xv, yv)

        self._connections = [vup, vout]

    def _set_polyline(self):
        """
        Method to construct a polyline for the
        SFR segments

        """
        if self._sfr is None:
            return

        conn = self.connections
        ij = []
        reach_data = self._sfr.reach_data
        reach_data.sort(axis=0, order=["iseg", "ireach"])
        for rec in reach_data:
            if rec.iseg == self.iseg:
                ij.append([rec.i, rec.j])

        line = []
        if conn[0]:
            line.append(list(conn[0]))

        for i, j in ij:
            xv = self._mg.xcellcenters[i, j]
            yv = self._mg.ycellcenters[i, j]
            line.append([xv, yv])

        if conn[-1]:
            line.append(list(conn[-1]))

        if line:
            self._polyline = line
        else:
            self._polyline = None

    def _set_attributes(self):
        """
        Method to set the attribute field
        for a SFR segment

        """
        if self._sfr is None:
            return

        outseg = []
        iupseg = []
        flow = []
        for per, recarray in self._sfr.segment_data.items():
            for rec in recarray:
                if rec.nseg == self.iseg:
                    outseg.append(rec.outseg)
                    iupseg.append(rec.iupseg)
                    flow.append(rec.flow)
                    break

        ij = []
        strtop = []
        other = []
        reach_data = self._sfr.reach_data
        reach_data.sort(axis=0, order=["iseg", "ireach"])
        for rec in reach_data:
            if rec.iseg == self.iseg:
                ij.append([rec.i, rec.j])
                strtop.append(rec.strtop)
                if self._other is not None:
                    other.append(rec[self._other])

        if ij:
            self._ij = tuple(ij[-1])

        if outseg:
            outseg = list(set(outseg))[0]
        else:
            outseg = 0

        if iupseg:
            iupseg = list(set(iupseg))[0]
        else:
            iupseg = 0

        strtop = min(strtop)
        if self._other is not None:
            other = np.mean(other)
        else:
            other = None
        flow = max(flow)

        self._attributes = _Attributes(
            self.iseg, iupseg, outseg, flow, strtop, other
        )


class _Attributes(object):
    """
    Object oriented storage method to standardize
    the topology function calls

    Parameters
    ----------
    iseg : int
        segment number
    iupseg : int
        upstream segment number
    outseg : int
        output segment number
    flow : float
        maximum specified flow rate
    strtop : float
        minimum strtop elevation
    other : None or float
        additional field data
    """

    def __init__(self, iseg, iupseg=0, outseg=0, flow=0, strtop=0, other=None):
        self.iseg = iseg
        self.iupseg = iupseg
        self.outseg = outseg
        self.flow = flow
        self.elev = strtop
        self.spill_flg = 0
        self.ag_diversion = 0
        if other is None:
            self.other = np.nan
        else:
            self.other = other
