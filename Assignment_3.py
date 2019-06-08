l=[]
i=0
n=int(input("enter number"))
l.append(n)
count=1
while i==0:
    n=input("wanna enter more?(y/n)")
    if n=="y":
        k=int(input("enter number"))
        l.append(k)
        count+=1
    else:
        break

print("list:",l)
l.sort()
print("sorted list:",l)

print("enter element")
ele=int(input())

front=0
end=count
check=0

while front<end:
    mid=int((front+end)/2)
    if ele>l[mid]:
        front=mid
    elif ele<l[mid]:
        end=mid
    else:
        print("element found at",mid+1,"position")
        check=1
        break

if check==0:
    print("element not found")
