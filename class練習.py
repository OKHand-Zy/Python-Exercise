# -*- coding: utf-8 -*-

class circle  :
    def __init__(self):
        self.pi=3.14
        self.radios=1 
    def getArea(self,x):
        return self.pi*x*x

class halo :
    def getArea(self,x):
        return x*x
    
class tringle (halo,circle) :
    def getArea(self,x):
        return super().getArea(x)

c = circle()
print( tringle().getArea(10) )


'''

# 汽車類別
class Cars:
    # 建構式
    def __init__(self, color, seat):
        self.color = color  # 顏色屬性
        self.seat = seat  # 座位屬性
    # 方法(Method)
    def drive(self):
        print(f"My car is {self.color} and has {self.seat} seats.")
#主程式
mazda = Cars("blue", 4)
mazda.drive()  #執行結果：My car is blue and has 4 seats.
'''