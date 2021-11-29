from typing import Any, List

import numpy as np
import pytest

from pysmooth import smooth


@pytest.fixture
def test_arr() -> List[float]:
    return [
        25,
        7,
        10,
        8,
        39,
        22,
        41,
        43,
        36,
        29,
        33,
        50,
        26,
        47,
        32,
        9,
        42,
        20,
        45,
        37,
        18,
        35,
        28,
        14,
        15,
        46,
        21,
        19,
        17,
        4,
        11,
        27,
        12,
        40,
        3,
        34,
        23,
        49,
        44,
        5,
        48,
        30,
        13,
        2,
        24,
        6,
        1,
        31,
        16,
        38,
    ]


@pytest.fixture
def expected_3RS3R() -> List[float]:
    return [
        10,
        10,
        10,
        10,
        22,
        39,
        41,
        41,
        36,
        33,
        33,
        33,
        33,
        32,
        32,
        32,
        32,
        37,
        37,
        37,
        35,
        28,
        28,
        28,
        21,
        21,
        19,
        19,
        17,
        13,
        12,
        12,
        12,
        23,
        27,
        34,
        34,
        44,
        44,
        44,
        30,
        30,
        13,
        13,
        6,
        6,
        6,
        16,
        31,
        38,
    ]


def test_3RS3R(test_arr: List[float], expected_3RS3R: List[float]) -> None:
    results = smooth(x=test_arr, kind="3RS3R", twiceit=False, endrule="Tukey")

    assert results == expected_3RS3R


@pytest.fixture
def expected_3RSS() -> List[float]:
    return [
        10,
        10,
        10,
        10,
        22,
        39,
        41,
        41,
        36,
        33,
        33,
        33,
        33,
        32,
        32,
        32,
        32,
        37,
        37,
        37,
        35,
        28,
        28,
        28,
        21,
        15,
        21,
        19,
        17,
        13,
        12,
        12,
        12,
        23,
        27,
        34,
        34,
        44,
        44,
        44,
        30,
        30,
        13,
        13,
        6,
        6,
        6,
        16,
        31,
        38,
    ]


def test_3RSS(test_arr: List[float], expected_3RSS: List[float]) -> None:
    results = smooth(x=test_arr, kind="3RSS", twiceit=False, endrule="Tukey")

    assert results == expected_3RSS


@pytest.fixture
def expected_3RSR() -> List[float]:
    return [
        10,
        10,
        10,
        10,
        22,
        39,
        41,
        41,
        36,
        33,
        33,
        33,
        33,
        32,
        32,
        32,
        32,
        37,
        37,
        37,
        35,
        28,
        28,
        28,
        21,
        21,
        19,
        19,
        17,
        13,
        12,
        12,
        12,
        23,
        27,
        34,
        34,
        44,
        44,
        44,
        30,
        30,
        13,
        13,
        6,
        6,
        6,
        16,
        31,
        38,
    ]


def test_3RSR(test_arr: List[float], expected_3RSR: List[float]) -> None:
    results = smooth(x=test_arr, kind="3RSR", twiceit=False, endrule="Tukey")

    assert results == expected_3RSR


@pytest.fixture
def expected_3R() -> List[float]:
    return [
        10,
        10,
        10,
        10,
        22,
        39,
        41,
        41,
        36,
        33,
        33,
        33,
        33,
        32,
        32,
        32,
        32,
        37,
        37,
        37,
        35,
        28,
        28,
        15,
        15,
        21,
        21,
        19,
        17,
        11,
        11,
        12,
        12,
        23,
        27,
        34,
        34,
        44,
        44,
        44,
        30,
        30,
        13,
        13,
        6,
        6,
        6,
        16,
        31,
        38,
    ]


def test_3R(test_arr: List[float], expected_3R: List[float]) -> None:
    results = smooth(x=test_arr, kind="3R", twiceit=False, endrule="Tukey")

    assert results == expected_3R


@pytest.fixture
def expected_3() -> List[float]:
    return [
        14,
        10,
        8,
        10,
        22,
        39,
        41,
        41,
        36,
        33,
        33,
        33,
        47,
        32,
        32,
        32,
        20,
        42,
        37,
        37,
        35,
        28,
        28,
        15,
        15,
        21,
        21,
        19,
        17,
        11,
        11,
        12,
        27,
        12,
        34,
        23,
        34,
        44,
        44,
        44,
        30,
        30,
        13,
        13,
        6,
        6,
        6,
        16,
        31,
        38,
    ]


def test_3(test_arr: List[float], expected_3: List[float]) -> None:
    results = smooth(x=test_arr, kind="3", twiceit=False, endrule="Tukey")

    assert results == expected_3


@pytest.fixture
def expected_S() -> List[float]:
    return [
        25,
        7,
        10,
        8,
        39,
        22,
        41,
        43,
        36,
        29,
        33,
        50,
        26,
        47,
        32,
        9,
        42,
        20,
        45,
        37,
        18,
        35,
        28,
        14,
        15,
        46,
        21,
        19,
        17,
        4,
        11,
        27,
        12,
        40,
        3,
        34,
        23,
        49,
        44,
        5,
        48,
        30,
        13,
        2,
        24,
        6,
        1,
        31,
        16,
        38,
    ]


def test_S(test_arr: List[float], expected_S: List[float]) -> None:
    results = smooth(x=test_arr, kind="S", twiceit=False, endrule="Tukey")

    assert results == expected_S


def test_bad_smoother(test_arr: List[Any]) -> None:
    with pytest.raises(RuntimeError):
        smooth(x=test_arr, kind="30Rock", twiceit=False, endrule="Tukey", do_ends=True)


def test_bad_endrule(test_arr: List[Any]) -> None:
    with pytest.raises(RuntimeError):
        smooth(x=test_arr, kind="3", twiceit=False, endrule="Turkey", do_ends=True)


@pytest.fixture
def test_arr_with_nas() -> List[float]:
    return [
        25,
        7,
        10,
        8,
        39,
        22,
        41,
        43,
        36,
        29,
        np.nan,
        50,
        26,
        47,
        32,
        9,
        42,
        20,
        45,
        37,
        18,
        35,
        28,
        14,
        15,
        46,
        21,
        19,
        17,
        4,
        11,
        27,
        12,
        40,
        3,
        34,
        23,
        49,
        44,
        5,
        48,
        30,
        13,
        2,
        24,
        6,
        1,
        31,
        16,
        38,
    ]


def test_nan(test_arr_with_nas: List[float]) -> None:
    with pytest.raises(ValueError):
        smooth(x=test_arr_with_nas, kind="3RS3R", twiceit=False, endrule="Tukey")


# @pytest.fixture
# def test_arr_with_nonnumbers() -> List[Any]:
#     return [
#         25,7,10,8,39,22,41,43,36,29,"sabot",50,26,47,32,9,42,20,45,37,18,35,28,14,
#         15,46,21,19,17,4,11,27,12,40,3,34,23,49,44,5,48,30,13,2,24,6,1,31,16,
#         38,
#     ]


# def test_nonnumbers(test_arr_with_nonnumbers: List[Any]) -> None:
#     with pytest.raises(ValueError):
#         @typeguard_ignore
#         smooth(
#           x=test_arr_with_nonnumbers,
#           kind="3RS3R",
#           twiceit=False,
#           endrule="Tukey"
#         )
