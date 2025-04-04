
num = int(input("Enter the number of elements in the list: "))
list1 = []
def list(num):
   lis = []
   for i in range(1,num+1):
    indix= int(input("Enter a number: "))
    lis.append(indix)
   return lis

list1 = list(num)
print(list1)
print(sorted(list1))
print(sorted(list1,reverse=True))

