a = list(input().strip())
b = list(input().strip())

def check(a, b):
    # First quick check - if lengths are different, not anagrams
    if len(a) != len(b):
        return 0
        
    # Check both ways - a against b and b against a
    for l in set(a + b):  # using set to check each unique character once
        if a.count(l) != b.count(l):
            return 0
    return 1

print(check(a, b))

from collections import Counter

str1 = input().strip()
str2 = input().strip()

# Create character frequency dictionaries
counter1 = Counter(str1)
counter2 = Counter(str2)

# Compare the frequency dictionaries
print(1 if counter1 == counter2 else 0)

# Read two strings
str1 = input().strip()
str2 = input().strip()

# Sort both strings and compare
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)

# Print 1 if anagrams, 0 if not
print(1 if sorted_str1 == sorted_str2 else 0)