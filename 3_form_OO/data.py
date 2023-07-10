
class Data:

    def __init__(self, d, m, a):
        self.__d = d
        self.__m = m
        self.__a = a
    

    def get_a(self):
        return self.__a
    
    def get_d(self):
        return self.__d
    
    def get_m(self):
        return self.__m
    
    def formatada(self):
        print(f"{self.get_d()}/{self.get_m()}/{self.get_a()}")