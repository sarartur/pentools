from .types.settings import SettingsBase

class Settings(SettingsBase):

    def __init__(self, **kwargs) -> None:
        SettingsBase.__init__(self)
        self.base_url = "https://pentools.herokuapp.com"
        self.script_type = "all"
        self.full = None
        self.script_id = None
        self.encoding = None
        self.port = None
        self.host = None
        self.shell = None

        options = {k:v for k,v in kwargs.items() if v}
        self.register_from_kwargs(**options)
