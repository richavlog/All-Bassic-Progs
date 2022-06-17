#given_number like= 2345.1347216482926
number=float(input("enter a number"))
# using % operator and printing upto 4 decimal places
ans_value = '%.4f' % number
# print the answer
print("the given number upto 4 decimal places", ans_value)