inputset = {1, 2, 3}

elements = list(inputset)
n = len(elements)

total_subsets = 1 << n  

print("All subsets:")
for i in range(total_subsets):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(elements[j])
    print(subset)
