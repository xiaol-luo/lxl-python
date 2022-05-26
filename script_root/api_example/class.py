#!/usr/bin/python
#class.py

import pdb

class Person:
    def __init__(self, name):   
        print("init person")
        self.name = name

    def __del__(self):
        print("%s says bye." % self.name)

    def sayHi(self):
        print("hello. my name is %s" %self.name)

class Student(Person):
    def __init__(self, name, school_name):
        print("init student")
        Person.__init__(self, name)
        self.school_name = school_name

    def sayHi(self):
        print("hello I am a student, name is %s, study in %s" %(self.name, self.school_name))


p = Person('xiaol_luo')
p.sayHi()

s = Student("xiaol_luo", "xxxxx");
s.sayHi()
