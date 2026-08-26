nm=input('Enter student name : ')
ct=input('Enter City : ')
co=input('Enter Course : ')

file=open("students.csv","a")
file.write(f"{nm},{ct},{co}\n")
print('csv file write successful')
file.close()