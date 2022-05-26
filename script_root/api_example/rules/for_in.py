#!/usr/bin/python
#for_in.py

for i in range(0, 10, 1):
    print("num is", i)
else:
    print("exit normal will excute else, but not break")

for i in range(0, -10, -1):
    print("other num is", i)
    if -5 == i:
        print("hit break, not excute else part")
        break
else:
    print("exit normal will excute else, but not break")
