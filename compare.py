from data_generator import randomSubset, ascendingSubset, descendingSubset, constantSubset, vShapedSubset, aShapedSubset
from sorts import insertionSort, selectionSort, heapSort, mergeSort, quickSortIterative, quickSortMiddle, quickSortRandom
from timeit import default_timer as timer
from copy import deepcopy
import pandas as pd
import xlsxwriter

max, jump, amount= 25000, 1000,[]
algorithms=[insertionSort, selectionSort, heapSort, mergeSort, quickSortIterative]#quickSortIterative, quickSortMiddle, quickSortRandom
dataSets= aShapedSubset(max, jump)#randomSubset(max, jump), ascendingSubset(max, jump), descendingSubset(max, jump), constantSubset(max, jump), vShapedSubset(max, jump)
for i in range(0, max+1, jump):
    amount.append(i)

def compare_algorithm(fun, *args):
    start=timer()
    fun(*args, 0, len(*args)-1)
    endtime=timer()-start
    result.append(endtime)
    return result

# do quicksortow
# main=[]
# for a in algorithms:
#     for ds in dataSets:
#         result=[]
#         for d in ds:
#             for i in algorithms:
#                 compare_algorithm(i, deepcopy(d))
#         main.append(result)

main=[]
for a in algorithms:
    result=[]
    for ds in dataSets:
        compare_algorithm(a, deepcopy(ds))
    main.append(result)

df = pd.DataFrame.from_dict({'rozmiar zbioru':amount, 'skrajnie prawy':main[0], 'środkowy':main[1], 'losowy':main[2]})
df.to_excel('quick.xlsx', header=True, index=False)
