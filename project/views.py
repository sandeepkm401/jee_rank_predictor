from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv(r"C:\Users\sande\Downloads\jee_percentile_vs_air_5000_students.csv")
X = df.drop("All_India_Rank", axis = 1)
y = df["All_India_Rank"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)

def rankpredictor(request):
    if request.method == "POST":
        percentile = float(request.POST.get("percentile"))
        rank = int(model.predict([[percentile]])[0])
        rll = rank - 264
        if rll <= 0:
            rll = 2
        rul = rank + 209

        if percentile == 100:
            rll = 1
            rul = 2

        d = {
            "rll": rll,
            "rul": rul,
            "percentile": percentile
        }
        return render(request, "home.html", context = d)
    elif request.method == "GET":
        return render(request, "home.html")
def working(request):
    return render(request, "working.html")