import argparse
import shlex

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", '--show',  help='determin whether show result', action='store_true')
    exclusive_group = parser.add_mutually_exclusive_group(required=True)
    #exclusive_group = parser.add_mutually_exclusive_group(required=False)
    exclusive_group.add_argument('-b', '--brief', help='show brief infomation', action='store_true')
    exclusive_group.add_argument('-d', '--detail', help='show detail infomation', action='store_true')
    parser.add_argument('square', type=int, help='display a square of a given number')

    #parser.parse_args(['-h'])
    #print("----------------------------------------------------------------\n")

    # args = parser.parse_args(['-s', '-d', '12'])
    # args = parser.parse_args(shlex.split('-b 12'))
    # args = parser.parse_args(shlex.split('-d 12'))
    # args = parser.parse_args(shlex.split('-s -b 12'))
    args = parser.parse_args(shlex.split('-s -d 12'))
    ret = args.square * args.square
    if args.show:
        if args.brief:
            print("simple show {}".format(ret))
        else:
            print("detail show {}".format(ret))
    else:
        print("not show")