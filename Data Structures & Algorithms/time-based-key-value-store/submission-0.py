class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        curr = timestamp
        while curr >= 0:
            if (key, curr) in self.map:
                return self.map[(key, curr)]
            curr -= 1
        return ""
        
