import joblib

model = joblib.load("superset_model.pkl")
encoder = joblib.load("muscle_encoder.pkl")


def ml_should_superset(ex1, ex2):

    try:
        m1 = encoder.transform([ex1["primary"]])[0]
        m2 = encoder.transform([ex2["primary"]])[0]

        prediction = model.predict([[m1, m2]])[0]

        return prediction == 1

    except:
        return False
