f=open("./python/data.txt","r")

lines=0
words=0
chars=0

for line in f:
    line=line[:-1]
    lines+=1
    charsinline=len(line)
    chars+=charsinline
    w=len(line.split())
    words+=w



    for ch in line:
        if ch.isalpha():
            pass
        elif ch.isdigit():
            pass

print(lines,words,chars)

f.close()