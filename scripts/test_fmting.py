import requests

HOST = "123.21.234.12"
PORT = 12341
SHELL = "bin/bash"

kwargs = {
    'host': HOST,
    'port': PORT,
    'shell': SHELL
}

r = requests.get('http://127.0.0.1:8000/all')
assert(r.status_code == 200)
for type_ in r.json():
    for script in type_['scripts']:
        replacement_mapping = {f"<(({k}))>": v for k, v in kwargs.items() if f"<{({k})}/>" in script['code']}
        for k,v in replacement_mapping.items():
            script['code'] = script['code'].replace(k, v)
        for v in replacement_mapping.values():
            assert(v in script['code'])