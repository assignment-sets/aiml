import pandas as pd

#1
data = {
    'Student ID': [101, 102, 103],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 78, 92],
    'English': [90, 82, 85],
    'Physics': [88, 79, 84],
    'Chemistry': [91, 85, 87],
    'Biology': [78, 88, 80],
    'History': [85, 91, 79]
}

marksheet = pd.DataFrame(data)
print(marksheet)

#2
