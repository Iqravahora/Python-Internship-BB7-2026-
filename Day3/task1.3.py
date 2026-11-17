number = [10,15,20,25,30,35,30,45,50,15]
uniq = []

for num in number:
    if num not in uniq:
        uniq.append(num)
        
print ("original:",number)
print ("uniq:",uniq)
        