class calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def add(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y

if __name__ == "__main__":
    a = calc(10, 20)
    print(a.add())