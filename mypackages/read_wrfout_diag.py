def read_wrfout_diag(filepath,china=1):
    # o3等变量文件
    with open(filepath, 'r') as f:
        array = [line.strip().split(' ') for line in f]
        ar = array[:-1]
        for j in range(0, len(ar)):
            while '' in ar[j]:
                ar[j].remove('')
        # ar = ar[::-1]
    return ar
