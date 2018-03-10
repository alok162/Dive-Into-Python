class Name:
    def __init__(self,fname='Alok', lname='Choudhary'):
        self.__fname=fname
        self.__lname=lname
    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self,f_name):
        self.__fname=f_name
    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self,l_name):
        self.__lname=l_name
        
obj = Name()
obj.fname='Vikki'
print obj.fname,obj.lname
obj.lname='Singh'
print obj.fname, obj.lname

