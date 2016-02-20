"""This is a version from Charles Severance to assignment 9.4
for dictionary chapter"""

name = raw_input("Enter file: ")
handle = open(name, "r")
text =handle.read()
words = text.split()

counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1
    
bigCount = None
bigWord = None
for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count
        
print bigCount, bigCount