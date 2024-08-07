from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import joblib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

def send_email(to_email, subject, message):
    # Mock function to simulate email sending
    print(f"Sending email to {to_email}\nSubject: {subject}\nMessage: {message}")

@app.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already registered'}), 400

    new_user = User(email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@app.route('/predict', methods=['POST'])
def predict():
    weather_data = request.json['weather_data']
    model = joblib.load('rain_model.pkl')
    prediction = model.predict([weather_data])

    if prediction[0] == 1:  # Assuming 1 indicates rain
        users = User.query.all()
        for user in users:
            send_email(user.email, 'Rain Alert', 'Rain is predicted. Stay safe!')
    return jsonify({'message': 'Prediction complete, alerts sent if rain is predicted'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
