f = open(filename)
while True:
    char = f.read(1)
    if not char: break
    process(char)
f.close()