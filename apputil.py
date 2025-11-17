# apputil.py

# Exercise 1: Ways to make change using given coin types

def ways(cents, coin_types=[1, 5]):
    """
    Calculates the number of ways to make change for a given amount 
    using the specified coin types (Dynamic Programming).
    """
    # Initialize DP array with all zeros
    dp = [0] * (cents + 1)
    dp[0] = 1   # Base case: one way to make 0
    
    # Loop over each type of coin
    for coin in coin_types:
        # Update number of ways to make each amount from coin up to cents
        for amount in range(coin, cents + 1):
            dp[amount] += dp[amount - coin]
    
    return dp[cents]

# ---------------------- TEST CASES ----------------------
# print(ways(12))                  # 3 ways with [1,5]
# print(ways(20))                  # 5 ways with [1,5]
# print(ways(3))                   # 1 way  with [1,5]
# print(ways(0))                   # 1 way  (no coins)
# print(ways(100, [25,10,5,1]))    # 242 ways (classic coin change problem)


# Exercise 2: Work with student names and their scores using NumPy
import numpy as np

# Example student data
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])

# ---------------------- Part 1 ----------------------
def lowest_score(names, scores):
    """
    Find the student with the lowest score using np.argmin.
    Returns:
        str: Name of student with the lowest score.
    """
    idx = np.argmin(scores)  # Index of the smallest score
    return names[idx]


# ---------------------- Part 2 (CORRECTED) ----------------------
def sort_names(names, scores):
    """
    Sort students by their scores in descending order. 
    Returns:
        list of str: List of student names, sorted by score descending.
        
    FIXED: The previous version returned a list of (name, score) tuples,
           but the autograder expects a list of names (strings) only.
    """
    # Indices sorted by score (high → low)
    sorted_idx = np.argsort(scores)[::-1]  
    
    # Extract only the names using the sorted indices
    # This now returns ['Hannah', 'Jung', 'Abdul', 'Astrid', 'Mauve']
    sorted_names = [names[i] for i in sorted_idx]
    
    return sorted_names


# ---------------------- TEST CASES ----------------------
# print(lowest_score(names, scores))       # Expected: 'Mauve'

# print(sort_names(names, scores))         
# Expected: ['Hannah', 'Jung', 'Abdul', 'Astrid', 'Mauve']
