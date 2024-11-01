"""Tukey's (Running Median) smoother.

A direct as I can translation of the R and C code for stats::smooth() found
in R 4.1.2.  A copy of the original code can be found at
https://github.com/wch/r-source/blob/trunk/src/library/stats/src/smooth.c

"""

from enum import Enum
from statistics import median


class EndRule(int, Enum):
    sm_no_endrule = 0
    sm_copy_endrule = 1
    sm_tukey_endrule = 2


N_CUTOFF = 2


# TODO: reimplement this in rust
def med3(u: float, v: float, w: float) -> float:
    """Find the median of three numbers.

    Parameters
    ----------
    u, v, w : float
        The three numbers to find the median of.

    Returns
    -------
    float
        median of u, v, w
    """
    if u <= v <= w or u >= v >= w:
        return v
    elif u <= w <= v or u >= w >= v:
        return w
    else:
        return u


def imed3(u: float, v: float, w: float) -> int:
    """Find the index of the median of three numbers.

    Parameters
    ----------
    u, v, w : float
        The three numbers to find the index of the median of.

    Returns
    -------
    int
        -1 if u, 0 if v, or 1 if w is the median
    """
    if u <= v <= w or u >= v >= w:
        return 0
    elif u <= w <= v or u >= w >= v:
        return 1
    else:
        return -1


def sm_3(x: list[float], y: list[float], n: int, end_rule: int) -> tuple[bool, list[float], list[float]]:
    chg = False

    if n <= N_CUTOFF:
        for i in range(n):
            y[i] = x[i]
        return False, x, y

    for i in range(1, n - 1):
        j = imed3(x[i - 1], x[i], x[i + 1])
        y[i] = x[i + j]
        chg = chg or bool(j)

    chg, y, x = sm_do_endrule(y, x, n, chg, end_rule)

    return chg, x, y


def sm_do_endrule(
    y: list[float],
    x: list[float],
    n: int,
    chg: bool,
    end_rule: int,
) -> tuple[bool, list[float], list[float]]:
    if end_rule == EndRule.sm_no_endrule:
        pass
    elif end_rule == EndRule.sm_copy_endrule:
        y[0] = x[0]
        y[n - 1] = x[n - 1]
    elif end_rule == EndRule.sm_tukey_endrule:
        y[0] = median([3 * y[1] - 2 * y[2], x[0], y[1]])
        chg = chg or (y[0] != x[0])
        y[n - 1] = median([y[n - 2], x[n - 1], 3 * y[n - 2] - 2 * y[n - 3]])
        chg = chg or (y[n - 1] != x[n - 1])
    else:
        msg = f"invalid end-rule for running median of 3: {end_rule}"
        raise RuntimeError(msg)

    return chg, y, x


def sm_3R(
    x: list[float],
    y: list[float],
    z: list[float],
    n: int,
    end_rule: int,
) -> tuple[int, list[float], list[float], list[float]]:
    chg, x, y = sm_3(x, y, n, 1)  # "sm_COPY_ENDRULE"
    it = int(chg)

    while chg:
        chg, y, z = sm_3(y, z, n, 0)  # "sm_NO_ENDRULE"
        if chg:
            it += 1
            for i in range(1, n - 1):
                y[i] = z[i]

    if n > 2:
        chg, y, x = sm_do_endrule(y, x, n, chg, end_rule)

    return (it, x, y, z) if it else (int(chg), x, y, z)


def sptest(x: list[float], i: int) -> bool:
    if x[i] != x[i + 1]:
        return False
    elif (x[i - 1] <= x[i] and x[i + 1] <= x[i + 2]) or (x[i - 1] >= x[i] and x[i + 1] >= x[i + 2]):
        return False
    else:
        return True


def sm_split3(x: list[float], y: list[float], n: int, do_ends: bool) -> tuple[bool, list[float], list[float]]:
    # y[] := S(x[])  where S() = "sm_split3"
    chg = False

    for i in range(n):
        y[i] = x[i]

    if n <= 4:
        return False, y, x

    # Colin Goodall doesn't do splits near ends
    # in spl() in Statlib's "smoother" code !!
    if do_ends and sptest(x, 1):
        chg = True
        y[1] = x[0]
        y[2] = med3(x[2], x[3], 3 * x[3] - 2 * x[4])

    for i in range(2, n - 3):
        if sptest(x, i):
            # plateau at x[i] == x[i+1]
            # at left :
            if (j := imed3(x[i], x[i - 1], 3 * x[i - 1] - 2 * x[i - 2])) > -1:
                y[i] = x[i - 1] if j == 0 else 3 * x[i - 1] - 2 * x[i - 2]
                chg = y[i] != x[i]
            # at right :
            if (j := imed3(x[i + 1], x[i + 2], 3 * x[i + 2] - 2 * x[i + 3])) > -1:
                y[i + 1] = x[i + 2] if j == 0 else 3 * x[i + 2] - 2 * x[i + 3]
                chg = y[i + 1] != x[i + 1]
    if do_ends and sptest(x, n - 3):
        chg = True
        y[n - 2] = x[n - 1]
        y[n - 3] = med3(x[n - 3], x[n - 4], 3 * x[n - 4] - 2 * x[n - 5])
    return chg, x, y


def sm_3RS3R(
    x: list[float],
    y: list[float],
    z: list[float],
    w: list[float],
    n: int,
    end_rule: int,
    split_ends: bool,
) -> tuple[int, list[float], list[float], list[float], list[float]]:
    # y[1:n] := "3R S 3R"(x[1:n]);  z = "work";

    it, x, y, z = sm_3R(x, y, z, n, end_rule)
    chg, y, z = sm_split3(y, z, n, split_ends)
    if chg:
        (
            it2,
            z,
            y,
            w,
        ) = sm_3R(z, y, w, n, end_rule)
        it += it2
    # else y == z already
    return (it + chg), x, y, z, w


def sm_3RSS(
    x: list[float],
    y: list[float],
    z: list[float],
    n: int,
    end_rule: int,
    split_ends: bool,
) -> tuple[int, list[float], list[float], list[float]]:
    # y[1:n] := "3RSS"(x[1:n]);  z = "work"

    it, x, y, z = sm_3R(x, y, z, n, end_rule)
    chg, y, z = sm_split3(y, z, n, split_ends)
    if chg is True:
        chg, z, y = sm_split3(z, y, n, split_ends)
    # else  y == z already
    return (it + int(chg)), x, y, z


def sm_3RSR(
    x: list[float],
    y: list[float],
    z: list[float],
    w: list[float],
    n: int,
    end_rule: int,
    split_ends: bool,
) -> tuple[int, list[float], list[float], list[float], list[float]]:
    # y[1:n] := "3RSR"(x[1:n]);  z := residuals; w = "work";

    # == "SR" (as follows) is stupid ! (MM) ==

    it, x, y, z = sm_3R(x, y, z, n, end_rule)
    chg: bool = True
    while chg:
        it += 1
        chg, y, z = sm_split3(y, z, n, split_ends)
        ch2, z, y, w = sm_3R(z, y, w, n, end_rule)
        chg = chg or bool(ch2)

        if chg is False:
            break
        if it > 2 * n:
            break  # INF.LOOP stopper
        for i in range(n):
            z[i] = x[i] - y[i]

    return it, x, y, z, w
