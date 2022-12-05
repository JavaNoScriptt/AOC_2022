input = open('sample.txt','r')
input = input.read()
highest =0
for items in input.split('\n\n'):
  current = 0
  for i in items.split('\n'):
    current+=int(i)   
  if current > highest:
    highest = current
print(highest)