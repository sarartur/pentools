from urllib.parse import quote
import base64

from . import enums

def format_code(script, encoding = None, **kwargs):
    kwargs = {k: v for k, v in kwargs.items() if v}
    for k,v in kwargs.items():
        script.code = script.code.replace(f"<(({k}))>", str(v))
    if encoding == enums.Encoding.url:
        script.code = quote(script.code)
    elif encoding == enums.Encoding.base64:
        script.code = base64.b64encode(bytes(script.code, 'utf-8'))
    else:
        pass
    return script


