f= open('given.txt',"r")
input=f.read()
total = 0
for item in input.split('\n'):
    print(len(item))
    firstC, secondC = item[:len(item)//2], item[len(item)//2:]
    print(firstC)
    print(secondC)
    for character in firstC:
        if secondC.find(character)!=-1:    
            if ord(character) <122 and ord(character) >97:
                total+=(ord(character)-96)
            elif ord(character) <90 and ord(character) >65:
                total+=(ord(character)-38)
print(total)
