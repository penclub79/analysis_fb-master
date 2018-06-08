s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s = s.upper().replace(',', "").replace('.', "").replace('\n', "")


s = list(s)
s = ''.join(s)
s = s.split(' ')
s = list(set(s))

print(s)