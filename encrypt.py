def encrypt(s:str, key:int) -> str:
    '''
    
    Parameters
    ----------
    s : str
        given string for encrpyt.
    key : int
        The number of execution steps.

    Returns
    -------
    Encrypted string

    '''
    ls = list(s)
    for _ in range(key):
        ls.insert(0, ls.pop())
        for i in range(len(ls)):
            if ls[i] == 'z':
                ls[i] = 'a'
            elif ls[i] == 'Z':
                ls[i] = 'A'
            else:
                ls[i] = chr(ord(ls[i]) + 1)
                
    
    return ''.join(ls)
    
