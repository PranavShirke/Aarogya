import sys
import json

# Comprehensive disease prediction rules with more symptoms
DISEASE_RULES = {
    # Single symptoms
    'fever': 'Common Cold',
    'cough': 'Bronchitis',
    'sore_throat': 'Strep Throat',
    'headache': 'Migraine',
    'fatigue': 'Anemia',
    'nausea': 'Gastritis',
    'dizziness': 'Vertigo',
    'rash': 'Allergic Reaction',
    'muscle_pain': 'Fibromyalgia',
    'shortness_of_breath': 'Asthma',
    
    # Two symptoms
    'fever,cough': 'Flu',
    'fever,sore_throat': 'Tonsillitis',
    'fever,headache': 'Viral Infection',
    'fever,fatigue': 'Mononucleosis',
    'fever,rash': 'Measles',
    'cough,sore_throat': 'Bronchitis',
    'cough,headache': 'Sinus Infection',
    'cough,shortness_of_breath': 'Pneumonia',
    'sore_throat,headache': 'Sinusitis',
    'nausea,fatigue': 'Food Poisoning',
    'dizziness,nausea': 'Motion Sickness',
    'rash,itching': 'Contact Dermatitis',
    
    # Three symptoms
    'fever,cough,sore_throat': 'COVID-19',
    'fever,cough,headache': 'Influenza',
    'fever,sore_throat,headache': 'Tonsillitis',
    'fever,fatigue,headache': 'Viral Meningitis',
    'fever,rash,headache': 'Chickenpox',
    'cough,shortness_of_breath,fatigue': 'Chronic Bronchitis',
    'nausea,vomiting,fatigue': 'Gastroenteritis',
    'dizziness,nausea,headache': 'Migraine',
    'rash,itching,fever': 'Allergic Reaction',
    'muscle_pain,fatigue,headache': 'Fibromyalgia',
    
    # Four symptoms
    'fever,cough,sore_throat,headache': 'Severe Viral Infection',
    'fever,cough,shortness_of_breath,fatigue': 'Pneumonia',
    'fever,rash,headache,muscle_pain': 'Dengue Fever',
    'nausea,vomiting,fatigue,dizziness': 'Food Poisoning',
    'rash,itching,fever,headache': 'Allergic Reaction',
    
    # Five or more symptoms
    'fever,cough,sore_throat,headache,fatigue': 'Severe Viral Infection',
    'fever,cough,shortness_of_breath,fatigue,muscle_pain': 'Pneumonia',
    'fever,rash,headache,muscle_pain,nausea': 'Dengue Fever'
}

# Additional symptom combinations with probabilities
SYMPTOM_PROBABILITIES = {
    'fever': {
        'Common Cold': 0.6,
        'Flu': 0.2,
        'Viral Infection': 0.2
    },
    'cough': {
        'Bronchitis': 0.5,
        'Flu': 0.3,
        'COVID-19': 0.2
    },
    'sore_throat': {
        'Strep Throat': 0.4,
        'Tonsillitis': 0.3,
        'Viral Infection': 0.3
    },
    'headache': {
        'Migraine': 0.4,
        'Sinusitis': 0.3,
        'Viral Infection': 0.3
    },
    'fatigue': {
        'Anemia': 0.4,
        'Viral Infection': 0.3,
        'Chronic Fatigue': 0.3
    },
    'nausea': {
        'Gastritis': 0.4,
        'Food Poisoning': 0.3,
        'Viral Infection': 0.3
    },
    'dizziness': {
        'Vertigo': 0.5,
        'Migraine': 0.3,
        'Anemia': 0.2
    },
    'rash': {
        'Allergic Reaction': 0.5,
        'Contact Dermatitis': 0.3,
        'Viral Infection': 0.2
    },
    'muscle_pain': {
        'Fibromyalgia': 0.4,
        'Viral Infection': 0.3,
        'Flu': 0.3
    },
    'shortness_of_breath': {
        'Asthma': 0.5,
        'Bronchitis': 0.3,
        'Pneumonia': 0.2
    }
}

def predict_disease(symptoms):
    if not symptoms:  # If no symptoms are selected
        return "Please select at least one symptom"
        
    # Sort symptoms to ensure consistent key lookup
    symptoms_key = ','.join(sorted(symptoms))
    
    # Try to find exact match first
    if symptoms_key in DISEASE_RULES:
        return DISEASE_RULES[symptoms_key]
    
    # If no exact match, try to find the closest match
    # This handles cases where we have a subset of symptoms
    for key in DISEASE_RULES:
        key_symptoms = set(key.split(','))
        if all(symptom in key_symptoms for symptom in symptoms):
            return DISEASE_RULES[key]
    
    # If still no match, use probability-based prediction
    if len(symptoms) == 1:
        symptom = symptoms[0]
        if symptom in SYMPTOM_PROBABILITIES:
            # Get the most probable disease for the single symptom
            return max(SYMPTOM_PROBABILITIES[symptom].items(), key=lambda x: x[1])[0]
    
    return "Unknown combination of symptoms"

if __name__ == "__main__":
    try:
        input_json = sys.argv[1]
        input_data = json.loads(input_json)
        symptoms = input_data['symptoms']
        
        prediction = predict_disease(symptoms)
        print(prediction)
    except Exception as e:
        print(f"Error processing input: {str(e)}", file=sys.stderr)
        sys.exit(1)
