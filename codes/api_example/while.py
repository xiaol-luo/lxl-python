#!/usr/bin/python
#while.py

running = True

while running:
    opera = input("your operation(c, b, s) : ")

    if "c" == opera:
        continue

    if "b" == opera:
        print("hit break, will not excute the code of else part")
        break

    if "s" == opera:
        running = False

else:
    print("the while loop finish, if while break because of break will not reach here")
