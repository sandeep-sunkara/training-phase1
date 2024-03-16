class faculty:
    def __init__(self,name,dept,id):
        self.name=name
        self.dept=dept
        self.id=id
    def print_info(self):
        print("faculty information:","\n",self.name,"\n",self.dept,"\n",self.id)
obj=faculty("someone","somedept",1234)
obj.print_info()

class cse(faculty):
    pass
obj=cse("jyothi","cse",4321)
obj.print_info()
