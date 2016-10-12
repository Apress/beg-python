f = open(filename)
for char in f.read():
    process(char)
f.close()