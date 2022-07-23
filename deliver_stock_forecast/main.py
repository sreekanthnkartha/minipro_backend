import pandas as pd
from sklearn import model_selection
from sklearn.preprocessing import PolynomialFeatures
purchase_units=int(input("Enter purchase units: "))
purchase_price=int(input("Enter purchase price: "))
total_purchase=int(input("Enter total purchase: "))
sales_units=int(input("Enter sales units: "))
sales_price=int(input("Enter sales price: "))
total_sales=int(input("Enter total sales: "))
profit=int(input("Enter profit: "))
test=pd.DataFrame({'purchase(units)':[purchase_units],
                   'purchase price':[purchase_price],
                   'total (purchase)':[total_purchase],
                   'sales(units)':[sales_units],
                   'sales price':[sales_price],
                   'total(sales)':[total_sales],
                   'profit':[profit],})
test = poly.fit_transform(test)
pred=model_selection.predict(test)
print("output:",int(pred[0][0]))