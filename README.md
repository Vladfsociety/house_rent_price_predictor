# House rent price predictor
#### This repository contains a machine learning project aimed at predicting house rent prices based on various features. The model is created and tested in a Jupyter notebook, ensuring a thorough and interactive analysis.
## Project Structure
```
house_rent_price_predictor/
├── .streamlit/
│   └── config.toml                       # Configuration file to customize Streamlit application
├── data/
│   ├── clean/                            
│   │   ├── data.csv                      # Clean dataset in .csv format
│   │   └── data.joblib                   # Serialized clean dataset for use in app
│   └── raw/
│       └── house_rent_data.csv           # Raw dataset containing house rent information
├── model/
│   └── voting.joblib                     # Serialized trained model for predicting house rent prices
├── notebooks/
│   └── house_rent_price_predictor.ipynb  # Jupyter notebook for data analysis, model training, and evaluation
├── src/
│   ├── app/                              
│   │   └── main.py                       # Main web app file
│   └── model/
│       ├── interval_voting_regressor.py  # Custom interval voting regressor model
│       └── log_scaler.py                 # Custom log scaler
├── .gitignore                            # Specifies files to be ignored by Git
├── README.md                             # Project description, installation instructions, and usage guide
├── app.py                                # Entry point for web app
├── config.json                           # Сonfig file with the paths to the dataset/model files
├── config.py                             # Script for loading dataset/model files
├── requirements.txt                      # List of dependencies required to run the project application
├── requirements_dev.txt                  # List of dependencies required to run the project for development
├── setup.py                              # Defines how to build, install, and distribute for Python project 
```
## Installation
#### To get started with the project, follow these steps:
#### 1. Clone the repository:
```
git clone https://github.com/Vladfsociety/house_rent_price_predictor.git
cd house_rent_price_predictor
```
#### 2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
#### 3. Install the required packages:
#### 3.1. For run notebook:
```
pip install -r requirements_dev.txt
```
#### 3.2. For run web app:
```
pip install -r requirements.txt
```
#### 4. Install the project in editable mode:
```
pip install -e .
```
## Usage
#### 1. Run the Jupyter notebook:
```
jupyter lab
```
#### 2. Run the Streamlit app:
```
streamlit run app.py
```
## Ending Work
```
deactivate # On Windows, use `venv\Scripts\deactivate`
```
