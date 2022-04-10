from fbchat import Client, log, _graphql
from fbchat.models import *
import json
import random
import requests
import os
import concurrent.futures
from difflib import SequenceMatcher, get_close_matches
# selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
options = Options()
c = DesiredCapabilities.CHROME
c["pageLoadStrategy"] = "none"
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-sh-usage")


driver = webdriver.Chrome(
    service=Service(os.environ.get("CHROMEDRIVER_PATH")),
    options=options, desired_capabilities=c)


class ChatBot(Client):

    def onMessage(self, mid=None, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        try:
            msg = str(message_object).split(",")[15][14:-1]
            if ("//video.xx.fbcdn" in msg):
                msg = msg
            else:
                msg = str(message_object).split(",")[19][20:-1]
        except:
            try:
                msg = (message_object.text).lower()
            except:
                pass

        def sendMsg():
            if (author_id != self.uid):
                self.send(Message(text=reply ,mentions=[Mention(thread_id, offset=0, length=3)]), thread_id=thread_id,
                          thread_type=thread_type)
                   

#responses
        try:
            if("hello" in msg):
                reply = "hello world /"
                sendMsg()
            elif("help" in msg):
                reply = "Sure! What should I do?"
                sendMsg()
            elif (msg == "hi"):
                reply = "Hi ! How can I help you?"
                sendMsg()
            

        except:
            pass

        self.markAsDelivered(author_id, thread_id)




#cookies for facebook login session
cookies = {
    "sb": "",
    "fr": "",
    "c_user": "",
    "datr": "",
    "xs": ""
}


client = ChatBot("",
                 "", session_cookies=cookies)
print(client.isLoggedIn())

try:
    client.listen()
except:
    time.sleep(3)
    client.listen()
