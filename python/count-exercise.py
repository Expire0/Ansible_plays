class Twit:
    def count3(self,check):
        self.check = check
        self.taz1 = self.check % 3
        self.taz2 = self.check % 5
        return self.taz1,self.taz2

    def count5(self):
        if self.taz1 == 0:
            print(str(self.check) + "- foo")
        if  self.taz2 == 0:
            print(str(self.check) + "- Bar")
        if self.taz1 == 0 and self.taz2 == 0:
            print(str(self.check) + "- Foobar")


top = 100
f = Twit()

for num in range(top):
    f.count3(num)
    f.count5()
