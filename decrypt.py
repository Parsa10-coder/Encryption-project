def decrypt(s:str, key:int) -> str:
    '''
    Parameters
    ----------
    s : str
        Encrypted string for decrypt.
    key : int
        The number of execution steps.

    Returns
    -------
        Primary string.

    '''
    ls = list(s)
    for _ in range(key):
        ls.insert(len(ls), ls.pop(0))
        for i in range(len(ls)):
            if ls[i] == 'a':
                ls[i] = 'z'
            elif ls[i] == 'A':
                ls[i] = 'Z'
            else:
                ls[i] = chr(ord(ls[i]) - 1)
                
    return ''.join(ls)
