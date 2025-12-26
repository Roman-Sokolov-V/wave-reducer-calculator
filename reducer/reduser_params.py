from dataclasses import dataclass

@dataclass
class ReducerParams:
    gear_number: int | None = None
    ball_diameter: int | float | None = None
    requested_outer_radius: int | None = None
    reducer_outer_diameter: int | None = None
    resolution: int = 600