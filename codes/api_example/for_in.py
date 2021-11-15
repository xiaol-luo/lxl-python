#!/usr/bin/python
#for_in.py

for i in range(1, 10, 2):
    print("num is", i)
else:
    print("exit normal will excute else, but not break")

for i in range(1, 10):
    print("other num is", i)
    if 5 == i:
        print("hit break, not excute else part")
        break
else:
    print("exit normal will excute else, but not break")
