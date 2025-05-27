
size = int(input("Enter the size of the pattern: "))

# iterate size number of times
for x in range(size):
    # print "*" size number of times
    for y in range(size):
        print("*", end="")
    # add a space after each line
    print("")