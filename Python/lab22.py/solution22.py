def save(roll,name,marks):
    f=open("studentdata.txt","a")
    t=f"\n{roll} {name} {marks}"
    f.write(t)
    f.close()

def calcaverage():
    f=open("studentsdata.txt","r")
    data=[]
    for line in f:
        line=line.strip()
        t=line.split()
        roll=int(t[0])
        name=t[1]
        marks=int(t[2])
        student=(roll,name,marks)
        data.append(student)
    total=0
    for student in data:
        total+=student[2]
    avg=total/len(data)
    return total,avg
     