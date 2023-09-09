"""
Поиск вхождений символа а, но без backtracking
"""

import re

regex = r'(?>a+)b'
print(re.findall(regex, 'a'*100))