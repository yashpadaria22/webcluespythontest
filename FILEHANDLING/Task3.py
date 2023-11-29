import pandas as pd
class Datapipeline():
    def __init__(self,data=None) :
        self.data=data
    def load(self,path):
        self.data=pd.read_csv(path)
        return self
    def filter(self, column, condition=None, **values):
        # Apply filtering based on conditions
        if condition == 'greater_than':
            self.data = self.data[self.data[column] > values['value']]
        elif condition == 'less_than':
            self.data = self.data[self.data[column] < values['value']]
        elif condition == 'equal_to':
            self.data = self.data[self.data[column] == values['value']]
        elif condition =="greater_than_equal_to":
            self.data = self.data[self.data[column] >= values['value']]
        elif condition =="less_than_equal_to":
            self.data = self.data[self.data[column] <= values['value']]
        # Add more conditions as needed
        self.data.to_csv("filterdata.csv",index=False)
        return self
dsl = Datapipeline()
# path="C:\Users\HP\Desktop\Python_test\FILEHANDLING"  
path=input("Enter path of your CSV file: ")
dsl.load(path).filter(column='age', condition='greater_than', value=30)