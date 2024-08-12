import google.generativeai as genai
import os
import requests
import tweepy

from utils import *
from dotenv import load_dotenv
load_dotenv() 

key_nytimes = os.getenv("key_nytimes")

GOOGLE_API_KEY = os.getenv("google_api_key")
if not GOOGLE_API_KEY:
    raise ValueError("google_api_key environment variable is not set.")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

client = tweepy.Client(
    consumer_key=os.getenv("consumer_key"), consumer_secret=os.getenv("consumer_secret"),
    access_token=os.getenv("access_token"), access_token_secret=os.getenv("access_token_secret")
)


def post_twitter(posts_gemini, headline):
    intro = f'Poem based on NY Times headline: {headline}'
    text = f'{intro}\n{posts_gemini}'
    client.create_tweet(text=text)


def get_posts_gemini(headline):
    
    word_limit = TWITTER_CHARACTER_LIMIT - len(headline) - BUFFER_TWITTER_CHAR_LIMIT

    try:
        response = model.generate_content(f'Create a rhyme no longer than {word_limit} characters based on the following newspaper headline: {headline}')
        return response.candidates[0].content.parts[0].text
    
    except requests.exceptions.RequestException as e:
    
            print(f'Error - Gemini: ', {e})
            return None


def get_posts_news():
    url = 'https://api.nytimes.com/svc/topstories/v2/home.json?api-key='

    try:
        response = requests.get(url + key_nytimes)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error - Newspaper API:', response.status_code)
            return None
    
    except requests.exceptions.RequestException as e:
  
        print('Error - Newspaper API:', e)
        return None


def check_against_sensitive_words(posts_news):
    
    for article in posts_news['results']:
        try:
                response = model.generate_content(f"Here is a list of sensitive topics: {SENSITIVE_WORD_ARRAY}. Does the following text includes such topics? {article['abstract']}. Please reply with only either 'Yes' or 'No'")
                if(response.candidates[0].content.parts[0].text[:-2] == 'No'):
                    return article['title']
            
        except requests.exceptions.RequestException as e:
        
                print(f'Error - Gemini: ', {e})
                return None
         

def main():

    posts_news = get_posts_news()
    if posts_news:

        #title = posts_news['results'][0]['title']
        #abstract = posts_news['results'][0]['abstract']
        #url = posts_news['results'][0]['url']
        headline = check_against_sensitive_words(posts_news)
    
        if headline:
            posts_gemini = get_posts_gemini(headline)
            if posts_gemini:
                
    
                print(posts_gemini)
                post_twitter(posts_gemini, headline)

            else:
                print('Failed to fetch posts from gemini API.')

        else:
            print('Failed to obtain headline that does not meet sensitivity requirements.')

    else:
        print('Failed to fetch posts from news API.')
  
 
if __name__ == '__main__':
    main()