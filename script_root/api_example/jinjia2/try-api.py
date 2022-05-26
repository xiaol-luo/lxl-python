import logging
import jinja2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("log")
logger.setLevel(logging.DEBUG)


env = jinja2.Environment(loader=jinja2.ChoiceLoader([
    jinja2.FileSystemLoader("./templates"),
    jinja2.FileSystemLoader("./templates2"),
    ]))
test_tt = env.get_template("test.tt")
ret = test_tt.render(xxx="aaa")
logger.debug(ret)

test2_tt = env.get_template("test2.tt")
logger.debug(test2_tt.render())
