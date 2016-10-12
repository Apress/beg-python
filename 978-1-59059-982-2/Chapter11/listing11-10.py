f = open(filename)
for line in f.readlines():
    process(line)
f.close()