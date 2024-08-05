#Creating a function with 2 parameters
def add(x,y):
    return x+y
summ=add(2,3);
print(summ)

#While loop
a=0
while(a<5):
 a=a+1
 print("Hello")

#For in Loop over a list
print("List")
l=["Geeks", "For", "Geeks"]
for i in l:
    print(i)

#For in Loop over a turple
print("List")
l=("Geeks", "For", "Geeks")
for i in l:
    print(i)

#For in Loop over a String(Space between letters)
print("String")
s="Geeks"
for i in s:
    print(i)

#Index for sequence
list = ["Geeks", "For", "Geeks"]
for index in range(len(list)):
 print(list[index])

#Continue Statement 
for letter in 'geeksforgeeks':
    if letter=='e' or letter=='k':
        continue
    print ('Current letter:', letter)

