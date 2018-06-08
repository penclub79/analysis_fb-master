s = """We encourage everyone to contribute to Python. 
If you still have questions after reviewing the material
in this guide, then the Python Mentors 
group is available to help guide new contributors through the process."""

#데이터 정제
s = s.replace(",", "").replace(".","").replace("\n","").upper()
# print(s)

summary = {}
splits = s.split(" ")
print(splits)

for split in splits:
    if split in summary.keys():
        summary[split] += 1
    else:
        summary[split] = 1

for key, value in summary.items():
    print("{} : {}".format(key,value))

