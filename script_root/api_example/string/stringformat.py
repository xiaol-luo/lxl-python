from string import Template

format_1 = "{0} {1} {0}"
format_2 = "{me} {you} {me}"

print("{0} {1} {0}".format("00", "11"))
print("{me} {you} {me}".format(me="Me", you="You"))

dict = {"me": "DICT_ME", "you": "DICT_YOU"}
print("{0[me]}, {0[you]}".format(dict))


class Item:
    def __init__(self):
        self.me = "Item_Me"
        self.you = "Item_You"


item = Item()
print("{0.me}, {0.you}".format(item))
print("{item.me}, {item.you}".format(item=item))

template_1 = "template 1 $me $you $me"
template_2 = "template 2 $me $you $me"

t1 = Template(template_1)
print(t1.substitute(me="ME", you="YOU"))

t2 = Template(template_2)
print(t2.substitute(dict))

print("{0:x<+30.10f}---{1:y^ 20.5f}".format(1.0, -2.0))
print("{0:x>+30.10f}---{1:y^ 20.5f}".format(-1.0, 2.0))
print("{0:x=+30.10f}---{1:y^ 20.5f}".format(-1.0, 2.0))
