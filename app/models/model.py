from enum import Enum
from pathlib import Path
import joblib
from sklearn.model_selection import GridSearchCV
from data_perdict import DataPerdict
class TypeModel(Enum):
    KNN = "knn_model.pkl",
    RandomForest = "random_forest_model.pkl"

class Model:
    _model: dict = {}
    def __init__(self, model: GridSearchCV):
        self.model = model
    @staticmethod
    def __load_model(type: TypeModel):
        dir_save_models = f"{Path(__file__).resolve().parent.parent}\model_store"
        path_mode = f"{dir_save_models}\{str(type.value).replace("('","").replace("',)","")}"
        model = joblib.load(path_mode)           
        return Model(model)
    
    def perdict(self,data: DataPerdict):
    
    # Perform prediction
        y_pred = self.model.predict(data.convert_to_feature())

        return y_pred[0]
    
    def get_instance(self, type: TypeModel):
    # Singleton check - load model only if not loaded
        if(self._model.get(type, None) is None):
            self._model[type] = self.__load_model(type)
        return self._model.get(type)