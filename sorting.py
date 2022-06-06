from abstract import CSVSort

class MergeSort(CSVSort):
   
    
    def  __init__(self, data):
        self.data = data
    
    def sortData(self):
        if len(self.data) >1:
            middle = len(self.data)//2
            left =  self.data[:middle]
            right = self.data[middle:]

            leftSort = MergeSort(left)
            leftSort.sortData()

            rigthSort = MergeSort(right)
            rigthSort.sortData()            

            o = j=z=0
            while o < len(left) and j < len(right):
                if left[o][1] < right[j][1]:
                    self.data[z] = left[o]
                    o +=1
                
                else:
                    self.data[z]=right[j]
                    j+=1
                z+=1
            
            while o < len(left):
                self.data[z] = left[o]
                o+=1
                z+=1
            
            while j < len(right):
                self.data[z] = right[j]
                j+=1
                z+=1
        
        print(self.data)
    

