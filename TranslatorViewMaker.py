#imports
import configparser
from io import StringIO
#preperations
parser = configparser.RawConfigParser(delimiters=('='),default_section=(' '))
parser.optionxform = lambda option: option
string = StringIO()
print("Before running this program make sure to run a duplicate checker on your .ini using Ksempac's Translation Toolkit")
print("Also make sure that the ini file is inside the same folder as the program because I'm lazy (it will be fixed)")
source = input("Please enter your .ini file name here, preferebly en.ini: ")
theme = input("Please type you theme name (for your reference, you can even leave it blank):")
print('Select the type of view:')
print("1.Show the line's section and value in the file")
print("2.show the line's line number in the file")
choice = input()
parser.read(source, encoding="utf-8")
#where the magic happens
for parser.sections in parser:
      section = parser.sections
      print('[',section,']',sep='')
      for key in parser[section]:
          if choice == '1':
             line = theme, section, key
             parser.set(section, key, line)
             print(key, '=', line)
          else:
             line_num = 0
             line_source = open(source, "r", encoding="utf-8")
             for number, line in enumerate(line_source):
                   if key in line:
                       line_num = number + 1
                       break
             line = theme, line_num
             parser.set(section, key, line)
             print(key, '=', line)

with open('tr.ini', "w", encoding="utf-8") as target:
    parser.write(target)
input("Done! Your tr.ini is ready to be used, press ENTER to exit")