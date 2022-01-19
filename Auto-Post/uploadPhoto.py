from InstagramAPI import InstagramAPI
from apscheduler.schedulers.blocking import BlockingScheduler
import os, os.path
import random

InstagramAPI = InstagramAPI("", "")
InstagramAPI.login()

def post():
    image = random.randint(1, len([name for name in os.listdir('.') if os.path.isfile(name)]))
    photoPath = '/Users/harveyallen/Documents/Programming/socialNetwork/instagramBot/autoPost/images/' + str(image) + '.jpg'
    print(photoPath)
    caption = "Sample"
    InstagramAPI.uploadPhoto(photoPath, caption=caption)


post()
scheduler = BlockingScheduler()
scheduler.add_job(post, 'interval', hours=1)
scheduler.start()
