# loop 
"""for i in range(0,10):
     i = i + 1
     print(i) """

a = 1
b = 1 


# If ELSE Code 
"""if(a == b):
    print("True")   
else:
    print("False") """

# Condition Match Code 
"""if (a==1 and b == 1):
    print("Match")
else:
    print("Unmatch")"""

#Element is Present 
""" a = ['a','b','bb','c']

if('bb' in a):
    print("Element is Present")
else:
    print("Element is not Present") """


# This Progra for replacing values in list
"""thislist = ["Banana","Apple", "kiwi","Orange"]

thislist[1:2] = ["Watermelon","Jamun"]

print(thislist) """

# Code for append the matching Element in the list.
""" fruits =["Banana","Apple","Melon","Water Melon"]
newlist =[]

for x in fruits:
    print(x)

    if "a" or 'A' in x:
        newlist.append(x)



print(newlist) """

#Sorting Element from list 
""" a = [4,2,10,5,6,1]

a.sort()
print(a) """

# Reversing a list items
""" b =[1,2,3,4,5]
b.reverse()
print(b) """

# Customized Function 
""" def func(n):
    return abs(n - 50)


newlist =[100,50,65,82,23]
newlist.sort(key = func)
print(newlist)
 """

#list Reverse Function
""" k = ["apple","ball","coconut"]
k.reverse()
print(k) """

# JOINING LIST WITH DIFFERENT TYPES

#First Method with the + sign 
""" list1 = ['a','b','c']
list2 = [1,2,3,4,5]

list3 = list1 + list2
print(list3)

# Second Method using append function
a = ['a','b','c']
b = [1,2,3,4,5]

for d in b:
    a.append(d)

print(a)

#using extend to join list 
c = ['a','b','c']
d = [1,2,3,4,5]
c.extend(d)
print(c) """

# Tuple Example
""" fruits = ("Apple","Banana","Cherry","strawberry","Raspberry")
(green,yellow,*red) = fruits

print(green)
print(yellow)
print(*red) """


# Assigning Values To the Certain Group 
""" fruits = ("Apple","guava","Mango","pineapple","Raspberry")
(green,*Trophic,red) = fruits

print(green)
print(*Trophic)
print(red) """


# Updating tuple Method
""" listn = ("Jamshed","Ali","sameer")
y = list(listn)
y[1] = "Noman"
listn = tuple(y)

print(listn)
 """

 




 




