import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM vikra@'
lst = re.findall('\\S+', s)
print(lst)
z=len(lst)
for k  in range(z):
    print(lst[k], k+1)