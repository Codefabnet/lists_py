import sys
import os


multiline = '''
Now is the time
for all good men
to come to the aid of their country
'''

print(multiline)
print(multiline.title())
print(multiline.replace("men", "goats"))
print(len(multiline))

multiline += "                          "
print(len(multiline))
multiline = "          " + multiline
print(len(multiline))

print(multiline.strip())
print(len(multiline.strip()))
print(multiline.rstrip())
print(len(multiline.rstrip()))
print(multiline.lstrip())
print(len(multiline.lstrip()))
