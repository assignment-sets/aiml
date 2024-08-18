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
marksheet['Total'] = marksheet[['Math', 'English', 'Physics', 'Chemistry', 'Biology', 'History']].sum(axis=1)
marksheet['Percentage'] = marksheet['Total'] / 6
top_student = marksheet.loc[marksheet['Percentage'].idxmax()]
print(top_student) 

#3
min_marks = marksheet[['Math', 'English', 'Physics', 'Chemistry', 'Biology', 'History']].min()
lowest_count = (marksheet[['Math', 'English', 'Physics', 'Chemistry', 'Biology', 'History']] == min_marks).sum(axis=1)
result = marksheet[lowest_count > 2]
print(result[['Student ID', 'Name']])

#4
loc = r'C:\marksheet.csv'
marksheet.to_csv(loc, index=False)

#5
for _, row in marksheet.iterrows():
    print(row['Name'])
    
#6
for row in marksheet.itertuples(index=True):
    print(row.Name)
    
#7
high_math_scores = marksheet[marksheet['Math'] > 80]
print(high_math_scores[['Name']])

#8
second_row = marksheet.iloc[1]
print(second_row)
value = marksheet.iloc[1, 2]
print(value)

#10
marksheet = marksheet[marksheet['Math'] >= 80]
print(marksheet)