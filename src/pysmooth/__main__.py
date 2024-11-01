"""Command-line interface."""

import numpy as np

from pysmooth._smooth import sm_3, sm_3R, sm_3RS3R, sm_3RSR, sm_3RSS, sm_split3


def smooth(
    x: list[float],
    kind: str = "3RS3R",
    twiceit: bool = False,
    endrule: str = "Tukey",
    do_ends: bool = False,
) -> list[float]:
    """Tukey's smoothers, translated from the `smooth` function found in the R module {stats}.

    Parameters
    ----------
    x : arraylike
        a list of numbers to smooth
    kind : str, optional
        the kind of smoother required.  Valid options include "3RS3R", "3RSS",
        "3RSR", "3R", "3", "S"
    twiceit : bool, optional
        Run the smoother over the data twice.  Twicing a smoother S(y) means
        S(y) + S(y - S(y)), i.e., adding smoothed residuals to the smoothed
        values. This decreases bias (increasing variance)
    endrule : str, optional
        rule for smoothing at the boundary. Valid options are "copy" and "Tukey"
    do_ends : bool, optional
        indicate if the 3-splitting of ties should also happen at the boundaries
        (ends). This is only used for kind = "S"

    Returns
    -------
    y : list of floats
        the smoothed values
    it : int
        number of iterations required to reach stable smoothing
    """
    if kind not in ("3RS3R", "3RSS", "3RSR", "3R", "3", "S"):
        msg = "An invalid kind of smoother was selected"
        raise RuntimeError(msg)

    if endrule == "copy":
        iend = 1
    elif endrule == "Tukey":
        iend = 2
    else:
        msg = f"endrule must be either 'copy' or 'Tukey', but {endrule} was passed"
        raise RuntimeError(msg)

    if any(np.isnan(np.array(x, dtype=np.float64))):
        msg = "The sequence to be smoothed contains NAs/nans. This algorithm " "is unable to accomodate NAs."
        raise ValueError(msg)

    if not all(np.issubdtype(type(_), np.number) for _ in x):
        msg = "The sequence contains non-float values."
        raise ValueError(msg)

    if kind.startswith("3RS") and not do_ends:
        iend = -iend
    elif kind == "S":
        iend = int(do_ends)

    n: int = len(x)
    y: list[float] = np.zeros(n, dtype=np.float64).tolist()
    if kind != "S":
        z: list[float] = np.zeros(n, dtype=np.float64).tolist()
        w: list[float] = np.zeros(n, dtype=np.float64).tolist()
        split_ends = iend < 0

        if kind == "3RS3R":
            _, x, y, z, w = sm_3RS3R(x, y, z, w, n, abs(iend), split_ends)
        elif kind == "3RSS":
            _, x, y, z = sm_3RSS(x, y, z, n, abs(iend), split_ends)
        elif kind == "3RSR":
            _, x, y, z, w = sm_3RSR(x, y, z, w, n, abs(iend), split_ends)
        elif kind == "3R":
            _, x, y, z = sm_3R(x, y, z, n, iend)
        elif kind == "3":
            _, x, y = sm_3(x, y, n, iend)

    else:
        _, x, y = sm_split3(x, y, n, bool(iend))

    if twiceit:
        r: list[float] = smooth(x=y, kind=kind, twiceit=False, endrule=endrule, do_ends=do_ends)
        y += r

    return y
