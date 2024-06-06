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

print("A slice operation creates a new list object")
print("----------------------------------------------------------") 
full_slice = user_list[:]

print("Slice of user_list, full slice:\n"
      "                    ", full_slice)
print("Slice of user_list from second to last item:\n"
      "                    ", full_slice[-2:])
full_slice[-1] = 'Stephen'
print("full slice modified:\n"
      "                    ", full_slice)
print("user_list unmodified:\n"
      "                    ", user_list)

print()
print()

print("Using a slice to change or clear list items.")
print("----------------------------------------------------------") 
print("user_list: ".ljust(25), user_list)
user_list[2:5] = ['Tom', 'Dick', 'Harry']
print("Changed user_list by slice:\n"
       "                         ", user_list)
user_list[1:3] = []
print("Removed items by slice:\n"
       "                         ", user_list)
user_list[:] = []
print("Clear lsit by slice:\n"
       "                         ", user_list)
user_list[:] = full_slice
print("Restore user_list by slice, using full_slice list:\n"
       "                         ", user_list)

print()
print()

