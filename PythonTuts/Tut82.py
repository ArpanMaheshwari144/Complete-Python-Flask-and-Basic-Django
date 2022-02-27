# install win32com->pip install pywin32

# import requests
# import json
#
# def speak(str):
#     from win32com.client import Dispatch
#     speak=Dispatch("SAPI.spVoice")
#     speak.Speak(str)
#
# if __name__ == '__main__':
#     speak("Arpan Listen News For Today...Let's Begin")
#     url = ("http://newsapi.org/v2/top-headlines?country=us&apiKey=b39b1225f3f54d47a1dd2aa4cdb58087")
#
#     news = requests.get(url).text
#     news_dict = json.loads(news)   #json.loads() json object ko python object mei change kar deta hai
#     arts=news_dict['articles']
#     for article in arts:
#         speak(article['title'])
#         print(article['title'])
#         print(article['url'])
#         speak("Moving to the next news...Listen Carefully Arpan Maheshwari")
#     speak("Thanks for listening....")

import requests
import json
from win32com.client import Dispatch
def speak(string):
    speak=Dispatch('SAPI.spVoice')
    speak.speak(string)

speak("Good Morning Arpan!Hope you enjoy your morning tea")
speak("lets Begin Our News Session")
url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=b39b1225f3f54d47a1dd2aa4cdb58087')
data=requests.get(url=url)
india=data.json()
print(india['articles'][0]['description'])
speak("What would you like to listen I have these top newspapers hope you like these Newspapers")
for i in range(20):
    print(i,india['articles'][i]['source']['name'])

no=int(input("choose newspaper number: "))
speak(india['articles'][no]['title'])
print("for more ",india['articles'][no]['url'])
speak(india['articles'][no]['content'])
speak(india['articles'][no]['description'])
speak("Hope you like these news")
speak("Stay Updated")
speak("Enjoy your Day")