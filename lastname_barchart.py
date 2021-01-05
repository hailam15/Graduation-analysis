# read file
with open("clean_data.csv", encoding="utf8") as file:
	data = file.read().split("\n")

header = data[0]
students = data[1:]

total_student = len(students)

# split header
header = header.split(",")
subjects = header[5:]

# split each student in list
for i in range(len(students)):
	students[i] = students[i].split(",")

# remove last student (empty student)
students.pop()

name = [] # list of last names
name_count = [] # number of iterations

for s in students:
	s_name = s[1].split(" ")
	lastname = s_name[0]
	if lastname not in name:
		name.append(lastname)
		name_count.append(0)
		name_count[name.index(lastname)] += 1
	else:
		name_count[name.index(lastname)] += 1

# print(name)
# print(name_count)

counted_max_num = [] # numbrr of iterations from max to min
sort_index = [] # list of postions after sorted

# Initialize counted_max_num, list of max iterations
for i in range(len(name)):
	max_number = 0
	for j in range(len(name)):
		if name_count[j] > max_number and name_count[j] not in counted_max_num:
			max_number = name_count[j]
	counted_max_num.append(max_number)

# Initialize sort_index, position by finding the postion of maximum numbers from counted_max_num
for max_num in counted_max_num:
	for i in range(len(name)):
		if name_count[i] == max_num and i not in sort_index:
			sort_index.append(i)

name_sorted = [] # Sorted list
name_count_sorted = [] # List of sorted iterations of last names 

# Use sort_index to sort last names and iterations
for index in sort_index:
	name_sorted.append(name[index])
	name_count_sorted.append(name_count[index])

# print(name_sorted)
# print(name_count_sorted)

# Draw barchart
# https://matplotlib.org/3.1.0/gallery/ticks_and_spines/custom_ticker1.html#sphx-glr-gallery-ticks-and-spines-custom-ticker1-py
import matplotlib.pyplot as plt
import numpy as np

num = 20 

x = np.arange(num)
y = np.arange(num)

fig, axis = plt.subplots()
plt.bar(x, name_count_sorted[0:num])

# label for column x
plt.xticks(x, name_sorted[0:num])

axis.set_ylabel('Number of students')

rects = axis.patches

# Make some labels.
# https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart
labels = name_count_sorted[0:num]
for rect, label in zip(rects, labels):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha='center', va='bottom')

plt.title(str(num) + ' most popular last names in exams')

plt.show()