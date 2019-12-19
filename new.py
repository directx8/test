
# import matplotlib
import os
import numpy as np

from random import randint

# nikola is coool

# 3D  array for the thing we want

class PD:
    def __init__(self, LED, wavelenght):
        self.LED = LED
        self.wavelenght = wavelenght
        self.nLED = 2;
        self.nWavelenght = 3;
        
        self.shape = (30, self.nWavelenght)
        self.dt = np.zeros(self.shape) 
    
    def Data_pop(self, index, data):
        self.dt[index, self.wavelenght] = data
        
    def Return_data(self):
        return self.dt
    

def Main():
    
    l = PD(2,2)
    
    for i in range(0,3):
        for j in range(0,30):
            data = randint(0,255)
            l[2].Data_pop(j,data)
        
        
    print(l.Return_data())
    
    


if __name__ == '__main__':
	Main()


        
