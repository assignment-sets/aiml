import numpy as np

# Creating two NumPy arrays
study_duration1 = np.array([1, 7, 3, 9, 4])
study_duration2 = np.array([4, 3, 8, 2, 1])

print("Array 1:", study_duration1)
print("Array 2:", study_duration2)

total_duration_manual = study_duration1 + study_duration2
print(total_duration_manual)

total_duration = np.add(study_duration1, study_duration2)
print("Addition:", total_duration)

subtraction_result = np.subtract(study_duration2, study_duration1)
print("Subtraction:", subtraction_result)

# Multiplying the arrays
multiplication_result = np.multiply(study_duration1, study_duration2)
print("Multiplication:", multiplication_result)

# Dividing the arrays
division_result = np.divide(study_duration2, study_duration1)
print("Division:", division_result)

exponential_result = np.exp(study_duration1)
print("Exponential of the array:", exponential_result)

mean_result = np.mean(study_duration1)
print("Mean of the array:", mean_result)

median_result = np.median(study_duration1)
print("Median of the array:", median_result)

reshaped_arr = study_duration1.reshape(3, 2) #2 is rows and 3 is cols
print("Reshaped array:", reshaped_arr)

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

file_path = r'C:\Users\User\Desktop\hello\\' #or just remove r and use forward slash
np.savetxt(file_path + 'data.csv', arr, fmt="%d")
np.savetxt(file_path + 'data.txt', arr, fmt="%d")
print(f"NumPy array has been successfully written to {file_path}")

import pandas as pd

st_dataset = {
    "key_1" : 1,
    "key_2" : 2
    }

series = pd.Series(st_dataset)

# print(series)

student_data = {
    'Name': ['John Doe', 'Jane Smith', 'David Johnson'],
    'Email': ['john.doe@example.com', 'jane.smith@example.com', 'david.johnson@example.com']
}

df = pd.DataFrame(student_data)
df['Roll Num'] = [101, 102, 103]

print("Student DataFrame:")
print(df)

num_rows = len(df)  
print(f"Number of rows in the DataFrame: {num_rows}")

row_count = 0

for _ in df.iterrows():
    row_count += 1

print(f"Number of rows in the DataFrame: {row_count}")
