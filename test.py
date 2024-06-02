import sys
import os

print()

if len(sys.argv) > 1:
    test_str = sys.argv[1]
else:
    test_str = "abcdefghijklmnopqrstuvwxyz"

print(test_str)
print(len(test_str))
print(type(test_str))
print(type(test_str) == str)
print(isinstance(test_str, str))


print(test_str.center(50))

print(test_str[0])
print(test_str[-1])
print(test_str[0:10])
print(test_str[10:20])
print(test_str[20:])

print(test_str.find("d"))
print(test_str.find("j"))
for idx in range(len(test_str)):
    print(f"this is test_str: {test_str[idx:idx+1]}")