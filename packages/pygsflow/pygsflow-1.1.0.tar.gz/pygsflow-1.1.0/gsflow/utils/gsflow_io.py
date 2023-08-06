import os
import warnings
import inspect

warnings.simplefilter("always", UserWarning)
warnings.simplefilter("always", PendingDeprecationWarning)
warnings.simplefilter("always", DeprecationWarning)


def get_file_abs(control_file=None, model_ws=None, fn=None):
    """
    Utility method to create file's absolute path

    Parameters
    ----------
    control_file : str
        absoulute path to the control file
    model_ws : str
        relative path to model_ws
    fn : str
        path to file

    Returns
    -------
        abs_file : str
            absolute file path

    """

    if fn is not None:
        fn = os.path.normpath(fn)
        if os.path.isabs(fn):
            return fn

    if model_ws is not None:
        sws = os.path.abspath(os.getcwd())
        ws = os.path.join(sws, model_ws)
        if fn is None:
            abs_file = ws
        else:
            abs_file = os.path.join(ws, fn)
    else:
        control_folder = os.path.dirname(control_file)
        abs_file = os.path.abspath(os.path.join(control_folder, fn))

    return abs_file


def _get_relative_path(control, fn):
    """
    If relative paths are used, they should be relative to the control file

    Parameters
    ----------
    control : str
        control file path and name
    fn : str
        file path and name

    Returns
    -------
        str : relative path

    """
    control_file_abs = os.path.abspath(control)
    fn_abs = os.path.abspath(fn)
    # find common path
    rel_dir = os.path.relpath(
        os.path.dirname(fn), os.path.dirname(control_file_abs)
    )
    rel_path = os.path.join(rel_dir + os.path.basename(fn))
    return rel_path


def find_parameter(name, parameters_list):
    """
    Utility method to loop through parameters to find values
    etc...

    Parameters
    ----------
    name : str
        parameter name
    parameters_list : list
        list of ParameterRecord objects or ControlRecord objects

    Returns
    -------
    rec : record object

    """

    if len(parameters_list) > 0:
        for rec in parameters_list:
            if rec.name.lower() == name.lower():
                return rec
        return None

    else:
        err = "parameter_list is empty"
        _warning(err, inspect.getframeinfo(inspect.currentframe()))
        return None


def line_strip(line):
    """
    Remove comments and replace commas from input text
    for a free formatted modflow input file

    Parameters
    ----------
        line : str
            a line of text from a modflow input file

    Returns
    -------
        str : line with comments removed and commas replaced

    """
    for comment_flag in [";", "#", "!!"]:
        line = line.split(comment_flag)[0]
    line = line.strip()
    return line.replace(",", " ")


def multi_line_strip(fobj):
    """
    Remove comments and replace commas from input text
    for a free formatted modflow input file

    Parameters
    ----------
        fobj : open file object
            a line of text from an input file

    Returns
    -------
        str : line with comments removed and commas replaced

    """
    while True:
        line = line_strip(fobj.readline())
        if line:
            return line.lower()


def _warning(msg, frame, wtype=UserWarning):
    """
    Method to standardize the warning output in pyGSFLOW and avoid
    absolute file paths in warning messages

    Parameters
    ----------
    msg : str
        error message
    frame : named tuple
        named tuple from inspect.getframeinfo
    wtype :
        warning type to be displayed defaults to UserWarning

    """
    module = os.path.split(frame.filename)[-1]
    warnings.warn_explicit(msg, wtype, module, frame.lineno)


def _write_pickle(f, obj):
    """
    Method to write a binary pickle file. Used with _Cascades and _Streamsobj

    Parameters
    ----------
    f : str
        file name
    obj : class object
        class object to dump into a binary object

    Returns
    -------
        None
    """
    import pickle

    with open(f, "wb") as foo:
        pickle.dump(obj, foo)


def _read_pickle(f):
    """
    Method to read a binary pickle file. Used with _Cascades and _Streamsobj

    Parameters
    ----------
    f : str
        file name

    Returns
    -------
        class object
    """
    import pickle

    with open(f, "rb") as foo:
        data = pickle.load(foo)
    return data


def isint(s):
    """
    Method to check if a string is an integer

    Parameters
    ----------
    s : str

    Returns
    -------
        bool
    """
    try:
        int(s)
        return True
    except (TypeError, ValueError):
        return False
