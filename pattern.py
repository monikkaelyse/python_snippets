def pattern(n):
    ''' Returns pattern in form:
    
    (n)(n-1)(n-2)...4321
    (n)(n-1)(n-2)...432
    (n)(n-1)(n-2)...43
    (n)(n-1)(n-2)...4
    ...............
    ..............
    (n)(n-1)(n-2)
    (n)(n-1)
    (n)
    
    '''
    
    test_string = ''
    for i in range(n):
        if i:
           test_string += '\n'
        for j in range(n-i):
            test_string += str(n-j)

    return test_string
