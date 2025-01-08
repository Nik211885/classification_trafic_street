from django.http import HttpRequest
from django.shortcuts import render
from model import Model, TypeModel
from django.http import JsonResponse
from data_perdict import DataPerdict
# Create your views here.

def index(request: HttpRequest):
    if(request.method == "POST"):
        x_pred = DataPerdict.create_data()
        model = Model.load_model(TypeModel.KNN)
        y_pred = model.perdict(x_pred)
        return render(request, "index.html", {"LabelPred": y_pred})
    else:
        return JsonResponse({"error": "Method Not Allowed"}, status=405)