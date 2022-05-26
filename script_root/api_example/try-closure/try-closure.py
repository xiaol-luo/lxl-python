import logging

logging.basicConfig(level=logging.DEBUG)

void_fun = lambda : "hello void_fun"
logging.debug(void_fun())

one_param_func = lambda x: "one_param_fun input is {}".format(x)
logging.debug(one_param_func("xxx"))

two_param_fun = lambda x, y: "tow_param_fun input is {}:{}".format(x, y)
logging.debug(two_param_fun("xxx", "yyy"))

def gen_closure(subfix):
    def append_subfix(name):
        return name + subfix
    return append_subfix

def gen_lambda_closure(subfix):
    lambda_fun = lambda name: name + subfix
    return lambda_fun

closure = gen_closure(".txt")
logging.debug("closure ret %s", closure("xxx"))

lambda_closure = gen_lambda_closure(".txt")
logging.debug("lambda_closure ret %s", lambda_closure("xxx"))