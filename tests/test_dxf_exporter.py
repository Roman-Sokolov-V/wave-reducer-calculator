import numpy as np
import pytest
from unittest.mock import MagicMock, patch

from services.dxf_exporter import ReducerDXFExporter


class DummyGeometry:
    stacked_xy = np.array([[0, 0], [1, 1]])
    outer_radius = 100.0
    inner_radius = 80.0
    radius_of_separator_outer = 60.0
    radius_of_separator_inner = 50.0
    eccentricity = 5.0
    eccentric_radius = 20.0

@patch("services.dxf_exporter.ezdxf.new")
def test_write_base_wheel_shape(mock_new):
    mock_doc = MagicMock()
    mock_msp = MagicMock()

    mock_new.return_value = mock_doc
    mock_doc.modelspace.return_value = mock_msp

    exporter = ReducerDXFExporter(DummyGeometry())
    exporter._write_to_file_base_wheel_shape()

    mock_new.assert_called_once_with("R2000")
    mock_doc.modelspace.assert_called_once()

    mock_msp.add_point.assert_called_once_with([0, 0])
    mock_msp.add_spline.assert_called_once()
    mock_msp.add_circle.assert_any_call((0, 0), radius=100.0)
    mock_msp.add_circle.assert_any_call((0, 0), radius=80.0)

    mock_doc.saveas.assert_called_once_with("base_wheel.dxf")


@patch("services.dxf_exporter.ezdxf.new")
def test_write_separator(mock_new):
    mock_doc = MagicMock()
    mock_msp = MagicMock()

    mock_new.return_value = mock_doc
    mock_doc.modelspace.return_value = mock_msp

    exporter = ReducerDXFExporter(DummyGeometry())
    exporter._write_to_file_separator()

    mock_msp.add_circle.assert_any_call((0, 0), radius=60.0)
    mock_msp.add_circle.assert_any_call((0, 0), radius=50.0)

    mock_doc.saveas.assert_called_once_with("separator.dxf")

@patch("services.dxf_exporter.ezdxf.new")
def test_write_eccentric(mock_new):
    mock_doc = MagicMock()
    mock_msp = MagicMock()

    mock_new.return_value = mock_doc
    mock_doc.modelspace.return_value = mock_msp

    exporter = ReducerDXFExporter(DummyGeometry())
    exporter._write_to_file_eccentric()

    mock_msp.add_point.assert_called_once_with([0, 5.0])
    mock_msp.add_circle.assert_called_once_with(
        (0, 5.0), radius=20.0
    )

    mock_doc.saveas.assert_called_once_with("eccentric.dxf")


def test_write_profiles_calls_correct_methods():
    exporter = ReducerDXFExporter(DummyGeometry())

    exporter._write_to_file_base_wheel_shape = MagicMock()
    exporter._write_to_file_separator = MagicMock()
    exporter._write_to_file_eccentric = MagicMock()

    exporter.write_profiles_to_files(
        will_shape=True,
        separator=False,
        eccentric=True
    )

    exporter._write_to_file_base_wheel_shape.assert_called_once()
    exporter._write_to_file_separator.assert_not_called()
    exporter._write_to_file_eccentric.assert_called_once()


