import jinja2

_tt_env:jinja2.Environment = None


def get_env()->jinja2.Environment:
    global _tt_env
    if not _tt_env:
        _tt_env = jinja2.Environment(loader=jinja2.PackageLoader(__package__), extensions=['jinja2.ext.do'])
    return _tt_env


def render(tt_path, *args, **kwargs):
    tt = get_template(tt_path)
    if tt:
        return True, tt.render(*args, **kwargs)
    return False, None


def get_template(tt_path):
    env = get_env()
    tt = env.get_template(tt_path)
    return tt

def set_filter(name, filter):
    env = get_env()
    env.filters[name] = filter

