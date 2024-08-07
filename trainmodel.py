import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Example data: Replace this with your actual weather data
data = {
    'feature1': [0.1, 0.2, 0.3, 0.4],
    'feature2': [1, 2, 3, 4],
    'feature3': [10, 20, 30, 40],
    'rain': [0, 1, 0, 1]
}
df = pd.DataFrame(data)

X = df[['feature1', 'feature2', 'feature3']]
y = df['rain']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

joblib.dump(model, 'rain_model.pkl')
