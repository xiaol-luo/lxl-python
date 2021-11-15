import logging

logging.basicConfig(level=logging.DEBUG)

def try_sum(num):
    logging.debug("try_sum start input num : {}".format(num))
    sum = num
    loop = 0
    while loop < 2:
        loop = loop + 1
        num = yield (False, sum)
        sum = sum + num
        logging.debug("try_sum continue input num : %d， sum : %d", num, sum)
    yield (True, sum)

co_item = try_sum(3)
logging.debug("co_item %s",co_item)
co_ret = next(co_item)
logging.debug("co_ret %s", co_ret)
while not co_ret[0]:
    input_str = input("input num :")
    num = int(input_str)
    co_ret = co_item.send(num)
    logging.debug("co_ret %s", co_ret)

logging.debug("---------------- try generator in for --------------- ")
def try_gen_num(begin, end):
    while (begin < end):
        yield begin
        begin = begin + 1

for num in try_gen_num(1, 10):
    logging.debug("try_gen_num ret %d", num)


#yield from genernater
def wrap_try_sum(num):
    logging.debug("wrap_try_sum start")
    yield from try_sum(num)
    logging.debug("wrap_try_sum end")

logging.debug("excute wrap_try_sum")
co_wrap_item = wrap_try_sum(1)
co_wrap_ret = next(co_wrap_item)
while not co_wrap_ret[0]:
    input_str = input("wrapper input num :")
    num = int(input_str)
    co_wrap_ret = co_wrap_item.send(num)
    logging.debug("co_wrap_item %s", co_wrap_ret)