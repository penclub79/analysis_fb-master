lst = [1, 3.14, 'python', 7, 89.1, 3]

lst_cleaned = [] #필터링 된것을 담아오자

for item in lst:
    # if isinstance(item, int) or isinstance(item, float):
    if isinstance(item, (int, float)):
        lst_cleaned.append(item)

print(lst_cleaned)