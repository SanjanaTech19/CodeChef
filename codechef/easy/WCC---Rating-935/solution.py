# cook your dish here
# Read the number of test cases
t = int(input())

for i in range(t):
    # Read the prize multiplier X
    X = int(input())
    
    # Read the match results string
    S = input()
    
    # Count occurrences using Python's built-in string method
    carlsen_wins = S.count('C')
    chef_wins = S.count('N')
    draws = S.count('D')
    
    # Calculate total points (Win = 2 points, Draw = 1 point)
    carlsen_points = carlsen_wins * 2 + draws
    chef_points = chef_wins * 2 + draws
    
    # Output the appropriate prize money
    if carlsen_points > chef_points:
        print(60 * X)
    elif carlsen_points == chef_points:
        print(55 * X)
    else:
        print(40 * X)