def create_types_message(types, full = False):
    msg = f"\nAvailable {'scripts and types' if full else 'types'}\n\n"
    for i, type_ in enumerate(types):
        msg += f"{i}. {type_['name']}\n"
        if full:
            msg += f"\t{type_['description']}\n"
            for i, script in enumerate(type_['scripts']):
                msg += f"\t\t{i}. {script['name']} [id: {script['id']}]{tuple(os['name'] for os in script['operating_systems'])}\n"
    return msg

def create_script_message(script, full = False):
    msg = '\n'
    if full:
        msg += f"id: {script['id']}\n"
        msg += f"operating systems: {tuple(os['name'] for os in script['operating_systems'])}\n\n"
    msg += "---------------(code)---------------\n\n"
    msg += f"{script['code']}\n\n"
    msg += "-------------(end code)-------------\n"
    return msg