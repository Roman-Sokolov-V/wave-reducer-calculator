from dataclasses import dataclass

@dataclass
class ReducerParams:
    gear_number: int
    ball_diameter: int
    requested_outer_radius: int | None = None
    reducer_outer_diameter: int | None = None
    resolution: int = 600
