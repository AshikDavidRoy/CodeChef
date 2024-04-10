def encode_dna_sequence(N, S):
    encoded_sequence = ''
    for i in range(0, N, 2):
        pair = S[i:i+2]
        if pair == '00':
            encoded_sequence += 'A'
        elif pair == '01':
            encoded_sequence += 'T'
        elif pair == '10':
            encoded_sequence += 'C'
        elif pair == '11':
            encoded_sequence += 'G'
    return encoded_sequence

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the length of the sequence and the binary string
    N = int(input())
    S = input().strip()
    
    # Encode the DNA sequence and print the result
    encoded_sequence = encode_dna_sequence(N, S)
    print(encoded_sequence)
