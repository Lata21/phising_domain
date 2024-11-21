import streamlit as st
import requests

# Set title and description
st.title("Link Safety Prediction")

# Input fields
url = st.text_input("Enter URL:")
domain = st.text_input("Enter Domain:")
page_content = st.text_area("Enter Page Content:")

# Button to trigger prediction
if st.button("Check Safety"):
    if url and domain and page_content:
        # Print the data to be sent for debugging purposes
        st.write(f"Sending data: URL: {url}, Domain: {domain}, Page Content: {page_content[:100]}...")  # Show the first 100 chars

        # Prepare the data to send to FastAPI for prediction
        input_data = {
            "url": url,
            "domain": domain,
            "page_content": page_content
        }

        # FastAPI endpoint URL (adjust as needed)
        api_url = "http://127.0.0.1:8000/predict/"  # Ensure FastAPI is running at this address
        
        try:
            # Send the data to FastAPI
            response = requests.post(api_url, json=input_data)
            response.raise_for_status()  # Ensure we get a successful response
            
            # Parse the response JSON
            data = response.json()

            # Display the prediction
            st.success(f"The URL is: **{data['prediction']}**")
        except requests.exceptions.HTTPError as errh:
            st.error(f"HTTP error occurred: {errh}")
        except requests.exceptions.RequestException as err:
            st.error(f"Error during prediction: {err}")
    else:
        st.warning("Please fill in all the fields.")

# Footer with additional info, centered
st.write("---")
st.markdown("<h5 style='text-align: center;'>Developed by Lata Bharti | AI/ML Enthusiast</h5>", unsafe_allow_html=True)
