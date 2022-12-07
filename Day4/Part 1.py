f= open('Day4/Sample.txt',"r")
input=f.read()
count=0
for i in  input.split('\n'):
    i=i.split(",")
    i = [item.split('-') for item in i]
    if int(i[0][0])<= int(i[1][0]) and int(i[0][-1]) >= int(i[1][-1]):
        count+=1
    elif int(i[0][0])>= int(i[1][0]) and int(i[0][-1]) <= int(i[1][-1]):
        count+=1
print(count)