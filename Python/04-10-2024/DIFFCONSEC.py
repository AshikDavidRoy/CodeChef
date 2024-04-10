def min_operations(binary_string):
    count = 0
    for i in range(1, len(binary_string)):
        if binary_string[i] == binary_string[i - 1]:
            count += 1
    return count

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the length of the binary string and the binary string itself
    N = int(input())
    binary_string = input().strip()
    
    # Calculate and print the minimum number of operations needed
    min_ops = min_operations(binary_string)
    print(min_ops)
