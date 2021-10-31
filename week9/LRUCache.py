
class LRUCache:

    def __init__(self, capacity: int):
        self.od, self.cap = collections.OrderedDict(), capacity

    def get(self, key: int) -> int:
        if key in self.od.keys(): 
            self.od.move_to_end(key)
            return self.od[key]
        else: return -1
        
    def put(self, key: int, value: int) -> None:
        if len(self.od) == self.cap and key not in self.od.keys(): self.od.popitem(last=False)
        self.od[key] = value
        self.od.move_to_end(key)

