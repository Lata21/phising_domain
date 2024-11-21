from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Define the input schema
class LinkInput(BaseModel):
    url: str
    domain: str
    page_content: str

# Simulated prediction function (dummy model)
def dummy_predict(features):
    # Check for HTTPS link, which we assume to be safe
    if features[2] == 1:  # If the URL starts with https://
        return "safe"
    else:
        # Anything else is considered unsafe for simplicity
        return "unsafe"

# Feature extraction function (simplified)
def extract_features(url: str, domain: str, page_content: str):
    features = []
    features.append(len(url))  # Length of the URL
    features.append(len(domain))  # Length of the domain name
    features.append(1 if url.startswith("https://") else 0)  # Whether the URL starts with https
    features.append(page_content.count("keyword"))  # Count of a keyword in the page content

    # Fill up to 31 features if needed (though we're using only 4 for now)
    while len(features) < 31:
        features.append(0)

    return features

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "API is up and running!"}

# Prediction endpoint
@app.post("/predict/")
def predict_link(input_data: LinkInput):
    try:
        # Extract features from the input
        features = extract_features(input_data.url, input_data.domain, input_data.page_content)
        
        # Make a prediction using the dummy model
        prediction = dummy_predict(features)

        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
