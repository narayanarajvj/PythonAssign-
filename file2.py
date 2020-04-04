# 5. Write a python program to find the longest word in a given file.
def max_len(w):
    return len(max(w, key=len))

f1 = open("text1.txt", "r")
words = f1.read().split()
m = max_len(words)
print([word for word in words if len(word) == m])
