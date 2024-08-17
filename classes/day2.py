# creating fataframe using pandas

import pandas as pd

student_data = {
    'Student ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Roll Number': [101, 102, 103, 104, 105]
}

student_df = pd.DataFrame(student_data)

student_df.set_index(['Student ID', 'Name'], inplace=True)

print(student_df)

print(student_df.reset_index())

print(student_df)


# ---------------------------------------------------------------------------------------------


# reading csv using pandas

import pandas as pd

# Provide the file path using a raw string literal
file_path = r'C:\Users\User\Desktop\hello\employees.csv'

# Read the CSV file into a pandas DataFrame
emp_df = pd.read_csv(file_path)

# Calculate yearly commission (20% of salary) and assign it to a new column
emp_df = emp_df.assign(yearly_commision=emp_df['salary'] * 0.2)

# Add a new column 'total_id' which is the concatenation of 'employ_id' and 'job_id'
emp_df = emp_df.assign(total_id=emp_df['employ_id'].astype(str) + '_' + emp_df['job_id'].astype(str))

# Display the updated DataFrame
print(emp_df)



# ---------------------------------------------------------------------------------------------



# removing header

emp_df_01 = pd.read_csv(file_path, header=None)

emp_df_01 = emp_df_01.iloc[1:]

print(emp_df)
print(emp_df_01)


# ---------------------------------------------------------------------------------------------


#droppin cols

emp_df.drop(columns=['manager_id'], inplace=True)

columns_to_drop = emp_df.columns[[0, 2, 4]]
duplicate_emp_ddf = emp_df.drop(columns=columns_to_drop, inplace=False)


# ---------------------------------------------------------------------------------------------

# using matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Create NumPy arrays
x = np.array([0, 6])  # Values from 0 to 6
y = np.array([0, 250])  # Values from 0 to 250

# Plotting
plt.figure(figsize=(8, 6))  # Optional: Adjust the figure size

plt.plot(x, y, label='Line Plot')  # Plot x vs y with a label
plt.xlabel('X-axis')  # Label for x-axis
plt.ylabel('Y-axis')  # Label for y-axis
plt.title('Plot of X and Y Values')  # Title of the plot
plt.legend()  # Show legend

plt.grid(True)  # Optional: Add gridlines

plt.show()  # Display the plot


# ---------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Generate numbers from 0 to 10
x = np.arange(0, 11)
# Calculate squares of these numbers
y = x**2

# Plotting
plt.figure(figsize=(8, 6))  # Optional: Adjust the figure size

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Square of Numbers')  # Plot x vs y with a label
plt.xlabel('Numbers')  # Label for x-axis
plt.ylabel('Squares')  # Label for y-axis
plt.title('Plot of Numbers vs Squares')  # Title of the plot
plt.legend()  # Show legend

plt.grid(True)  # Optional: Add gridlines

plt.show()  # Display the plot
