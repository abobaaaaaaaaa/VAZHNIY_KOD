import re
a='01/02/2011,32/13/1231,21/21/3123,3213123t34t4gw435vgw4'
b=str(input())
print(re.findall(b,a))
