from abstract import CSVSearch

class SearchCSV(CSVSearch):
    def __init__(self,data, list, id ):
        self.data = data
        self.target =list
        self.finder = id
    
    def search(self):
        left = 0
        right = len(self.data)-1
       
        while left <= right:
            mid = (left +right)
            if list == self.data[mid][self.id[6]]:
                return self.data[mid]
            else:
                if list < self.data[mid][self.id[6]]:
                   right = mid -1 
                if list > self.data[mid][self.id[6]]:              
                    left = mid +1