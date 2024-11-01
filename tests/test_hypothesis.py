from typing import List

import hypothesis.strategies as st
from hypothesis import given, settings

from pysmooth.__main__ import smooth


@settings(deadline=None)
@given(x=st.lists(elements=st.integers(), min_size=3))
def test_hypo_3RS3R_int(x: List[float]) -> None:
    smooth(x=x, kind="3RS3R", twiceit=False, endrule="Tukey")
    smooth(x=x, kind="3RS3R", twiceit=False, endrule="copy")

    smooth(x=x, kind="3RS3R", twiceit=True, endrule="Tukey")
    smooth(x=x, kind="3RS3R", twiceit=True, endrule="copy")


@settings(deadline=None)
@given(x=st.lists(elements=st.integers(), min_size=3))
def test_hypo_3RSS_int(x: List[float]) -> None:
    smooth(x=x, kind="3RSS", twiceit=False, endrule="Tukey")
    smooth(x=x, kind="3RSS", twiceit=False, endrule="copy")

    smooth(x=x, kind="3RSS", twiceit=True, endrule="Tukey")
    smooth(x=x, kind="3RSS", twiceit=True, endrule="copy")


@settings(deadline=None)
@given(x=st.lists(elements=st.integers(), min_size=3))
def test_hypo_3RSR_int(x: List[float]) -> None:
    smooth(x=x, kind="3RSR", twiceit=False, endrule="Tukey")
    smooth(x=x, kind="3RSR", twiceit=False, endrule="copy")

    smooth(x=x, kind="3RSR", twiceit=True, endrule="Tukey")
    smooth(x=x, kind="3RSR", twiceit=True, endrule="copy")


@settings(deadline=None)
@given(x=st.lists(elements=st.integers(), min_size=3))
def test_hypo_3R_int(x: List[float]) -> None:
    smooth(x=x, kind="3R", twiceit=False, endrule="Tukey")
    smooth(x=x, kind="3R", twiceit=False, endrule="copy")

    smooth(x=x, kind="3R", twiceit=True, endrule="Tukey")
    smooth(x=x, kind="3R", twiceit=True, endrule="copy")


@settings(deadline=None)
@given(x=st.lists(elements=st.integers(), min_size=3))
def test_hypo_3_int(x: List[float]) -> None:
    smooth(x=x, kind="3", twiceit=False, endrule="Tukey")
    smooth(x=x, kind="3", twiceit=False, endrule="copy")

    smooth(x=x, kind="3", twiceit=True, endrule="Tukey")
    smooth(x=x, kind="3", twiceit=True, endrule="copy")


@settings(deadline=None)
@given(x=st.lists(elements=st.integers(), min_size=2, max_size=2))
def test_hypo_3_2(x: List[float]) -> None:
    smooth(x=x, kind="3", twiceit=False, endrule="Tukey")
    smooth(x=x, kind="3", twiceit=False, endrule="copy")

    smooth(x=x, kind="3", twiceit=True, endrule="Tukey")
    smooth(x=x, kind="3", twiceit=True, endrule="copy")


@settings(deadline=None)
@given(x=st.lists(elements=st.integers(), min_size=3))
def test_hypo_S_int(x: List[float]) -> None:
    smooth(x=x, kind="S", twiceit=False, endrule="Tukey")
    smooth(x=x, kind="S", twiceit=False, endrule="copy")

    smooth(x=x, kind="S", twiceit=True, endrule="Tukey")
    smooth(x=x, kind="S", twiceit=True, endrule="copy")


@settings(deadline=None)
@given(x=st.lists(elements=st.floats(allow_nan=False, allow_infinity=False), min_size=3))
def test_hypo_3RS3R_float(x: List[float]) -> None:
    smooth(x=x, kind="3RS3R", twiceit=False, endrule="Tukey")
    smooth(x=x, kind="3RS3R", twiceit=False, endrule="copy")

    smooth(x=x, kind="3RS3R", twiceit=True, endrule="Tukey")
    smooth(x=x, kind="3RS3R", twiceit=True, endrule="copy")


@settings(deadline=None)
@given(x=st.lists(elements=st.floats(allow_nan=False, allow_infinity=False), min_size=3))
def test_hypo_3RSS_float(x: List[float]) -> None:
    smooth(x=x, kind="3RSS", twiceit=False, endrule="Tukey")
    smooth(x=x, kind="3RSS", twiceit=False, endrule="copy")

    smooth(x=x, kind="3RSS", twiceit=True, endrule="Tukey")
    smooth(x=x, kind="3RSS", twiceit=True, endrule="copy")


@settings(deadline=None)
@given(x=st.lists(elements=st.floats(allow_nan=False, allow_infinity=False), min_size=3))
def test_hypo_3RSR_float(x: List[float]) -> None:
    smooth(x=x, kind="3RSR", twiceit=False, endrule="Tukey")
    smooth(x=x, kind="3RSR", twiceit=False, endrule="copy")

    smooth(x=x, kind="3RSR", twiceit=True, endrule="Tukey")
    smooth(x=x, kind="3RSR", twiceit=True, endrule="copy")


@settings(deadline=None)
@given(x=st.lists(elements=st.floats(allow_nan=False, allow_infinity=False), min_size=3))
def test_hypo_3R_float(x: List[float]) -> None:
    smooth(x=x, kind="3R", twiceit=False, endrule="Tukey")
    smooth(x=x, kind="3R", twiceit=False, endrule="copy")

    smooth(x=x, kind="3R", twiceit=True, endrule="Tukey")
    smooth(x=x, kind="3R", twiceit=True, endrule="copy")


@settings(deadline=None)
@given(x=st.lists(elements=st.floats(allow_nan=False, allow_infinity=False), min_size=3))
def test_hypo_3_float(x: List[float]) -> None:
    smooth(x=x, kind="3", twiceit=False, endrule="Tukey")
    smooth(x=x, kind="3", twiceit=False, endrule="copy")

    smooth(x=x, kind="3", twiceit=True, endrule="Tukey")
    smooth(x=x, kind="3", twiceit=True, endrule="copy")


@settings(deadline=None)
@given(x=st.lists(elements=st.floats(allow_nan=False, allow_infinity=False), min_size=3))
def test_hypo_S_float(x: List[float]) -> None:
    smooth(x=x, kind="S", twiceit=False, endrule="Tukey")
    smooth(x=x, kind="S", twiceit=False, endrule="copy")

    smooth(x=x, kind="S", twiceit=True, endrule="Tukey")
    smooth(x=x, kind="S", twiceit=True, endrule="copy")
