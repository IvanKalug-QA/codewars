# Task:
# This kata requires you to write an object that receives a file path and does operations on it. NOTE FOR PYTHON USERS: You cannot use modules os.path, glob, and re
# The purpose of this kata is to use string parsing, so you're not supposed to import external libraries. I could only enforce this in python.
# Testing:
# Python:
#
# >>> master = FileMaster('/Users/person1/Pictures/house.png')
# >>> master.extension()
# 'png'
# >>> master.filename()
# 'house'
# >>> master.dirpath()
# '/Users/person1/Pictures/'
# Ruby:
#
# master = FileMaster.new('/Users/person1/Pictures/house.png')
# master.extension
# #--> png
# master.filename
# #--> house
# master.dirpath
# #--> /Users/person1/Pictures/
# C#:
#
# FileMaster FM = new FileMaster("/Users/person1/Pictures/house.png");
# FM.extension(); // output: "png"
# FM.filename(); // output: "house"
# FM.dirpath(); // output: "/Users/person1/Pictures/"
# JavaScript:
#
# const fm = new FileMaster('/Users/person1/Pictures/house.png');
# fm.extension(); // output: 'png'
# fm.filename(); // output: 'house'
# fm.dirpath(); // output: '/Users/person1/Pictures/'
# TypeScript:
#
# const fm = new FileMaster('/Users/person1/Pictures/house.png');
# fm.extension(); // output: 'png'
# fm.filename(); // output: 'house'
# fm.dirpath(); // output: '/Users/person1/Pictures/'
# PHP:
#
# $fm = new FileMaster('/Users/person1/Pictures/house.png');
# $fm.extension(); // 'png'
# $fm.filename(); // 'house'
# $fm.dirpath(); // '/Users/person1/Pictures'
# Notes:
# I have other kata that need to be tested. You may find them here and here
# Please post any questions or suggestion in the discourse section. Thank you!
# Thank to all users who contributed to this kata! I appreciate your input!

class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath
    def extension(self):
        return self.filepath.split('/')[-1].split('.')[-1]
    def filename(self):
        return self.filepath.split('/')[-1].split('.')[0]
    def dirpath(self):
        return '/'.join(self.filepath.split('/')[0:-1]) + '/'