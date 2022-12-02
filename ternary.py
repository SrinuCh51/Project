import time
a=int(input("Enter the value of a:")) 
b=int(input("Enter the value of b:")) 
c=int(input("Enter the value of c:")) 
d=int(input("Enter the value of d:")) 
max=a if a>b and a>c and a>d else b if b>c and b>d else c if c>d else d
print()
print("The max value is:")
print()
print(max)
print()
time.sleep(2)
print("End of an application")