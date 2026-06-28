# Write a python program to print a continuous number triangle

# 1) Generator Expression
n=5 
for i in range(1,n+1):
    print(" ".join(str(x) for x in range(1, i+1)))
    
    
# 2) Without Generator Expression
n = 5

for i in range(1, n + 1):
    temp = []

    for x in range(1, i + 1):
        temp.append(str(x))

    print(" ".join(temp))
    
    
# 3) Using a Lambda Function
n = 5

convert = lambda x: str(x)

for i in range(1, n + 1):
    print(" ".join(convert(x) for x in range(1, i + 1)))


# 4) map
n = 5

for i in range(1, n + 1):
    print(" ".join(map(lambda x: str(x), range(1, i + 1))))

#Output:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5



#----------------------------

#----------------------------
# print an inverted number traingle

# 1) Generator Expression
n=5 
for i in range(n, 0, -1):
    print(" ".join(str(x) for x in range(1, i+1)))

#Outpur:
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1


#----------------------------
#Centered pyramid of Numbers
#----------------------------
#Print a centered pyramid of numbers
n=5
for i in range(1, n+1):
    spaces = " "*(n-i)
    numbers = " ".join(str(x) for x in range(1, i+1))
    print(spaces+numbers)

#Output : 
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5

