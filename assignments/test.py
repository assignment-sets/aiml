import pandas as pd

# Define data and create DataFrame
data = {
    'Student ID': [101, 102, 103],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 78, 92],
    'English': [90, 82, 85]
}

marksheet = pd.DataFrame(data)

# Define the new row to insert
new_row = pd.DataFrame({
    'Student ID': [104],
    'Name': ['David'],
    'Math': [88],
    'English': [91]
})

# Specify the position where the new row will be inserted (e.g., position 1)
position = 1

# Split the DataFrame into two parts: before and after the insertion point
df_before = marksheet.iloc[:position]
df_after = marksheet.iloc[position:]

# Concatenate the two parts with the new row in between
result = pd.concat([df_before, new_row, df_after], ignore_index=True)

print(result)
