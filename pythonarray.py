#Defining and Declaring an array
arr = [10,20,30,40,50]

print(arr)

# Accessing Array Elements
print (arr[0])
print(arr[1])
print(arr[3])
print(arr[-1]) #Negative indexing (replaces the last value of the array)
print(arr[-2]) #Negative indexing (replaces the second last value of the array)

brands=["Coke","Sprite","Softa","Toyota"]
print(brands)

#finding the length of brands
num_of_brands=len(brands)
print(num_of_brands)

#adding elements to brands
brands.append("Mercedes")
print(brands)
num_of_brands=len(brands)
print(num_of_brands)

#deleting elements to brands

colors = ["red","green","marroon","green","blue","indigo","violet","orange"]
num_of_colors=len(colors)
print(colors)
print(num_of_colors)

del colors[6]
print(colors)
num_of_colors=len(colors)
print(num_of_colors)

colors.remove("blue")
print(colors)
num_of_colors=len(colors)
print(num_of_colors)

colors.pop(3)
print(colors)

#Modifying elements using index
marangi = ["Oranges","Bananas","Apples","Straeberries"]
print(marangi)

marangi[1]= "Yellow"
print(marangi)

marangi[-1]= "Quavas"
print(marangi)

# Concantenation
concat = [1,2,3]
print(concat)

concat = concat + [4,5,6]
print(concat)

# Repeating element in an array
repeat = ["a"]
print((repeat))
repeat = repeat * 5
print((repeat))

# Slicing an array
fruits = ["Oranges","Bananas","Apples","Straeberries","Lemon", "Limes"]
print(fruits)
print(fruits[1:4]) # print data start index 1 excluding idex 4
print(fruits[ :3]) # print data start index missing so default 0 with index 3 been exclusive
print(fruits[-4: ]) # print data last 4 as the last index is missing
print(fruits[-3:-1 ]) # exclusive of the last item

# Multidimensional Array
mutl = [[1,2], [3,4],[5,6],[7,8]]
print((mutl))
print(mutl[0])
print(mutl[3])
print(mutl[2][1]) #means index 2 of the main array[5,6] and the value of index 1 of the inner array
print(mutl[3][0])