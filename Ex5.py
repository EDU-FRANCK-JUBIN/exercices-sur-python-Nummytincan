def minMaxMoy(list):
    min = list[0]
    max = list[0]
    moy = list[0]
    for i in range(1, len(list)-1):
        moy += list[i]
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]
    moy /= len(list)
    tuple = [min, max, moy]
    print(tuple)


minMaxMoy([10, 18, 14, 20, 12, 16])