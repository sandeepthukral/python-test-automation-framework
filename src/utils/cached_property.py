"""Run property initialization on first call, and get it from cache on other calls."""


def cached_property(func):
    attr_name = f'_{func.__name__}'

    @property  # type: ignore
    def wrapped(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, func(self))
        return getattr(self, attr_name)

    return wrapped
