def read_wrfout(filepath):
    # o3等变量文件
    '''
    return list
    
    '''
    with open(filepath, 'r') as f:
        array = [line.strip().split(' ') for line in f]
        ar = array[6:]
        for j in range(0, len(ar)):
            while '' in ar[j]:
                ar[j].remove('')
    return ar