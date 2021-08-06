def underscore_to_camelcase(string_):
    components = string_.split('_')
    return ''.join(x.title() for x in components)
