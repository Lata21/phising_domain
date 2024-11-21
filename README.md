
# Link Safety Prediction

This project is an end-to-end application to predict the safety of URLs using a machine learning approach. It consists of a **FastAPI backend** and a **Streamlit frontend** for user interaction. 

## Features

- **FastAPI Backend**: Accepts user input, processes the data, and returns predictions on URL safety.
- **Streamlit Frontend**: A user-friendly interface to enter details and view predictions.
- **Feature Extraction**: Simplified feature engineering for demonstration purposes.
- **Prediction Model**: A placeholder dummy model for predicting URL safety.

---

## Project Structure

```
.
├── app.py         # FastAPI backend
├── main.py        # Streamlit frontend
├── model.ipynb    # Jupyter Notebook for EDA and model training
```

---

## How to Run the Project

### Prerequisites
- Python 3.7 or above
- Dependencies listed in `requirements.txt` (to be created if not available)

### Steps

1. **Clone the repository**:
   ```bash
   git clone <repository-link>
   cd <repository-folder>
   ```

2. **Install Dependencies**:
   Install the necessary Python libraries.
   ```bash
   pip install fastapi pydantic uvicorn streamlit requests
   ```

3. **Start FastAPI Server**:
   ```bash
   uvicorn app:app --reload
   ```
   The backend will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

4. **Run Streamlit Frontend**:
   In a new terminal, run:
   ```bash
   streamlit run main.py
   ```
   Access the application at [http://localhost:8501](http://localhost:8501).

---

## Usage

1. Launch the Streamlit app.
2. Fill in the following fields:
   - **URL**: Enter the URL to check.
   - **Domain**: Enter the domain name of the URL.
   - **Page Content**: Provide a sample or actual content of the page.
3. Click **"Check Safety"** to predict whether the link is safe or unsafe.

---

## File Descriptions

### `app.py`
- Implements the FastAPI backend.
- Provides endpoints for health check (`GET /`) and link safety prediction (`POST /predict/`).
- Extracts features and uses a dummy prediction model.

### `main.py`
- Implements the Streamlit frontend.
- Sends user input to the FastAPI server and displays the prediction results.

### `model.ipynb`
- Includes exploratory data analysis (EDA) and training code for the Random Forest model.
- Saves the trained model (`Random Forest.pkl`) for use in production.

---

## Improvements to Consider
- Replace the dummy model with the trained Random Forest model.
- Enhance feature extraction with more URL-based, domain-based, and content-based features.
- Add error handling for edge cases.
