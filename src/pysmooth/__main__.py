"""Command-line interface."""
from typing import List, Tuple

import numpy as np
from rich.console import Console

from .smooth import sm_3, sm_3R, sm_3RS3R, sm_3RSR, sm_3RSS, sm_split3

console = Console()


def main() -> None:
    console.print("pysmooth: Python implementation of stats::smooth() from R")


def smooth(
    x: List[float], kind: str = "3RS3R", twiceit: bool = False, endrule: str = "Tukey", do_ends: bool = False
) -> Tuple[List[float], int]:
    """Tukey's smoothers, translated from the `smooth` function found in the
    R module {stats}

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
        raise RuntimeError("An invalid kind of smoother was selected")

    if endrule == "copy":
        iend = 1
    elif endrule == "Tukey":
        iend = 2
    else:
        raise RuntimeError(
            f"endrule must be either 'copy' or 'Tukey', but {endrule} was passed"
        )

    if endrule == "copy":
        iend = 1
    elif endrule == "Tukey":
        iend = 2
    else:
        raise RuntimeError(
            f"endrule must be either 'copy' or 'Tukey', but {endrule} was passed"
        )

    if any(np.isnan(x)):
        raise ValueError(
            "The sequence to be smoothed contains NAs/nans. This algorithm is unable to accomodate NAs."
        )

    if not all([np.issubdtype(type(_), np.number) for _ in x]):
        raise ValueError("The sequence contains non-numeric values.")

    if kind.startswith("3RS"):
        iend -= 1
    elif kind == "S":
        iend = int(bool(do_ends))

    n = len(x)
    y = np.zeros(n).tolist()
    split_ends = True if iend < 0 else False

    if kind != "S":
        it = 0  # /* -Wall */;
        z = np.zeros(n).tolist()
        if kind == "3RS3R":
            w = np.zeros(n).tolist()
            it, x, y, z, w = sm_3RS3R(x, y, z, w, n, iend, split_ends)
        elif kind == "3RSS":
            it, x, y, z = sm_3RSS(x, y, z, n, iend, split_ends)
        elif kind == "3RSR":
            w = np.zeros(n)
            it, x, y, z, w = sm_3RSR(x, y, z, w, n, iend, split_ends)
        elif kind == "3R":
            it, x, y, z = sm_3R(x, y, z, n, iend)
        elif kind == "3":
            it, x, y = sm_3(x, y, n, iend)

    else:
        it, x, y = sm_split3(x, y, n, bool(iend))

    if twiceit:
        r, _ = smooth(x=y, kind=kind, twiceit=False, endrule=endrule, do_ends=do_ends)
        y += r

    return y, it-1


if __name__ == "__main__":
    main()  # pragma: no cover
