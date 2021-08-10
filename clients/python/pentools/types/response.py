class Response(object):

    def __init__(self, data, err = None) -> None:
        self.data = data
        self.err = err