#Нет необходимости использовать вложеные циклы.
#Вводишь переменую N
#Проходишь по массиву (1 раз)
#и если ch1[i] больше левого и правого соседа и больше 3х, то
#Resultat[n]:=time[i]
#ResIndex[n]:=i;
#inc(n);
#Изначально длину массивов Resultat и ResIndex устанавливаешь равной длине ch1. А потом укорачиваешь до N.
#Приблизительно так.



def pick_peaks(arr):
    peak, pos = [], []
    res = {"peaks": [], "pos": []}

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            peak, pos = [arr[i]], [i]

        elif arr[i] < arr[i - 1]:
            res["peaks"] += peak
            res["pos"] += pos
            peak, pos = [], []
    print(res)
    return res

    #your code here
#pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1])# {"pos": [3, 7], "peaks": [6, 3]})
pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1])#{"pos":[3,7,10], "peaks":[6,3,2]})
pick_peaks([1, 2, 2, 2, 1]) #{pos: [1], peaks: [2]}
pick_peaks([1, 2, 2, 2, 3])