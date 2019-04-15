import pandas as pd

class machinelearning:
    
    def importset(self, i=None):
        data = pd.read_excel('F:\web development\Minor Project\cities.csv')
        if i == None:
            return data
        else:
            return data[i]