import pandas as pd


Sales = pd.DataFrame({'Apples': [35,41], 'Bananas': [21,34]}, index=['2017 Sales', '2018 Sales'])

print(Sales)

Sales.to_csv('fruit.csv')