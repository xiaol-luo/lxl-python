import argparse
import codecs
import re
import datetime
import time

parser = argparse.ArgumentParser()
parser.add_argument("file", help="target file")
parser.add_argument("begin", help="begin time")
parser.add_argument("end", help="end time")

args = parser.parse_args()

max_dt = datetime.datetime.min
min_dt= datetime.datetime.max

#max_dt = datetime.datetime.fromtimestamp(int(datetime.date.min.time())) 
#min_dt = datetime.datetime.fromtimestamp(int(datetime.date.min.time()))

net_records = []
total = 0.0
with codecs.open(args.file, 'r', 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
        ret = re.match(".*:(?P<year>[0-9]+)-(?P<month>[0-9]{1,2})-(?P<day>[0-9]{1,2}),(?P<hour>[0-9]{1,2}):(?P<min>[0-9]{1,2}):(?P<sec>[0-9]{1,2}).*new message.*len:(?P<num>[0-9]+).*", line)
        if ret:
            num = ret.group("num")
            year = int(ret.group("year"))
            month = int(ret.group("month"))
            day = int(ret.group("day"))
            hour = int(ret.group("hour"))
            minute = int(ret.group("min"))
            sec = int(ret.group("sec"))
            dt = datetime.datetime(year, month, day, hour, minute, sec)
            begin_dt = datetime.datetime.strptime(args.begin, "%Y-%m-%d,%H:%M:%S")
            end_dt = datetime.datetime.strptime(args.end, "%Y-%m-%d,%H:%M:%S")
            if dt > begin_dt and dt <= end_dt:
                total = total + float(num)
                net_records.append(num)
            if dt > max_dt:
                max_dt = dt
            if dt < min_dt:
                min_dt = dt            

print(",".join(net_records))
print("from {0} to {1} total is {2}".format(min_dt, max_dt, total))
print("from {0} to {1} total is {2}".format(min_dt, max_dt, total/1024))
