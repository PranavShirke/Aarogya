from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

# Create a simple dataset
# Features: [fever, cough, sore_throat, headache]
X = np.array([
    [1, 0, 0, 0],  # Fever only -> Common Cold
    [0, 1, 0, 0],  # Cough only -> Bronchitis
    [0, 0, 1, 0],  # Sore throat only -> Strep Throat
    [0, 0, 0, 1],  # Headache only -> Migraine
    [1, 1, 0, 0],  # Fever + Cough -> Flu
    [1, 0, 1, 0],  # Fever + Sore throat -> Tonsillitis
    [1, 1, 1, 0],  # Fever + Cough + Sore throat -> COVID-19
    [0, 0, 1, 1],  # Sore throat + Headache -> Sinusitis
])

y = np.array([
    'Common Cold',
    'Bronchitis',
    'Strep Throat',
    'Migraine',
    'Flu',
    'Tonsillitis',
    'COVID-19',
    'Sinusitis'
])

# Create and train the model
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

# Save the model
joblib.dump(model, 'disease_predictor.pkl')
print("Model created and saved successfully!") 