def print_every(i, nums):
    counter = ""
    for char in nums:
        if char % i == 0:
            char = str(char)
            counter = counter + char
    return print (counter)
print_every(3, [4, 7, 2, 10, 1, 0, 9, 6])
# should print 4, then print 10, then print 9