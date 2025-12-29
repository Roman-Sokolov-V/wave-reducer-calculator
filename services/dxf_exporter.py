import ezdxf

from reducer.geometry import ReducerGeometry


class ReducerDXFExporter:
    def __init__(self, geometry: ReducerGeometry):
        self.stacked_xy = geometry.stacked_xy
        self.outer_radius = geometry.track_outer_radius
        self.track_inner_radius = geometry.track_inner_radius
        self.radius_of_separator_outer = geometry.radius_of_separator_outer
        self.radius_of_separator_inner = geometry.radius_of_separator_inner
        self.eccentricity = geometry.eccentricity
        self.eccentric_radius = geometry.eccentric_radius

    def _write_to_file_base_wheel_shape(self):
        doc = ezdxf.new("R2000")
        msp = doc.modelspace()

        msp.add_point([0, 0])
        msp.add_spline(self.stacked_xy)
        msp.add_circle((0, 0), radius=self.outer_radius)
        msp.add_circle((0, 0), radius=self.track_inner_radius)
        doc.saveas("base_wheel.dxf")

    def _write_to_file_separator(self):
        doc = ezdxf.new("R2000")
        msp = doc.modelspace()

        msp.add_circle((0, 0), radius=self.radius_of_separator_outer)
        msp.add_circle((0, 0), radius=self.radius_of_separator_inner)
        doc.saveas("separator.dxf")

    def _write_to_file_eccentric(self):
        doc = ezdxf.new("R2000")
        msp = doc.modelspace()

        msp.add_point([0, self.eccentricity])
        msp.add_lwpolyline([[0, 0], [0, self.eccentricity]])
        msp.add_lwpolyline([[-6, 0], [6, 0]])
        msp.add_lwpolyline([[-3, self.eccentricity], [3, self.eccentricity]])
        msp.add_circle((0, self.eccentricity), radius=self.eccentric_radius)
        doc.saveas("eccentric.dxf")

    def write_profiles_to_files(
        self,
            will_shape: bool = True,
            separator: bool = True,
            eccentric: bool = True
    ):
        if will_shape:
            self._write_to_file_base_wheel_shape()
        if separator:
            self._write_to_file_separator()
        if eccentric:
            self._write_to_file_eccentric()
