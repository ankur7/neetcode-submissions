class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        from bisect import bisect_right
        if key not in self.store:
            return ""

        arr = self.store[key]
        i = bisect_right(arr, timestamp, key=lambda x: x[0]) - 1

        if i >= 0:
            return arr[i][1]
        return ""