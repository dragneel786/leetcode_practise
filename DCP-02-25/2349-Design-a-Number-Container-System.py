class NumberContainers:

    def __init__(self):
        self.number_to_index = defaultdict(list)
        self.index_to_number = dict()
        
    def change(self, index: int, number: int) -> None:
        # 1 > 10, 10 > 1
        if self.index_to_number.get(index, -1) == number:
            return

        self.index_to_number[index] = number
        heappush(self.number_to_index[number], index)

    def find(self, number: int) -> int:
        while(self.number_to_index[number] and \
         self.index_to_number[self.number_to_index[number][0]] != number):
            heappop(self.number_to_index[number])
        
        if self.number_to_index[number]:
            return self.number_to_index[number][0]
            
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)