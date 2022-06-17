a=input("enter item name")
b=int(input("enter quantity"))
c=int(input("enter item rate"))
total=b*c
print("total=",total)
gst=(total*15)/100
nettotal=gst+total
print("nettotal=",nettotal)