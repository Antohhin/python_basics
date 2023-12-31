"""
1.1 Введение
Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.

Вашей программе на вход подается последовательность строк.
Первая строка содержит число n (1 ≤ n ≤ 100).
В следующих n строках содержится по одному целому числу.

Выведите одно число – сумму данных n чисел.

Sample Input 1:

2
2
3
Sample Output 1:

5
Sample Input 2:

2
-2
-2
Sample Output 2:

-4
Sample Input 3:

1
31
Sample Output 3:

31
"""

def my_sumnums():
    n = int(input())
    sum = 0
    while n > 0:
        num = int(input())
        n -= 1
        sum += num
    print(sum)


def best_sumnums():
    n = int(input())
    s = 0
    for i in range(n):
        s += int(input())
    print(s)