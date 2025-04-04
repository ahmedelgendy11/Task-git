# Write a function find(string, char) that returns the number of times a character occurs in a string.
def find(string, char):
    z=0
    b=0
    for i in string:
        if i == char:
            print(f"the the location is {z}")
            b+=1
        z+=1      
    if b==0:
        print("The character is not present in the string")
    return (b+4)

string=input("Enter a string: ")
char=input("Enter a character: ")
find(string,char)