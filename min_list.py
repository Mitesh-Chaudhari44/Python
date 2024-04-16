# Given list
l = [100, 2, 300, 4, 10, 55]

# Initialize 'a' to a large number (assuming all elements are positive)
a = float('inf')  # Starting with infinity as the initial minimum

# Iterate through the list
for i in range(len(l)):
    # Check if the current element is smaller than 'a'
    if l[i] < a:
        # Update 'a' to the current element if it's smaller
        a = l[i]

# 'a' now holds the minimum element of the list
print("Minimum element of the list is:", a)
