def convert_to_title_case(Strings):
    words = Strings.split()
    result = []
    for word in words:
        if word.isupper():
            result.append(word)
        else:
            result.append(word.capitalize())
    return ' '.join(result)

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the input string
    S = input().strip()
    
    # Convert the string to title case and print the result
    title_case_string = convert_to_title_case(S)
    print(title_case_string)
