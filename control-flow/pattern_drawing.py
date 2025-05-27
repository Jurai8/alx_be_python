
size = int(input("Enter the size of the pattern: "))

pattern = size

while pattern > 0:
    for y in range(size):
        print("*", end="")
    # add a space after each line
    print("")

    pattern -= 1