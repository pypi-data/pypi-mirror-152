import inspect
from .mfag import ModflowAg
from ..utils.gsflow_io import _warning


class ModflowAwu(ModflowAg):
    """
    DEPRECATED and will be removed in version 1.1.0

    The ModflowAwu class is used to build read, write, and edit data
    from the MODFLOW-NWT AG package.

    Parameters
    ----------
    model : gsflow.modflow.Modflow object
        model object
    options : flopy.utils.OptionBlock object
        option block object
    time_series : np.recarray
        numpy recarray for the time series block
    well_list : np.recarray
        recarray of the well_list block
    irrdiversion : dict {per: np.recarray}
        dictionary of the irrdiversion block
    irrwell : dict {per: np.recarray}
        dictionary of the irrwell block
    supwell : dict {per: np.recarray}
        dictionary of the supwell block
    extension : str, optional
        default is .ag
    unitnumber : list, optional
        fortran unit number for modflow, default 69
    filenames : list, optional
        file name for ModflowAwu package to write input
    nper : int
        number of stress periods in the model

    Examples
    --------

    load a ModflowAwu file

    >>> ml = gsflow.modflow.Modflow('awutest')
    >>> awu = gsflow.modflow.ModflowAwu.load('test.awu', ml, nper=2, method="gsflow")

    """

    def __init__(
        self,
        model,
        options=None,
        time_series=None,
        well_list=None,
        irrdiversion=None,
        irrwell=None,
        supwell=None,
        extension="awu",
        unitnumber=None,
        filenames=None,
        nper=0,
    ):

        msg = (
            "ModflowAwu is deprecated and will be removed for version 1.1.0, "
            "please use ModflowAg"
        )
        _warning(
            msg,
            inspect.getframeinfo(inspect.currentframe()),
            DeprecationWarning,
        )

        super(ModflowAwu, self).__init__(
            model,
            options,
            time_series,
            well_list,
            irrdiversion,
            irrwell,
            supwell,
            extension,
            unitnumber,
            filenames,
            nper,
        )

    @staticmethod
    def load(f, model, nper=0, method="gsflow", ext_unit_dict=None):
        """
        Method to load the AG package from file

        Parameters
        ----------
        f : str
            filename
        model : gsflow.modflow.Modflow object
            model to attach the ag pacakge to
        nper : int
            number of stress periods in model
        method : str
            "gsflow" or "modflow"
        ext_unit_dict : dict, optional

        Returns
        -------
            ModflowAwu object
        """
        msg = "ModflowAwu is deprecated and will be removed, calling ModflowAg"
        _warning(
            msg,
            inspect.getframeinfo(inspect.currentframe()),
            DeprecationWarning,
        )

        return ModflowAg.load(f, model, nper, ext_unit_dict)
