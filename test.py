import sys
import os

multiline = '''
Now is the time
for all good men
to come to the aid of their country
'''

print()

for entry in os.listdir("."):
    print(entry)

if len(sys.argv) > 1:
    test_str = sys.argv[1]
else:
    test_str = "abcdefghijklmnopqrstuvwxyz"

print(test_str)
print(type(test_str))
print(type(test_str) == str)
print(isinstance(test_str, str))


print(multiline)
print(multiline.title())
print(multiline.replace("men", "goats"))
print(multiline)
print(len(multiline))

multiline += "                          "
print(len(multiline))
multiline = "          " + multiline
print(multiline)
print(len(multiline))

print(multiline.strip())
print(len(multiline.strip()))
print(multiline.rstrip())
print(len(multiline.rstrip()))
print(multiline.lstrip())
print(len(multiline.lstrip()))


print(test_str.center(20))

print(test_str[0])
print(test_str[-1])
print(test_str[0:10])
print(test_str[10:20])
print(test_str[20:])

print(test_str.find("d"))
print(test_str.find("j"))