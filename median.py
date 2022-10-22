arr1=input("Enter an array of numbers:")
arr2=input("Enter another array of numbers:")
arr3=arr1+arr2
print("After combining two arrays:",arr3)
arr3=sorted(arr3)
print("After sorting two arrays:",arr3)
if len(arr3)/2!=0:
    m=int((len(arr3))/2)
    print("The median is:",arr3[m])
else:
    m1=int(len(arr3)/2-1)
    m2=int(len(arr3)/2)
    print("The median is:",arr3[m1]+arr3[m2]/2)