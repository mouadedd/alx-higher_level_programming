#!/usr/bin/python3
'''this is a test'''


def pascal_triangle(n):
    '''this is a test'''
    if n <= 0:
        return []

    mutlatat = [[1]]
    while len(mutlatat) != n:
        mutlat = mutlatat[-1]
        tmp = [1]
        for elem in range(len(mutlat) - 1):
            tmp.append(mutlat[elem] + mutlat[elem + 1])
        tmp.append(1)
        mutlatat.append(tmp)
    return mutlatat
