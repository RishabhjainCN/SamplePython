class Date:

    def __init__(self):
        self.dd = 0
        self.mm = 0
        self.yy = 0
    def set(self,d,m,y):
        self.dd = d
        self.mm = m
        self.yy = y
    def show(self):
        print(self.dd, self.mm, self.yy)

x = Date()
x.set(26,6,19)
