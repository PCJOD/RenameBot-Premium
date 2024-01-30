import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6883869171:AAFKSTOs8f0IKiQUfeXkolYLp9dbdzj6E9g")

API_ID = int(os.environ.get("API_ID", "21136840"))

API_HASH = os.environ.get("API_HASH", "0f2ff6ef89fcd5ba226c3f40342f5319")

STRING = os.environ.get("STRING", "BQFChcgAEsF7salxJ3dYPlsweQ6Z2JymV67rqNmvb2_R167VgMzXs_Q7vsnfbJC1HbvxFegK5GGuX-RtDjcdRDMKYTwF5edSsw18T_6VQ2IjPG-qbVHo6we9bDjcfEU-Ahvc_2v_ZCGR-Wq2n4dfJTrUk2FVB07Po8eS3xXpXD_O990Kv1h9wIRAe_dUTZZsFnVTisxHODva-3EsOvgtuWpF3ZizRt-FS2W53j6Sc27UDtmDzn_StA527ggio-KBzgzewu7C5qZxe_9IHh0gec2VOxnP0ka-sv0WI1DDXty_fyxyJlM8fs-aKGFGiY3o3DoO2sYbypb_Xp0WdcloqEaQgBnhvQAAAAGbK2N3AQ")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
