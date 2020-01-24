import plotly.express as px
import os
import numpy as np

from random import randint

# Requirements: correlation, adding data from leds, boundry value detection, value plot correlation

class LED_set:
    def __init__(self, sets, num_leds):
        #init a 3d array and clear it 
        num_leds = num_leds
        sets = sets
        self.leds = [[[0 for k in range(num_leds)] for j in range(num_leds)] for i in range(sets)]
        for i in range(num_leds):
            for j in range(sets):
                self.leds[j][i].clear()
        
    def data_add(self, data, led, sets):
        self.leds[led][sets].append(data)
          
    def return_data(self):
        return(self.leds)
    
def Boundries(data, size, led, sets):
    countZero = 0
    countMax = 0
    
    for i in range(sets):
        for j in range(led):
            for y in range(size):
                if (data[i][j][y] > 0 and data[i][j][y] < 255):
                    countMax = 0
                    countZero = 0
                    
                if data[i][j][y] == 0:
                    countZero = countZero + 1
                    if countZero == 3:
                        print("Zero Value!")
                        countZero = 0
                
                if data[i][j][y] == 255:
                    countMax = countMax + 1
                    if countMax == 3:
                        print("Max Value!")
                        countMax = 0
                    
def Main():
    num_data_samples = 5
    num_sets = 4
    num_leds = 3
    num_corr_coef = 2
    
    # Init and clear the correlation coeffitient list
    correl_coef = [[0 for k in range(num_corr_coef)] for j in range(num_corr_coef)]
    for j in range(num_corr_coef):
        correl_coef[j].clear()
    
    led_sets = LED_set(num_sets, num_leds)
    data = led_sets.return_data()
    
    # populate data
    # number of Data samples
    for j in range(num_data_samples):
        # number of led sets
        for i in range(num_sets):
            # number of leds per cluster
            for k in range(num_leds):
                led_sets.data_add(randint(0,255), i, k)
        
    # Print the gathered data
    print(data)
    
    # correlation coef
    for i in range(num_sets):
        for j in range(num_leds):
            kf = np.corrcoef(data[i-1][j], data[i][j])
            for k in range(num_corr_coef):
                correl_coef[k].append(kf[0][1])
             
    fig = px.scatter(x=correl_coef[0], y=correl_coef[1])
    fig.show()
    
    Boundries(data, num_data_samples, num_leds, num_sets)
    
            
if __name__ == '__main__':
	Main()


        
