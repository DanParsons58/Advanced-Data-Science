def print_pyramid(n):
    m = n-1
    for n in range(n):
        print('-'*(m-n) + '='*(2*n+1) + '-'*(m-n))