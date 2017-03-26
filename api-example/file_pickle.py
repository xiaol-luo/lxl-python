#!/usr/bin/python
#file_pickle.py

import pickle as p
import string

file_name = 'tmp_item.txt'
f = open(file_name, 'w')
f.truncate()
write_items = ['apple', 'boy', 'cat']
base_string = "the item is {0}\n"
for item in write_items:
    f.write(base_string.format(item))
f.close()

f = open(file_name, 'r')
while (True):
    line_str = f.readline()
    if line_str:
        print(line_str)
    else:
        break
f.close()

pickle_file = 'pickle_file.data'
pickle_list = ['apple', 'orange']
print("pickle_list:", pickle_list)
f = open(pickle_file, 'wb')
p.dump(pickle_list, f)
f.close()
del pickle_list

f = open(pickle_file, 'rb')
storedlist = p.load(f)
print("storelist:", storedlist)



