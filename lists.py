print()
print()

print("A list of strings ")
print("-----------------------------------")
user_list = ['Dave', 'John', 'Sara']
print("user_list:", user_list)

print()
print()

print("A list of mixed types ")
print("-----------------------------")
data_list = ['Dave', 42, True]
print("data_list:", data_list)

print()
print()

print("An empty list ")
print("--------------")
empty_list = []
print("empty_list:", empty_list)

print()
print()

print("Check if item is in list ")
print("-----------------------------------------")
print("Is Dave in user_list?".ljust(35), "Dave" in user_list) #True
print("Is Dave in data_list?".ljust(35), "Dave" in data_list) #True
print("Is Dave in empty_list?".ljust(35), "Dave" in empty_list) #False

print()
print()

print("Print item at list index ")
print("--------------------------------------------------------")
print("First item in user_list, index '0'".ljust(45),
       user_list[0].rjust(10, "."))                 # First item - index '0'
print("Last item in user_list, index '-1'".ljust(45),
       user_list[-1].rjust(10, '.'))                # Last item  - index '-1'
print("Second to last item in user_list, index '-2'".ljust(45),
       user_list[-2].rjust(10, '.'))                # Second to last item  - index '-2'

print()
print()

print("Copy using assignment, '=', creates a new reference to a single list.")
print("---------------------------------------------------------------------")
user_list_copy = user_list
print("Copy user_list".ljust(23), user_list_copy)
user_list_copy.append('Steve')
print("Append to copy".ljust(23), user_list)
print("user_list updated through copied list:\n"
      "                       ", user_list)

print()
print()

print("----------------------------------------------------------")
print("For a slice specifier, the right index points just past\n"
      "the range sought, or the last item if not present.\n\n"
      "Using negative numbers, where x = number of items.\n"
      "The left index ranges from -x to -1, (first to last))\n"
      "The right index ranges from -(x-1) to no index given.\n\n"
      "[x:y] == from item at index x to item before index y\n"
      "[x:] == from item at index x to last item.\n"
      "[:y] == from first item to item before index y.\n"
      "[:] == full list, (first to last).\n")

print("A slice operation creates a new list object\n"
      "new_list = list[x:y], new_list may just be a print param.")
print("----------------------------------------------------------")
full_slice = user_list[:]

print("Slice of user_list, full slice: [:]\n"
      "                    ", full_slice)
print("Slice of user_list from second to last item: [-2:]\n"
      "                    ", full_slice[-2:])
print("Slice of user_list from first to second to last item: [-4:-1]\n"
      "                    ", full_slice[-4:-1])
full_slice[-1] = 'Stephen'
print("full slice modified:\n"
      "                    ", full_slice)
print("user_list unmodified:\n"
      "                    ", user_list)

print()
print()

print("Using a slice to change or clear existing list items.\n"
      "list[x:y] = modifying_list[x:y]")
print("----------------------------------------------------------")
print("user_list: ".ljust(25), user_list)
user_list[2:5] = ['Tom', 'Dick', 'Harry']
print("Changed user_list by slice: [2:5]\n"
       "                         ", user_list)
user_list[1:3] = []
print("Removed items by slice: [1:3] = []\n"
       "                         ", user_list)
user_list[:] = []
print("Clear user_list by slice: [:] = []\n"
       "                         ", user_list)
print("An empty list is logically false:\n"
       "                          user_list ==", bool(user_list))
user_list[:] = full_slice
print("Restore user_list by slice, using full_slice list:\n"
       "                         ", user_list)

print()
print()


print("Nesting lists.")
print("----------------------------------------------------------")
a = [1, 2, 3, 4]
b = [0, 1, 2, 3]
c = [a, b]

print("A list of lists, c:".ljust(35), c)
print("First list item in outer list c[0]:".ljust(36), c[0])
print("Second list item in outer list c[1]:".ljust(50), c[1])
print("First item in first list c[0][0]:".ljust(37), c[0][0])
print("First item in second list c[1][0]:".ljust(51), c[1][0])

print()

resp = input("Show list functions: 'Y' or 'N': ")

print()

if resp == 'Y' or resp == 'y':
    with open('list_funcs.txt', 'r') as f:
        print("List Functions")
        print("----------------------------------------------------------")
        print(f.read())
#        for line in f:   # This adds an extra line in output.
#            print(line)

print()

resp = input("Show list comprehension: 'Y' or 'N': ")

print()

if resp == 'Y' or resp == 'y':
    with open('list_comprehension.txt', 'r') as f:
        print("List Comprehension")
        print("----------------------------------------------------------")
        print(f.read())
