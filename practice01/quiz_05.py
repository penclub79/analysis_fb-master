s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s = s.upper().replace(',', "").replace('.', "").splitlines()
# s = s[0].split()+s[1].split()

from collections import Counter
wordDict = Counter()

# s = s.split(' ')

s.sort()

for sentence in s: #한 문장씩
    for word in sentence.split(): #한 문장에 들어있는 한 단어씩
        wordDict[word] += 1


for word, freq in wordDict.most_common():
    print (word, freq)

