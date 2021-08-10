import requests
from functools import wraps

from .types.resource import Resource
from .types.response import Response


class Client(object):
    def __init__(self, base_url, **kwargs) -> None:
        self.base_url = base_url

    def endpoint(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            resource = func(self, *args, **kwargs)
            r = requests.get(
                url = self.base_url + resource.uri,
                params = resource.params
            )
            if r.status_code == 422:
                try:
                    detail = r.json()['detail'][0]
                    param_name = detail['loc'][1]
                    msg = r.json()['detail'][0]['msg']
                    val = kwargs.get(param_name)
                    if not val:
                        val = 'null'
                    err_msg = msg.replace('value', f"{param_name} (val: {val})", 1)
                except:
                    pass
                else:
                    return Response(err_msg, err = True)
            if r.status_code == 200:
                return Response(r.json())
            return Response(f"Server error {r.status_code}", err = True)
        return wrapper

    @endpoint
    def get_script_types(self, script_type, **kwargs):
        return Resource(
            uri = f"/types/{script_type}")

    @endpoint
    def get_script_by_id(self, script_id, port, host, encoding, shell, **kwargs):
        return Resource(
            uri = "/scripts",
            params = {
                "id": script_id, "port": port,
                "host": host, "encoding": encoding,
                "shell": shell
        })

    @endpoint
    def get_script_by_name_and_type(self, script_type, script_name,
                port, host, encoding, shell, **kwargs):
        return Resource(
            uri = f"/{script_type}/{script_name}",
            params = {
                "port": port,"host": host, 
                "encoding": encoding, "shell": shell
        })