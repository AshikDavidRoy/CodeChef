# Function to add one to a large number represented as a string
def add_one_to_number(number_str):
    # Convert the string to a list of digits
    digits = list(map(int, number_str))
    
    # Start from the rightmost digit
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        # Add the carry to the current digit
        new_digit = digits[i] + carry
        
        # Update the current digit and carry
        digits[i] = new_digit % 10
        carry = new_digit // 10
        
        # If there's no carry, we can stop
        if carry == 0:
            break
    
    # If there's a carry after processing all digits, insert a new digit at the beginning
    if carry:
        digits.insert(0, carry)
    
    # Convert the list of digits back to a string and return
    return ''.join(map(str, digits))


# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input number as a string
    N = input().strip()
    
    # Add one to the number and print the result
    incremented_number = add_one_to_number(N)
    print(incremented_number)
