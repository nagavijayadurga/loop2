l=[10,20,30,40]
for i in l:
    print(i , i*i)


text="python"
index=0
for ch in text:
   print(index,ch)
   index+=1


numbers=[100,140,35,45,80,98]
total=0
for i in numbers:
    if i%2==0:
        total+=i
print("sum of even numbers:",total)


student = {
    "Name": "John",
    "Age": 21,
    "Course": "Python"
}

for key in student:
     print(key, ":", student[key])


numbers = []
for i in range(1, 101):
    numbers.append(i)
for i in numbers:
    if i % 3 == 0 or i % 5 == 0:
        print(i)