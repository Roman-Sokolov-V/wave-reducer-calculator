import math
import numpy as np
import pytest

from reducer.geometry import ReducerGeometry
from reducer.exeptions import TooSmallRequstedRadius


class DummyReducerParams:
    def __init__(
        self,
        gear_number=10,
        ball_diameter=10.0,
        requested_outer_radius=None,
        reducer_outer_diameter=None,
        resolution=1000,
    ):
        self.gear_number = gear_number
        self.ball_diameter = ball_diameter
        self.requested_outer_radius = requested_outer_radius
        self.reducer_outer_diameter = reducer_outer_diameter
        self.resolution = resolution


# -------------------------
# BASIC PROPERTIES
# -------------------------

def test_eccentricity():
    params = DummyReducerParams(ball_diameter=10)
    geo = ReducerGeometry(params)

    assert geo.eccentricity == 2.0


def test_number_of_waves():
    params = DummyReducerParams(gear_number=15)
    geo = ReducerGeometry(params)

    assert geo.number_of_waves == 16


def test_balls_radius():
    params = DummyReducerParams(ball_diameter=8)
    geo = ReducerGeometry(params)

    assert geo.balls_radius == 4


def test_separator_thickness():
    params = DummyReducerParams(ball_diameter=10)
    geo = ReducerGeometry(params)

    assert geo.separator_thickness == pytest.approx(2.2 * geo.eccentricity)


# -------------------------
# RADII LOGIC
# -------------------------

def test_min_inner_radius_positive():
    params = DummyReducerParams()
    geo = ReducerGeometry(params)

    assert geo.min_inner_radius > 0


def test_outer_radius_auto_calculated():
    params = DummyReducerParams(requested_outer_radius=None)
    geo = ReducerGeometry(params)

    assert geo.outer_radius > geo.min_inner_radius


def test_outer_radius_from_request():
    params = DummyReducerParams(requested_outer_radius=100)
    geo = ReducerGeometry(params)

    assert geo.outer_radius == 100
    assert geo.inner_radius == pytest.approx(100 - 2 * geo.eccentricity)


def test_too_small_requested_radius_raises():
    params = DummyReducerParams(requested_outer_radius=1)
    geo = ReducerGeometry(params)

    with pytest.raises(TooSmallRequstedRadius):
        _ = geo.outer_radius


# -------------------------
# ECCENTRIC RADIUS
# -------------------------

def test_eccentric_radius_formula():
    params = DummyReducerParams()
    geo = ReducerGeometry(params)

    expected = geo.inner_radius + geo.eccentricity - geo.ball_diameter
    assert geo.eccentric_radius == pytest.approx(expected)


# -------------------------
# SEPARATOR RADII
# -------------------------

def test_separator_radii_relation():
    params = DummyReducerParams()
    geo = ReducerGeometry(params)

    assert geo.radius_of_separator_outer > geo.radius_of_separator_inner
    assert geo.radius_of_separator_outer - geo.radius_of_separator_inner == pytest.approx(
        geo.separator_thickness
    )


# -------------------------
# XY GEOMETRY
# -------------------------

def test_xy_shapes():
    params = DummyReducerParams(resolution=500)
    geo = ReducerGeometry(params)

    x, y = geo.xy

    assert isinstance(x, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert x.shape == (500,)
    assert y.shape == (500,)


def test_stacked_xy_shape():
    params = DummyReducerParams(resolution=300)
    geo = ReducerGeometry(params)

    stacked = geo.stacked_xy

    assert stacked.shape == (300, 2)


# -------------------------
# BALL CENTERS
# -------------------------

def test_balls_centers_count():
    params = DummyReducerParams(gear_number=12)
    geo = ReducerGeometry(params)

    centers = list(geo.balls_centers)

    assert len(centers) == 13  # gear_number + 1


def test_balls_centers_are_tuples():
    params = DummyReducerParams()
    geo = ReducerGeometry(params)

    x, y = next(iter(geo.balls_centers))

    assert isinstance(x, (float, np.floating))
    assert isinstance(y, (float, np.floating))


# -------------------------
# CACHED PROPERTY BEHAVIOR
# -------------------------

def test_cached_property_same_object():
    params = DummyReducerParams()
    geo = ReducerGeometry(params)

    x1 = geo.xy
    x2 = geo.xy

    assert x1 is x2