string = input("Enter a string: ")
def count_vowels(a):
    q="a,e,i,o,u"
    z=0
    for i in a:
        if i in q:
            z+=1
    return z
print(count_vowels(f"{string}"))