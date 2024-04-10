def check_guess(hidden, guess):
    result = ''
    for i in range(len(hidden)):
        if hidden[i] == guess[i]:
            result += 'G'
        else:
            result += 'B'
    return result

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the hidden word and the guess word
    hidden = input().strip()
    guess = input().strip()
    
    # Check the guess and print the result
    result = check_guess(hidden, guess)
    print(result)
