import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib


data = [

    # Good supersets
    ["chest", "back", 1],
    ["biceps", "triceps", 1],
    ["quads", "hamstrings", 1],
    ["shoulders", "back", 1],
    ["chest", "biceps", 1],
    ["hamstrings", "glute", 1],

    # Bad supersets
    ["chest", "chest", 0],
    ["back", "back", 0],
    ["biceps", "biceps", 0],
    ["triceps", "triceps", 0],
]

df = pd.DataFrame(data, columns=["muscle1", "muscle2", "compatible"])


encoder = LabelEncoder()

all_muscles = pd.concat([df["muscle1"], df["muscle2"]])
encoder.fit(all_muscles)

df["muscle1"] = encoder.transform(df["muscle1"])
df["muscle2"] = encoder.transform(df["muscle2"])


X = df[["muscle1", "muscle2"]]
y = df["compatible"]

model = DecisionTreeClassifier(max_depth=4)
model.fit(X, y)

joblib.dump(model, "superset_model.pkl")
joblib.dump(encoder, "muscle_encoder.pkl")

print("Superset model trained.")
