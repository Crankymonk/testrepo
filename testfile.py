class CountingClicker:
    def __init__(self, count: int = 0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    def click(self, num_times = 1):
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0