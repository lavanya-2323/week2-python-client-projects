# Week-2 Client Project
# Data Cleaning Script using Python

print("===== Data Cleaning Script =====")

# Sample raw data with duplicates and invalid values
raw_data = [10, 20, 30, 20, 40, 50, 10, 60, -5, 30, 70, -10]

print("\nRaw Data:", raw_data)

# Step 1: Remove negative values
filtered_data = [x for x in raw_data if x >= 0]

# Step 2: Remove duplicates
cleaned_data = list(set(filtered_data))

# Step 3: Sort the cleaned data
cleaned_data.sort()

# Step 4: Data transformation (square of each value)
squared_data = [x**2 for x in cleaned_data]

# Output
print("\nFiltered Data (no negatives):", filtered_data)
print("Cleaned Data (no duplicates):", cleaned_data)
print("Transformed Data (squares):", squared_data)
