
def get_input():
    x = None
    while x == None:
        try:
            x = int(input('please input n: '))        
        except ValueError as err:
            print(err)
    return x


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
n = get_input()
move(n, 'A', 'B', 'C')
