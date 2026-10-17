# Weather-Based Crop Recommendation System

A simple beginner-friendly AI training mini project built with Python and Streamlit.

## Features
- Inputs: temperature, humidity, expected rainfall, and soil type
- Gives a crop suggestion with a short explanation
- Simple rule-based recommendation logic
- Runs locally in a browser

## Requirements
- Python 3.9 or newer
- Internet connection for the first-time installation of Streamlit

## How to run on Windows
1. Extract this ZIP folder.
2. Open the extracted folder in VS Code.
3. Open Terminal in VS Code.
4. Install the required library:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:

   ```bash
   streamlit run app.py
   ```

6. A browser tab should open. If it does not, copy the local URL shown in the terminal (usually `http://localhost:8501`) into your browser.

## How it works
The app compares user-entered weather and soil values against a few illustrative rules in `recommend_crop()`. For example, warm conditions with high rainfall and clayey/loamy soil may suggest rice.

## Important limitation
This is a rule-based educational prototype, not a trained ML model and not an agronomic advisory tool. Crop suitability depends on location, season, soil pH and nutrients, irrigation, seed variety, pests, and local crop calendars. Validate recommendations with local agricultural experts before making real farming decisions.

## Possible future improvement
Use a verified crop dataset and train a classification model such as Decision Tree or Random Forest, then evaluate it on held-out data.
