#!/usr/bin/python
#if.py

expect_num = 23

input_num = int(input("Enter an guess integer :"))

if input_num == expect_num:
    print("input num is %d, guess succ" %expect_num)
elif input_num < expect_num:
    print("input num is greater than expect num")
else:
    print("input num is less than expect num")

print("done")
