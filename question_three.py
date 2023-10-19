# i)
students_marks=[78,83,90,88,75]
# creating a variable with the intial value of the sum as 0
sum=0
# looping through the list
for x in students_marks:
# adding all the values inthe list
    sum+=x
print(f'The sum of the items in the student marks list  is {sum}')

# ii)
# outputing the first and last marks using their indexes
print(f'First mark is {students_marks[0]} and last mark is {students_marks[-1]}')

# iii)
# adding a value 96 to a list of marks
students_marks.append(96)
print(f'96 has been add to list {students_marks}')

# Updating value 78 to 87 using index
students_marks[0] = 87
print(f'Updated list = {students_marks}')
