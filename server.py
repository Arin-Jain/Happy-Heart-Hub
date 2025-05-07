from flask import Flask, request, jsonify
import joblib  
import numpy as np

app = Flask(__name__)

model = joblib.load('Gradient Boosting.pkl')

@app.route('/predict', methods=['GET'])
def predict():
    # data = request.json
    # input_data = np.array([[data['age'], data['gender'], data['height'], data['weight'], data['ap_hi'], data['ap_lo'], data['cholesterol'], data['gluc']]])
    # prob = model.predict_proba(input_data)[:, 1][0]
    # print(prob)
    # return jsonify({'probability': prob})
    age = request.args.get('age')
    gender = request.args.get('gender')
    height = request.args.get('height')
    weight = request.args.get('weight')
    ap_hi = request.args.get('ap_hi')
    ap_lo = request.args.get('ap_lo')
    cholesterol = request.args.get('cholesterol')
    gluc = request.args.get('gluc')

    # Convert parameters to the appropriate types
    input_data = np.array([[float(age), int(gender), float(height), float(weight), int(ap_hi), int(ap_lo), int(cholesterol), int(gluc)]])
    
    # Predict probability
    prob = model.predict_proba(input_data)[:, 1][0]
    print(prob)
    # Return the probability as JSON response
    return jsonify({'prediction': prob})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
