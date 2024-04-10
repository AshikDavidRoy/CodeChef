# Function to check if a character is a vowel
def is_vowel(ch):
    return ch in ['a', 'e', 'i', 'o', 'u']

# Function to determine if Chef is happy or sad
def chef_happy_string(s):
    n = len(s)
    for i in range(n - 2):
        # Check if the substring of length greater than 2 consists only of vowels
        if is_vowel(s[i]) and is_vowel(s[i+1]) and is_vowel(s[i+2]):
            return "HAPPY"
    # If no such substring exists, Chef is sad
    return "SAD"

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input string
    S = input().strip()
    
    # Determine if Chef is happy or sad and print the result
    print(chef_happy_string(S))
