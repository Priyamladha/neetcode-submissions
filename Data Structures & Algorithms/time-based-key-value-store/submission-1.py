class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp,value])
        # print(self.hashmap)

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hashmap[key]
        # print(arr)
        if arr:
            l = 0
            r = len(arr) - 1

            maxT = [-1,""]
            while l<=r:
                m = (l+r)//2

                if arr[m][0] > timestamp:
                    r = m - 1
                else:
                    if arr[m][0] > maxT[0]:
                        maxT = arr[m]
                    l = m + 1
            return maxT[1] if maxT[0] != -1 else ""   

        return "" 
        
