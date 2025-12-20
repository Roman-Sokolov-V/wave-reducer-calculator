class TooSmallRequstedRadius(Exception):

    def __init__(self, message="requested_outer_radius is too small"):
        super().__init__(message)
