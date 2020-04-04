# 4. Write a Python program to combine each line from first file with the corresponding line
# in second file
f1 = open("text1.txt", "r")
f2 = open("text2.txt", "r")
fout = open("out.txt", "w")
for l1, l2 in zip(f1, f2):
  fout.write(l1+l2)
fout.close()
fout = open("out.txt", "r")
l3 = fout.read()
print(l3)
f1.close()
f2.close()
fout.close()