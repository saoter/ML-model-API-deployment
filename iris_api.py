import torch
import torch.nn as nn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class IrisClassifier(nn.Module):
    def __init__(self):
        super(IrisClassifier, self).__init__()
        self.fc1 = nn.Linear(4, 16)
        self.fc2 = nn.Linear(16, 3)
        self.relu = nn.ReLU()
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model_name = "models/iris_classifier_2023-03-28.pth"
model = IrisClassifier()
model.load_state_dict(torch.load(model_name))
model.eval()

class Item(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(item: Item):
    input_data = torch.tensor([item.sepal_length, item.sepal_width, item.petal_length, item.petal_width], dtype=torch.float32)

    # Make the prediction
    with torch.no_grad():
        output = model(input_data)
        predicted_class = torch.argmax(output).item()

    # Return the predicted class
    class_names = ["Setosa", "Versicolor", "Virginica"]
    return {"predicted_class": class_names[predicted_class]}
