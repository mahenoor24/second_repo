s=input("Enter your roman number :")
rom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
dec=0
for i in range(len(s)-1,-1,-1):
    num=rom[s[i]]
    if 3*num<dec:
        dec=dec-num
    else:
        dec=dec+num
print(dec)   