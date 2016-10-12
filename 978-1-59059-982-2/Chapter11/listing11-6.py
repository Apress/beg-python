f = open(filename)
char = f.read(1)
while char:
    process(char)
    char = f.read(1)
f.close()