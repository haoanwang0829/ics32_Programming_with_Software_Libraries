n = int(input())
def diagonal(n):
    m = n -1
    i = 0
    print('+' + '-' + '+')
    while i < m:
        j = 2 * i
        print(j * ' ' + '|' + ' ' + '|' )
        print(j * ' ' + '+' + '-' + '+' + '-' + '+')
        i += 1
    print(2 * m * ' ' + '|' + ' ' + '|')
    print(2 * m * ' ' + '+' + '-' + '+')
        
diagonal(n)
