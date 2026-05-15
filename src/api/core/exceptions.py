class FuelAPIBase(Exception):
    pass


class UsernameTaken(FuelAPIBase):
    pass


class UnknownAccount(FuelAPIBase):
    pass


class NoAuth(FuelAPIBase):
    pass


class Unauthenticated(FuelAPIBase):
    pass


class NoAction(FuelAPIBase):
    pass
