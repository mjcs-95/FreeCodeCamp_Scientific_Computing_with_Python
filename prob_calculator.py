import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs): 
        self.contents  = []
        for key, value in kwargs.items():
            self.contents.extend([key] * value)

    def draw(self, n):
        drawed = []
        for i in range( min( n,  len(self.contents) )):
            idx = random.randint(0,len(self.contents)-1)
            drawed.append(self.contents.pop(idx))
        return drawed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):    
    M = 0    
    for i in range(num_experiments):
        drawed = copy.deepcopy(hat).draw(num_balls_drawn)
        success = True
        for key,value in expected_balls.items():            
            if drawed.count(key) < value:
                success = False
                break        
        if success:
            M += 1                
    return M / num_experiments
