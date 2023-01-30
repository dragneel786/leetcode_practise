from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_freq = dict()
        self.freq_key = defaultdict(OrderedDict)
        self.minfreq = 1

    
    def get(self, key: int) -> int:
        if(key not in self.key_freq):
            return -1
        
        freq = self.key_freq[key]
        self.key_freq[key] = freq + 1
        
        freq_dict = self.freq_key[freq]
        value = freq_dict.pop(key)
        self.freq_key[freq + 1][key] = value
    
        if(self.minfreq == freq and not self.freq_key[freq]):
            self.minfreq += 1
        return value
    
    
    def put(self, key: int, value: int) -> None:
        
        if(key in self.key_freq):
            self.get(key)
            self.freq_key[self.key_freq[key]][key] = value
        else:
            self.cap -= 1
            self.key_freq[key] = 1
            self.freq_key[1][key] = value
            if self.cap < 0:
                self.cap += 1
                k, v = self.freq_key[self.minfreq].popitem(False)
                del self.key_freq[k]
            self.minfreq = 1
        
        

# op = ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
# val = [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
# for o, v in zip(op, val):
#     if o == "LFUCache":
#         cache = LFUCache(*v)
#     elif o == 'put':
#         cache.put(*v)
#     else:
#         print(cache.get(*v))

# # Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)