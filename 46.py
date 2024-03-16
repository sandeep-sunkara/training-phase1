class f15:
    def __init__(self,st,et):
        self.st=st
        self.et=et
        print("start time in constructor:",st)
        print("end time in constructor:",et)
    def disp(self):
        print("start time in disp:",self.st)
        print("end time in disp:",self.et)
obj=f15(1,4)
obj.disp()