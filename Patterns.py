print("Pattern 1")
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(5):
        print("*", end="")
    print(end="\n")    



print("Pattern 2")
n = int(input("Enter the number of rows: "))
for i in range(n+1):
    for j in range(i):
        print("*", end="")
    print(end="\n")    


print("Pattern 3")
n = int(input("Enter the number of rows: "))
for i in range(n+1):
    for j in range(i):
        print(j+1, end="")
    print(end="\n")    


print("Pattern 4")
n = int(input("Enter the number of rows: "))
for i in range(n+1):
    for j in range(i):
        print(i, end="")
    print(end="\n")    

