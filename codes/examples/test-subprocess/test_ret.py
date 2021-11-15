import sys
import os

ret = 0;
if len(sys.argv) > 1:
    ret = int(sys.argv[1])

print("input value is ", ret)
sys.exit(ret)


