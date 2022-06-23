def median(a):
    '''
    input : a list
    output: b number median of a list
    '''
    a = sorted(a)
    n = len(a)
    if n % 2 :
        return a[n//2]
    else:
        return (a[n//2-1] + a[n//2])/2