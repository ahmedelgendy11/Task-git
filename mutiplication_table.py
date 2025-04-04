num=int(input("Enter a number: "))
def mutiplication_table(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(f"{j} * {i} = {j*i}") 
mutiplication_table(num)

