import re

regex = r'(?>a+)b'
print(re.findall(regex, 'a'*100))