""" #reading from a text file
file_handler = open('E:\Data Classes\Class 1\Class2\File.txt','r')
print(file_handler.read())

#writing to a text file
file_handler = open('E:\Data Classes\Class 1\Class2\File.txt','w')
file_handler.write("This is a text file")


#updating a text file
file_handler = open('E:\Data Classes\Class 1\Class2\File.txt','a')
file_handler.write("Updating the text file") """

""" #Reading from  a File 
file_handler = open('E:\Data Classes\Class 1\Class2\File.txt','r')
print(file_handler.read())

#Writing In a File 
file_handler = open("E:\Data Classes\Class 1\Class2\File.txt","w")
file_handler.write("This is a text file")
print(file_handler)

#appending  a text file
file_handler = open("E:\Data Classes\Class 1\Class2\File.txt","a")
file_handler.write("Updating the text file") 
print(file_handler)



write a code for a python read write and append  """


""" # open file in read mode 
f = open("E:\Data Classes\Class 1\Class2\File.txt", "r") 

# read the content of the file 
content = f.read() 

# print the content 
print(content) 

# open file in append mode 
f = open("E:\Data Classes\Class 1\Class2\File.txt", "a") 

# write the content to the file 
f.write("I am adding additional content to this file") 

# close the file 
f.close() 

# open the file again in read mode 
f = open("E:\Data Classes\Class 1\Class2\File.txt", "r") 

# read the content of the file 
content = f.read() 

# print the content 
print(content) 

# close the file 
f.close() """


""" i = 1
while i <= 200:
    print(i)
    if i == 20:
        break
    i +=1


# Dictionary in Python

thisdict = {

    "brand":"Honda",
    "model":"City",
    "year":"2018"
}

thisdict1 = {

    "brand":"Suzuki",
    "model":"Cultus",
    "year":"2021"
}
thisdict2 = {

    "brand":"Toyota",
    "model":"Altis",
    "year":"2020"
}

concatDictionary ={
    "list1":thisdict,
    "list2":thisdict1,
    "list3":thisdict2
}

print(concatDictionary)
print(concatDictionary.keys()) """



arr = [3,5,2,0,1]
arr.sort()

print(arr)
