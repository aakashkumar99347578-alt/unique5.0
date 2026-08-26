import numpy as np
import pandas as pd

course  = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\courses.csv')
nov = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\reg-month1.csv')
dec  = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\reg-month2.csv')
students = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\students.csv')
matches = pd.read_csv(r'unique5.0/python_library/matches.csv')
delivery = pd.read_csv(r'C:\Users\aakas\OneDrive\Desktop\uniques 5.0\unique5.0\python_library\deliveries.csv')

print("----------------------------------------dec data frame----------------------------------")
print(dec)

print("------------------------------------------nov data frame------------------------------------")
print(nov)

print("-------------------------------------concate of two data frame-----------------------------------")
regs = pd.concat([nov,dec],ignore_index=True)
print(regs)

print("------------------------------multi indexing---------------------------------------")
multi = pd.concat([nov,dec],keys=['Nov','Dec'])
print(multi)
print(multi.loc[('Dec',4)])

# inner join

print("-------------------------------------------inner join ---------------------------------------")
print(students.merge(regs,how='inner',on='student_id'))

# left join

print("---------------------------------left join----------------------------------")
print(course.merge(regs,how='left',on='course_id'))

# right join

print("-------------------------------right join-----------------------------------")
temp_df = pd.DataFrame({
    'student_id':[26,27,28],
    'name':['Nitish','Ankit','Rahul'],
    'partner':[28,26,17]
})

students = pd.concat([students,temp_df],ignore_index=True)
print(students.tail())
print(students.merge(regs,how='right',on='student_id'))

# outer join -> in outer join me dono data frame me ke sare data liya jata hai ho ya n ho.

print("----------------------outer join----------------------------------")
print(students.merge(regs,how='outer',on='student_id').tail(10))

# find total revenue genrated ->

print("-------------------------------------------find total revenue genrated------------------------------")
print(course.merge(regs,how='inner',on='course_id')['price'].sum())

# 2. find month by month revenue

print("-----------------------------find month by month revenue------------------------------")
temp_df = pd.concat([nov,dec],keys=['Nov','Dec']).reset_index()
print(temp_df.merge(course,on='course_id').groupby('level_0')['price'].sum())

# 3. Print the registration table
# cols -> name -> course -> price

print("----------------------print the registration table---------------------------")
print(regs.merge(students,how='right',on='student_id').merge(course,on='course_id')[['name','course_name','price']])

# 5. find students who enrolled in both the months

print("---------------------------------------find students who enrolled in both the months-----------------------------------")
common_student = np.intersect1d(nov['student_id'],dec['student_id'])
print(students[students['student_id'].isin(common_student)])

# 6. find course that got no enrollment
# courses['course_id']
# regs['course_id']

print("-----------------------------------find course that got no enrollment------------------------------------------")
course_id_list = np.setdiff1d(course['course_id'],regs['course_id'])
print(course[course['course_id'].isin(course_id_list)])

# 7. find students who did not enroll into any courses

print("-----------------find students who did not enroll into any courses--------------------------")
student_id_list = np.setdiff1d(students['student_id'],regs['student_id'])
print(students[students['student_id'].isin(student_id_list)].shape[0])

# 8. Print student name -> partner name for all enrolled students
# self join

print("--------------------------------self join------------------------------------------")
print(students.merge(students,how='inner',left_on='partner',right_on='student_id')[['name_x','name_y']])

# 9. find top 3 students who did most number enrollments

print("-------------------------------find top 3 students who did most number enrollments----------------------------------")
print(regs.merge(students,on='student_id').groupby(['student_id','name'])['name'].count().sort_values(ascending=False).head(3))

# 10. find top 3 students who spent most amount of money on courses

print("------------------------find top 3 students who spent most amount of money on courses-------------------------------")
print(regs.merge(students,on='student_id').merge(course,on='course_id').groupby('name')['price'].sum().sort_values(ascending=False).head(3))

# Alternate syntax for merge

print("---------------------Alternate syntax for merge------------------------------")
print(pd.merge(students,regs,how='inner',on='student_id'))

# IPL Problems

print("---------------------------ipl data frame for ipl problems-----------------------------")
print(matches)
print(delivery)

# find top 3 studiums with highest sixes/match ratio

print("------------------find top 3 studiums with highest sixex/match ratio----------------------------------")
temp_df = delivery.merge(matches,left_on='match_id',right_on='id')
number_six = temp_df[temp_df['batsman_runs']==6].groupby('venue')['venue'].count()
matches_no = matches.groupby('venue')['venue'].count()
print((number_six/matches_no).sort_values(ascending=False).head(3))

# find orange cap holder of all the seasons

print("-----------------------find orange cap holder of all the seasons-----------------------------------------")
print(temp_df.groupby(['season','batsman'])['batsman_runs'].sum().reset_index().sort_values('batsman_runs',ascending=False).drop_duplicates(subset='season',keep='first').sort_values('season',ascending=False))

