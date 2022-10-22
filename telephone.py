dig=input("Enter any digit:")
l = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
ans=[]
ld=len(dig)
d=""
if d=="":
    print[ld]
    p=ld
    st=[]
    if p==ld:
        ans.append(st)
    else:
        le=l[d[p]]
        for lee in le:
            ans=p+1,st+lee
print(ans)