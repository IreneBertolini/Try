import pandas as pd
import numpy as np

cocktails = pd.read_csv ("/Users/irenebertolini/Desktop/data_cocktails.csv")

cocktails.head(1)
del cocktails['Garnish_type']
del cocktails['Garnish_amount']
del cocktails['Value_gr']
del cocktails['Basic_taste']

cocktails = cocktails.rename(columns={'strDrink': 'Drink', 'strCategory': 'Category' , 'strIngredients':'Ingredients', 'strInstructions': 'Instructions', 'strMeasures':'Measures','strGlass':'Glass'})
cocktails
cocktails = cocktails.fillna(0)
