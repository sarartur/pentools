class Resource(object):
    def __init__(self, uri, params = None) -> None:
        self.uri = uri
        if not params:
            self.params = dict()
        else:
            self.params = params