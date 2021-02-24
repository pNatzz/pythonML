class Got7member:
    def __init__(self): # dunder -> double underscores
        self.fname = ""
        self.number = ""

class Got7member2:
    def __init__(self, fname, number):
        self.fname = fname
        self.number = number

if __name__ == '__main__':
    m1 = Got7member()
    m1.fname = "JB"
    m1.number = 1

    m2 = Got7member()
    m2.fname = "Mark"
    m2.number = 2

    m3 = Got7member()
    m3.fname = "Jackson"
    m3.number = 3

    m4 = Got7member2("BB", 4)
    m5 = Got7member2("Jinyoung", 5)

    print(m1.fname)
    print(m4.fname)