import numpy as np
from math import ceil
from functools import cached_property

from .reducer_params import ReducerParams
from .exeptions import TooSmallRequstedRadius


class ReducerGeometry:
    def __init__(self, params: ReducerParams):
        self.gear_number = params.gear_number
        self.ball_diameter = params.ball_diameter
        self.requested_outer_radius = params.requested_outer_radius
        self.reducer_outer_diameter = params.reducer_outer_diameter
        self.resolution = params.resolution


    @cached_property
    def eccentricity(self) -> float:
        return 0.2 * self.ball_diameter

    @cached_property
    def number_of_waves(self) -> int:
        return self.gear_number + 1

    @cached_property
    def min_inner_radius(self) -> float:
        return ceil(1.03 * self.ball_diameter) / np.sin(np.pi / self.number_of_waves)

    @cached_property
    def balls_radius(self) -> float:
        return self.ball_diameter / 2

    @cached_property
    def separator_thickness(self) -> float:
        return 2.2 * self.eccentricity


    def _get_inner_radius_from_outer(self, outer_radius) -> float:
        return outer_radius - 2 * self.eccentricity


    def _get_outer_radius_from_inner(self, inner_radius) -> int:
        return math.ceil(inner_radius + 2 * self.eccentricity)


    @cached_property
    def outer_radius(self) -> float:
        if self.requested_outer_radius is not None:
            inner_radius = self._get_inner_radius_from_outer(self.requested_outer_radius)

            if inner_radius <= self.min_inner_radius:
                raise TooSmallRequstedRadius

            return self.requested_outer_radius
        return self._get_outer_radius_from_inner(self.min_inner_radius)

    @cached_property
    def inner_radius(self) -> float:
        return self._get_inner_radius_from_outer(self.outer_radius)


    @cached_property
    def eccentric_radius(self):
        return self.inner_radius + self.eccentricity - self.ball_diameter


    @cached_property
    def radius_of_separator_outer(self) -> float:
        return self.eccentric_radius + self.balls_radius + self.separator_thickness / 2

    @cached_property
    def radius_of_separator_inner(self) -> float:
        return self.radius_of_separator_outer - self.separator_thickness


    @cached_property
    def xy(self) -> tuple[np.ndarray]:
        theta = np.linspace(0, 2 * np.pi, self.resolution)
        S = np.sqrt(
            (self.balls_radius + self.eccentric_radius) ** 2
            - np.power(self.eccentricity * np.sin(self.number_of_waves * theta), 2)
        )
        l = self.eccentricity * np.cos(self.number_of_waves * theta) + S
        Xi = np.arctan2(self.eccentricity * self.number_of_waves * np.sin(self.number_of_waves * theta), S)

        x = l * np.sin(theta) + self.balls_radius * np.sin(theta + Xi)
        y = l * np.cos(theta) + self.balls_radius * np.cos(theta + Xi)
        return (x, y)


    @cached_property
    def stacked_xy(self) -> np.ndarray:
        return np.stack(self.xy, axis=1)


    @cached_property
    def balls_centers(self) -> zip:
        sh_angle = np.linspace(0, 1, self.gear_number + 1) * 2 * np.pi
        S_sh = np.sqrt((self.balls_radius + self.eccentric_radius) ** 2 - np.power(
            self.eccentricity * np.sin(self.number_of_waves * sh_angle), 2))
        l_Sh = self.eccentricity * np.cos(self.number_of_waves * sh_angle) + S_sh
        x_centers = l_Sh * np.sin(sh_angle)
        y_centers = l_Sh * np.cos(sh_angle)
        return zip(x_centers, y_centers)
