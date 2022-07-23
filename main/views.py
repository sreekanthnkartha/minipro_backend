from django.shortcuts import render
import pickle
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
# Create your views here.
class ModelView(APIView):
    def post(self,request):
        try:
            poly = PolynomialFeatures(7)
            model=pickle.load(open('model.sav','rb'))
            purchase_units=int(request.data['purchase_units'])
            purchase_price=int(request.data['purchase_price'])
            total_purchase=int(request.data['total_purchase'])
            sales_units=int(request.data['sales_units'])
            sales_price=int(request.data['sales_price'])
            total_sales=int(request.data['total_sales'])
            profit=int(request.data['profit'])
            test=pd.DataFrame({'purchase(units)':[purchase_units],
                       'purchase price':[purchase_price],
                       'total (purchase)':[total_purchase],
                       'sales(units)':[sales_units],
                       'sales price':[sales_price],
                       'total(sales)':[total_sales],
                       'profit':[profit],})

            test = poly.fit_transform(test)
            pred=model.predict(test)
            return Response({"output":int(pred[0][0])},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)