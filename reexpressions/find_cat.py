"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.
"""
import re
import sys

for line in sys.stdin:
    pattern = r"\bcat\b"
    line = line.strip()
    if re.search(pattern, line):
        print(line)
