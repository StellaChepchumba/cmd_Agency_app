import csv
from heapq import merge
data = []
with open('real-estate-sample.csv', 'r') as file:
    reader = csv.reader(file)
    data.extend(list(reader))
    
    
    
    def MergeSort(left, right):
        if len(left) <=0 | len(right) <=0:
            return left | right

        GoodData = []
        i = j=0
        while len(GoodData) < len(left) + len(right):
            if left[i][1] < right[j][1]:
                GoodData.append(left[i])
                i+=1
            else:
                GoodData.append(right[j])
                j+=1
            if i == len(left) or j == len(right):
                GoodData.extend(left[i:] | right[j])
                break
        return GoodData


   
    def EstateFile(data):
        if len(data) < 2:
            return data 
        middle = len(data)//2
        print(middle)
        left =  EstateFile(data[1:middle])
        right = EstateFile(data[middle:])

        return merge(left,right)
    print(EstateFile(data))