from datetime import datetime
import joblib
import numpy as np
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier

'''
WHY I CHOSE RANDOM FOREST CLASSIFIER-
I went with the Random Forest Classifier for this 
data because it's like the Swiss Army knife of models—pretty 
good at handling various features and making sense of complex datasets. 
 The idea is that it creates a bunch of decision trees 
 during training and then combines their predictions to give us an 
 overall prediction. For our task of predicting 'Rarity' 
 based on things like 'Level,' 'Health,' 'Energy,' and 'Sanity,' 
 this model is a solid fit. It's great because it can handle tricky 
 relationships in the data, doesn't mind if things aren't perfectly linear, 
 and helps us avoid overthinking the details. I tweaked some settings, 
 like the number of trees and how deep they can go, to find the sweet spot 
 between being smart about the data and not getting too caught up in it. So, 
 in a nutshell, I chose the Random Forest Classifier because it's reliable and 
does the job well for predicting 'Rarity' in our diverse dataset.
    
'''


class Machine:
    """
      Machine Class: Represents a Random Forest Classifier model for predicting 'Rarity'.

      Attributes:
          - name (str): The name of the model, set to "Random Forest Classifier".
          - target (Series): The target variable ("Rarity") extracted from the input DataFrame.
          - features (DataFrame): The DataFrame containing input features, excluding the target variable.
          - timestamp (str): The timestamp of when the model instance is created, formatted as "%Y-%m-%d %H:%M:%S".
          - model (RandomForestClassifier): The Random Forest Classifier model initialized with specified hyperparameters.

      Methods:
          - __init__(self, df: DataFrame): Constructor method initializing the model with input DataFrame.
          - __call__(self, pred_basis: DataFrame) -> Tuple: Callable method for making predictions on a provided DataFrame (`pred_basis`).
              Returns a tuple containing the predicted value and confidence.
          - save(self, filepath: str): Saves the current instance of the model to a specified file using joblib.
          - open(filepath: str) -> 'Machine': Static method to load a previously saved model instance from a file using joblib.
          - info(self) -> str: Returns a formatted string providing basic information about the model.
      """
    def __init__(self, df: DataFrame):
        """
        Constructor method initializing the model with input DataFrame.
        Parameters:
            - df (DataFrame): Input DataFrame containing features and the target variable 'Rarity'.
        """
        self.name = "Random Forest Classifier"
        self.target = df["Rarity"]
        self.features = df.drop(columns=["Rarity"])
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.model = RandomForestClassifier(n_estimators=100, max_depth=20, min_samples_leaf=5,
                                            min_samples_split=2, random_state=32)
        self.model.fit(self.features, self.target)

    def __call__(self, pred_basis: DataFrame):
        """
        Callable method for making predictions on a provided DataFrame.

        Parameters:
            - pred_basis (DataFrame): DataFrame with input features for making predictions.

        Returns:
            - tuple: A tuple containing the predicted value and confidence.
        """
        probability = self.model.predict_proba(pred_basis)
        prediction = self.model.predict(pred_basis)[0]
        confidence = np.max(probability, axis=1)
        return prediction, confidence

    def save(self, filepath):
        joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        """
        Static method to load a previously saved model instance from a file using joblib.

       Parameters:
           - filepath (str): The path to the file containing the saved model.

       Returns:
           - Machine: A new instance of the Machine class loaded from the file.
       """
        return joblib.load(filepath)

    def info(self, name, timestamp):
        return f"Base Model: {self.name}<br/>Timestamp: {self.timestamp}"

