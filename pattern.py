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
    for j in range(n):
        if j:
           test_string += '\n'
        for i in range(n-j):
            test_string += str(n-i)

    return test_string