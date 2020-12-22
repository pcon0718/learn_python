dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print()
for dimension in dimensions:
    print(dimension)

print("\nOriginal Dimensions:")
for dimension in dimensions:
    print(dimension)

# Write over the current tuple
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)