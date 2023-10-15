"""
Реализуйте программу, которая будет эмулировать работу с пространствами имен.
Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.

В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:

- create <namespace> <parent> –  создать новое пространство имен
 с именем <namespace> внутри пространства <parent>
- add <namespace> <var> – добавить в пространство <namespace> переменную <var>
- get <namespace> <var> – получить имя пространства, из которого
 будет взята переменная <var> при запросе из пространства <namespace>,
   или None, если такого пространства не существует

Sample Input:
    9
    add global a
    create foo global
    add foo b
    get foo a
    get foo c
    create bar foo
    add bar a
    get bar a
    get bar b

Sample Output:
    global
    None
    bar
    foo

Test3
    5
    create first global
    create second first
    create third second
    add first my_var
    get third my_var

Ответ
    first
"""


def get(namespace, var):
    if var in scopes[namespace]['variables']:
        return namespace
    else:
        while namespace != 'global':
        # if namespace == 'global':
            # return None
            return get(scopes[namespace]['parent'], var)
        return None

if __name__ == '__main__':
    
    query_number = int(input())
    scopes = {'global': {'parent': None, 'variables': set()}}
    for query in range(query_number):
        # print(input())
        cmd, namesp, arg = input().split()
        
        if cmd == 'create':
            scopes[namesp] = {'parent': arg, 'variables': set()}
            # print(f'create scope:', scopes)
        if cmd == 'add':
            scopes[namesp]['variables'].add(arg)
            # print(f'add to new var: {arg} to {scopes[namesp]}')
        if cmd == 'get':
            result = get(namesp, arg)
            print(result)
            # if arg in scopes[namesp]['variable']:
            #     space_title = scopes[namesp]
            # else:
            #     space_title = None
        
        # print(query)

# def foo():
#     a = 5
#     print(a)
# print(foo())
