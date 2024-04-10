def calculate_prize_money(X, results):
    carlsen_wins = results.count('C')
    chef_wins = results.count('N')
    draws = results.count('D')
    
    carlsen_points = 2 * carlsen_wins + draws
    chef_points = 2 * chef_wins + draws
    
    if carlsen_points > chef_points:
        return 60 * X
    elif carlsen_points < chef_points:
        return 40 * X
    else:
        return 55 * X

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read X and match results
    X = int(input())
    results = input().strip()
    
    # Calculate and print the prize money for Carlsen
    prize_money = calculate_prize_money(X, results)
    print(prize_money)
