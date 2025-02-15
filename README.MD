## 🛫 AI Travel Agent
This Streamlit app is an AI-powered Airline Guide that helps to get useful information about travel in a quick and concise manner.

### Features
- Get baggage information across airlines worldwide for both domestic and international.
- Provide transit information at various cities for different Nationality/Passports.
- Find the terminal for a given Airline at an airport for domestic and international travel.

### How to get Started?

1. Clone the GitHub repository

```bash
git clone https://github.com/Princejain1101/AirGuide.git
```
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```
3. Create a folder for your secret APIs
```bash 
mkdir .streamlit
touch .streamlit/secrets.toml
```
4. Setup your OpenAI API Key 

- Sign up for an [OpenAI account](https://platform.openai.com/) and obtain your API key.
- Get your OpenAI API key
- set this api key in .streamlit/secrets.toml as below
openai_api_key = "<openai_api_key>"

5. Setup your SerpAPI Key

- Sign up for an [SerpAPI account](https://serpapi.com/) and obtain your API key.
- Get your Serp API key
- set this api key in .streamlit/secrets.toml as below
serp_api_key = "<serp_api_key>"

6. Run the Streamlit App
```bash
streamlit run air_guide.py
```
- You should see a local URL in your terminal. 
- e.g. "https://localhost:8501"
- This local URL should open automatically or click on it to open.