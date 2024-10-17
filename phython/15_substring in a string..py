import re
s = 'ababababa'

res= len(re.findall('(?=(aba))', s))

print("Number of substrings", res)
