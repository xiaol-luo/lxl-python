#!/usr/bin/python
# regex.py

import re;
import os;
import glob;
#encoding=utf-8

use_gold_dict = {}
use_gold_bind_dict = {}

def analyse_use_gold_bind(use_log):
    global use_gold_bind_dict;
    
    p = re.compile(r"\[.*?\] MoneyGold \(Info\): \[Money::UseGoldBind Succ\]\[user\[(?P<name>\S*) (?P<uid>\d*)\] .*? use_gold_bind:(?P<gold_bind>\d+)")
    mr = p.match(use_log)
    if (None != mr) :
        #print(mr.span(), mr.group(), "user_name:", mr.group("name"), "uid:", mr.group("uid"), "gold_bind:", mr.group("gold_bind"))
        user_name = mr.group("name")
        gold_bind = mr.group("gold_bind")
        if user_name not in use_gold_bind_dict:
            use_gold_bind_dict[user_name] = 0

        use_gold = use_gold_bind_dict[user_name] + int(gold_bind)
        use_gold_bind_dict[user_name] = use_gold
        # print("%s use gold_bind %d" %(user_name, use_gold))

def analyse_use_all_gold(use_log):
    global use_gold_bind_dict;
    global use_gold_dict;

    p = re.compile(r"\[.*?\] MoneyGold \(Info\): \[Money::UseAllGold Succ\]\[user\[(?P<name>\S*) (?P<uid>\d*)\] .*? use_gold:(?P<gold>\d+) .*? use_gold_bind:(?P<gold_bind>\d+)")
    # p = re.compile(r"\[.*?\] MoneyGold \(Info\): \[Money::UseAllGold Succ\]\[user\[(?P<name>\S*) (?P<uid>\d*)\] .*? use_gold:(?P<gold>\d+) .*? use_gold_bind:(?P<gold_bind>\d+)")
    mr = p.match(use_log)
    if (None != mr) :
        #print(mr.span(), mr.group(), "user_name:", mr.group("name"), "uid:", mr.group("uid"), "gold_bind:", mr.group("gold_bind"), "use_gold:", mr.group("gold"))
        user_name = mr.group("name");
        gold_bind = mr.group("gold_bind")
        gold = mr.group("gold")
        
        if user_name not in use_gold_bind_dict:
            use_gold_bind_dict[user_name] = 0
        use_gold_bind = use_gold_bind_dict[user_name] + int(gold_bind)
        use_gold_bind_dict[user_name] = use_gold_bind

        if (user_name not in use_gold_dict):
            use_gold_dict[user_name] = 0
        use_gold = use_gold_dict[user_name] + int(gold)
        use_gold_dict[user_name] = use_gold

        
        # print("%s use gold_bind %d" %(user_name, use_gold))

        group_dict = mr.groupdict();
        for key, value in group_dict.items():
            print("group_dict key %s, value %s" %(key, value))
            print(mr.span(key))
    
print(os.getcwd())
work_dir = "D:\python\money_gold"
os.chdir(work_dir)
print(os.getcwd())
mr = re.compile("")

sensive_files = glob.glob('money_gold_2015_07*.txt')

for file in sensive_files :
    # print(file)
    fd = open(file, 'r')
    while True:
        log_str = fd.readline()
        # print(log_str)
        if len(log_str) <= 0: break
        analyse_use_all_gold(log_str)
        analyse_use_gold_bind(log_str)
        

for name, value in use_gold_bind_dict.items():
    if value > 0:
       print("%s total use gold_bind %s" %(name, value))

print("--------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------")
for name, value in use_gold_dict.items():
    if value > 0:
        print("%s total use gold %s" %(name, value))

        
    
    
