import datetime
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
import sys
import os
import logging

logger = logging.getLogger(__name__)

from sklearn.model_selection import GridSearchCV
sys.path.append(os.path.join(os.path.dirname(__file__)))
from data_perdict import DataPerdict
from model import Model, TypeModel

def index(request: HttpRequest):
    if request.method == "POST":
        # Get the datetime string and convert to datetime object
        date_time_str = request.POST.get("event_datetime")
        car_count = request.POST.get("car_count")
        bike_count = request.POST.get("bike_count")
        bus_count = request.POST.get("bus_count")
        trunk_count = request.POST.get("trunk_count")
        # Get model type and other data, ensuring proper type conversion
        model_type = request.POST.get("model_type")

        # Create prediction data
        data_perdict_model = DataPerdict()
        data_perdict = data_perdict_model.create_data(car_count, bike_count, bus_count, trunk_count, date_time_str)
        model_ = Model()
        model: Model
        # Initialize model and make predictions
        if model_type == "KNN":
            model = model_.get_instance(TypeModel.KNN)
        elif model_type == "Random forest":
            model = model_.get_instance(TypeModel.RandomForest)
        else:
            return JsonResponse({'Error': 'Model type not supported'}, status=400)

        y_pred = model.perdict(data_perdict)

        return JsonResponse({'label': f'{y_pred}'})

    elif request.method == "GET":
        return render(request, "index.html", {
            "Title": "Dự đoán tình trạng giao thông"
        })
    else:
        return JsonResponse({"error": "Method Not Allowed"}, status=405)