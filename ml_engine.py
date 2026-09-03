import numpy as np
from sklearn.ensemble import IsolationForest

# 1. This function creates our AI brain (the model)
def create_model():
    # We use IsolationForest to detect strange, non-human behaviors
    model = IsolationForest(contamination=0.05, random_state=42)
    return model

# 2. Let's create some "Normal Human" behavior data to train our AI brain
# Columns: [typing_speed, mouse_speed, backspace_error_rate]
normal_behavior_samples = np.array([
    [120.0, 450.0, 0.05], # Human 1: Moderate typing, moderate mouse, 5% errors
    [140.0, 600.0, 0.08], # Human 2
    [95.0,  300.0, 0.02], # Human 3
    [110.0, 510.0, 0.04], # Human 4
    [130.0, 420.0, 0.06], # Human 5
])

# 3. Train our model to recognize normal humans
ai_brain = create_model()
ai_brain.fit(normal_behavior_samples)

# 4. This function will check incoming transactions
def analyze_biometrics(typing_speed, mouse_speed, error_rate):
    # Prepare the data for the AI brain to inspect
    input_data = np.array([[typing_speed, mouse_speed, error_rate]])
    
    # Ask the AI brain if this looks normal (returns 1 for normal, -1 for anomaly)
    prediction = ai_brain.predict(input_data)
    
    # If the AI says -1, it means it isolated a strange, robotic-like behavior!
    if prediction == -1:
        return {"risk_score": 0.85, "status": "SUSPICIOUS_BOT"}
    else:
        return {"risk_score": 0.10, "status": "SAFE_HUMAN"}