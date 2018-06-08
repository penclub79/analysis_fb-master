str = "Life is too short, You need Python"

str = str.lower()
str = str.replace(" ","")
str = str.replace(",","")

lst = list(str)
print("lst : ", lst)
chars = set(lst)
print("chars: ", chars)
lst = list(chars)

lst.sort()
print("lst:", lst)
print("length of lst:", len(lst))


