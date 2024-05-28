import sys
import os

print()

for entry in os.listdir("."):
    print(entry)

if len(sys.argv) > 1:
    test_str = sys.argv[1]
else:
    test_str = "test"

print(test_str)
print(type(test_str))
print(type(test_str) == str)
print(isinstance(test_str, str))