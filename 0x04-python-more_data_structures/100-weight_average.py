#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numrtor= 0
    denmtor = 0

    for tupl in my_list:
        numrtor += tupl[0] * tupl[1]
        denmtor += tupl[1]

    return (numrtor / denmtor)
