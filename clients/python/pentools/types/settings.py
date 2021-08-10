
class SettingsBase(object):

    def __init__(self) -> None:
        pass

    def keys(self):
        return self.__dict__.keys()

    def __getitem__(self, key):
        return getattr(self, key)

    def register_from_kwargs(self, **kwargs):
        self.__dict__.update(**kwargs)