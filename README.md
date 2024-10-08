# Twitter AI Generated Content


### Overview
This Python application generates a daily poem based on a top headline from the New York Times. Google Gemini will check if a headline relates to sensitive topics (war, death, etc.). If a headline pertains to a sensitive topic, the application will find another headline. Google Gemini will then generate the poem and the application will post the poem to a specified [Twitter account](https://x.com/JunaidAlam39918).


### Features
* Headline Retrieval: Fetches the top headline from the New York Times API.
* Poem Generation: Uses the Google Gemini API to create a poem based on the headline.
* Twitter Posting: Automatically posts the generated poem to the designated [Twitter account](https://x.com/JunaidAlam39918).
* Scheduled Execution: Runs daily at 9 AM via GitHub Actions.


### Prerequisites
* Python: Ensure you have Python 3.6 or later installed.
* Libraries: Install the required libraries using pip:

```
Bash
pip install -q -U google-generativeai
pip install -U python-dotenv
pip install tweepy

```


* Twitter API Credentials: You'll need your Twitter developer account credentials (consumer key, consumer secret, access token, access token secret) to authenticate with the Twitter API.
* Google Gemini API Credentials: You'll need to obtain Google AI for Developers account to obtain a key.
* New York Times API Credentials: You'll need to obtain a New York Times Developer account to obtain a key.
* GitHub Actions: Set up a GitHub Actions workflow to trigger the application daily (or whatever times and frequency you decide).


### Configuration

1. **Create a ```.env``` file:** Store your API keys and Twitter credentials securely in a .env file. 


2. **Load environment variables:** In your Python code, use a library like dotenv to load the environment variables from the .env file.


### Usage
1. **Run the script:** Execute the Python script to generate and post the poem.
2. **GitHub Actions:** Configure your GitHub Actions workflow to run the script daily at 9 AM (or whatever times and frequency you decide).

### Customization
* **Headline Source:** Modify the code to fetch headlines from a different news source.
* **Poem Generation:** Experiment with different prompts or parameters in the Google Gemini API to customize the poem's style or content.
* **Twitter Posting:** Customize the tweet message or add additional features like media attachments.


### Author
- [@junaidalam2](https://github.com/junaidalam2)
