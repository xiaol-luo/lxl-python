import logging

logging.basicConfig(level=logging.DEBUG)

#positional argument -> like v
#keyword argument -> argument like k=v
#1.keyword argument must behind positional
#2.*args hold the extra positional argument
#3. **kwargs hold the extra keyword argument
#4. *args and **kwargs means that expand them as function arguments: 
#   arg[0], arg[1],..., k1=v1, k2=v2,...


def test_1(tag, a, b, c):
    logging.debug("test_1 tag:%s %s %s %s", tag, a, b, c)

def test_2(tag, a, b, c, *args, **kwargs):
    logging.debug("test_2 tag:%s %s %s %s", tag, a, b, c)    
    logging.debug("test_2 args %s", ",".join("{}".format(i) for i in args))
    logging.debug("test_2 kwargs %s", ",".join("{}:{}".format(k, v) for k, v in kwargs.items()))

def test_3(tag, *args, **kwargs):
    test_2(tag, *args, **kwargs)

def test_4(tag, a, b, x=10, y=20):
    logging.debug("test_4 tag:%s %s %s %s %s", tag, a, b, x, y)    
    #logging.debug("test_4 args %s", ",".join("{}".format(i) for i in args))
    #logging.debug("test_4 kwargs %s", ",".join("{}:{}".format(k, v) for k, v in kwargs.items()))



if __name__ == "__main__":
    test_1("a", 1, 2, 3)
    test_1("b", 1, c=2, b=3)
    #test_1("c", 1, c=2, 3) #invalid
    #test_1("d", 1, 2, b=3) #invalid
    test_2("a", 1, 2, 3, 4, x=1, y=2)
    test_2("b", 1, 2, 3, 4, 5, x=1, y=2)
    test_2("c", 1, 2, 3, 4, 5, 6, x=1, y=2)
    #test_2("d", 1, 2, x=1, y=2) #invalid
    #test_2("e", 1, 2, 3, x=1, y=2, 4, 5) #invalid
    test_2("f", 1, b=2, c=3, x=1, y=2)

    test_3("test_3 call a", 1, 2, 3, x=1, y=2)
    #test_3("test_3 call b", 1, 2, 3, b=1, y=2) #invalid mutiple b
    #test_3("test_3 call c", 1, 2, x=1, y=2) #invalid miss c
    test_3("test_3 call d", 1, 2, 3, 4, x=1, y=2)

    #try
    dict_arguments = {"x":1, "y":2}
    list_arguments = [4, 5, 6]
    test_2("try a", *list_arguments, **dict_arguments)
    test_2("try b", 1, *list_arguments, **dict_arguments)

    test_4("a", 1, 2, x=3, y=4)
    test_4("b", 1, 2, x=3)
    test_4("c", 1, 2)