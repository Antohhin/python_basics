"""
Последовательность поиска объектов в пайтон:
local, non-local, global, built-in
"""

# builtins scope
# global scope
t_c = 18
tmp = 'ok'

#non-local if new funcs exist
def convert_fahrenheit(t_c):
    # local scope
    tmp = t_c * 9/5
    return tmp + 32


if __name__ == '__main__':
    
    print(convert_fahrenheit(t_c))
    print(tmp)