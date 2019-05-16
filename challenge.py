import random
dict1={}
for i in range(1,127):
    dict1.__setitem__(i,chr(i))

prime=[]
for num in range(3,11084):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           prime.append(num)
string=input("Enter plain text:")
prime1=random.choice(prime)
prime2=random.choice(prime)
n=prime1*prime2
string=list(string)
m=[]
for i in string:
    temp=n%ord(i)
    if temp>=33 and temp<=126:
        m.append(chr(temp))
    if temp<33:
        m.extend((chr(33),chr(33-temp)))
    if temp>126:
        m.extend((chr(126),chr(temp-126)))
cipher=str(''.join(m))
print(cipher)
