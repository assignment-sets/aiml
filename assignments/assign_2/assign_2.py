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

#11
new_row = pd.DataFrame({
    'Student ID': [104],
    'Name': ['David'],
    'Math': [88],
    'English': [91]
})
position = 1
df_before = marksheet.iloc[:position, :]
df_after = marksheet.iloc[position:, :]
marksheet = pd.concat([df_before, new_row, df_after], ignore_index=True)
print(marksheet)

#12
marksheet['Total'] = 0
for index, row in marksheet.iterrows():
    marksheet.at[index, 'Total'] = row['Math'] + row['English']

print(marksheet)

#13
column_names = marksheet.columns

print(column_names)

#14
marksheet = marksheet.rename(columns={'Student ID': 'ID', 'Math': 'Maths'})
print(marksheet)

#15
df['Full Name'] = df['First Name'] + ' ' + df['Last Name']
print(df)

#16
unique_names = marksheet['Name'].unique()
print(unique_names)

#18
array = np.array([10, 20, 30, 40, 50])
series = pd.Series(array)
print(series)

#19
data = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
series = pd.Series(data)
print(series)

#21
series = pd.Series(np.arange(5))
print(series)

#22
data = {'a': 10, 'b': 20, 'c': 30}
series = pd.Series(data)
print(series['a'])
# o/p : 10