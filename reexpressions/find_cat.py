"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.

Sample Input:

cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?
Sample Output:

cat
catapult and cat
"cat"
!cat?
"""
import re
import sys

for line in sys.stdin:
    pattern = r"\bcat\b"
    line = line.strip()
    if re.search(pattern, line):
        print(line)
