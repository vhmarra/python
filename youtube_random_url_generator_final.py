import json
import urllib.request
import string
from selenium import webdriver #pip install selenium
import time


count = 1
API_KEY = 'YOUR KEY' #put your api key here
random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,random)
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
results = json.loads(data.decode(encoding))

for data in results['items']:
     videoId = (data['id']['videoId'])

last_part_url = (data['id']['videoId']) #11 digits base64 video ID
    
class bot_video_youtube():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=self.options)
        url = ("https://www.youtube.com/watch?v="+str(last_part_url))
        print("video url: ",url)
        print("video base64 id: ",last_part_url)
        self.driver.get(url)
 
class save_generate_link():
     def __init__(self):
          self.arquivo = open('generateurls.txt', 'a')
          self.arquivo.write(full_url + "\n")
          self.arquivo.close()

gerar = save_generate_link()
bot = bot_video_youtube()

