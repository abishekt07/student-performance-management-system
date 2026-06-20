students = {}
n = int (input("enter the number of students : "))
for i in range(n):
    name = input("Enter student name:")
    marks = int(input("Enter the Marks :"))
    students[name] = marks
file = open("students.txt", "w")
for name, marks in students.items():
    file.write(name + "," + str(marks) + "\n")
file.close()
file = open("students.txt", "r")
print("\nStudent Records")
for line in file:
    print(line.strip())
file.close()
average = sum(students.values()) / len(students)
print("Average Marks =", round(average, 2))
topper = max(students, key=students.get)

print("Topper =", topper)
print("Marks =", students[topper])
import matplotlib.pyplot as plt

names = list(students.keys())
marks = list(students.values())

plt.bar(names, marks)

plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
