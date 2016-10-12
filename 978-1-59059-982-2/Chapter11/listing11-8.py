f = open(filename)
while True:
    line = f.readline()
    if not line: break
    process(line)
f.close()