import matplotlib.pyplot as plt

from reducer.geometry import ReducerGeometry


class ReducerVisualizer:
    def __init__(self, geometry: ReducerGeometry):
        self.eccentricity = geometry.eccentricity
        self.reducer_outer_diameter = geometry.reducer_outer_diameter
        self.requested_outer_radius = geometry.requested_outer_radius
        self.eccentric_radius = geometry.eccentric_radius
        self.radius_of_separator_outer = geometry.radius_of_separator_outer
        self.radius_of_separator_inner =geometry.radius_of_separator_inner
        self.xy = geometry.xy
        self.balls_centers = geometry.balls_centers
        self.balls_radius = geometry.balls_radius

    def _wave(self, ax):
        ax.plot(*self.xy, color='b', linewidth=2.0)

        if self.reducer_outer_diameter is None or self.reducer_outer_diameter < self.requested_outer_radius * 2 + 5:
            self.reducer_outer_diameter = self.requested_outer_radius * 2 + 5
        reduser_outer_circle = plt.Circle(
            (0, 0), self.reducer_outer_diameter / 2, color='b', fill=False, linewidth=2.0
        )
        ax.add_patch(reduser_outer_circle)

    def _eccentric(self, ax):
        ax.plot([0, 0], (0, self.eccentricity), ".", linewidth=1.0)
        ax.plot([-6, 6], (0, 0), "--k", linewidth=1.0)
        ax.plot([-3, 3], (self.eccentricity, self.eccentricity), "--k", linewidth=1.0)

        eccentric_circle = plt.Circle(
            (0, self.eccentricity), self.eccentric_radius, color='g', fill=False, linewidth=1.0
        )
        ax.add_patch(eccentric_circle)

    def _separator(self, ax):
        outer_separator_circle = plt.Circle((0, 0), self.radius_of_separator_outer, fill=False, linewidth=1.0)
        inner_separator_circle = plt.Circle((0, 0), self.radius_of_separator_inner, fill=False, linewidth=1.0)
        ax.add_patch(outer_separator_circle)
        ax.add_patch(inner_separator_circle)

    def _balls(self, ax):
        for coord in self.balls_centers:
            sh_circle = plt.Circle((coord[0], coord[1]), self.balls_radius, color='r', fill=False, linewidth=1.0)
            ax.add_patch(sh_circle)


    def show(self, wave: bool = True, separator: bool = True, balls: bool = True, eccentric: bool = True):

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.plot(0, 0, linewidth=1.0)

        if wave is True:
            self._wave(ax)

        if eccentric is True:
            self._eccentric(ax)

        if separator is True:
            self._separator(ax)

        if balls is True:
            for coord in self.balls_centers:
                self._balls(ax)
        plt.title('Wave reduser', fontsize=20, fontweight='bold', color='r')
        plt.show()
