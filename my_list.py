
# create an empty list called my list

my_list = []

# Append the elements :10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


#Insert the value 15 at the second posotion
my_list.insert(1, 15)

# Extend my-list with another list[50, 60, 70]

my_list.extend([50, 60, 70])


# Step 5: Remove the last element from my_list
my_list.pop()


# Step 6: Sort my_list in ascending order

my_list.sort()


# Step 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)

print("index of 30:", index_of_30)


# Print the final list for reference
print("Final list", my_list)
