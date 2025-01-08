from enum import Enum
from pathlib import Path
import joblib
from sklearn.model_selection import GridSearchCV
from data_perdict import DataPerdict
class TypeModel(Enum):
    KNN = "knn_model.pkl",
    RandomForest = "random_forest_model.pkl"

class Model:
    def __init__(self, model: GridSearchCV):
        self.model = model
    @staticmethod
    def load_model(type: TypeModel):
        dir_save_models = Path(__file__).resolve().parent.parent + "\\model_store"
        model = joblib.load(f"{dir_save_models}\\{type}")           
        return Model(model)
    def perdict(self,data: DataPerdict):
        label = {0: 'heavy', 1: 'high', 2: 'low', 3: 'normal'}
        y_pred =  self.model.predict(data)
        label = label.get(int(y_pred), None)
        if(label is None):
            raise Exception("Has new label")
        return label