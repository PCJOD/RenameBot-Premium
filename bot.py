import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6524778568:AAGRqtl0eSdZtBZir_lh3zfPxeg4FCP2naw")

API_ID = int(os.environ.get("API_ID", "24482734"))

API_HASH = os.environ.get("API_HASH", "5ccf6a58166cc047a7eba01c5dbc930c")

STRING = os.environ.get("STRING", "BQF1k64AO3ivGgmxjSvpqbMlEVM8xdaMsUH0iu9ycutVIlYw6gliup1wY8Ib_q_x3Knp9Um5pFrDC4-RWKDTsbh0aDU8oIEwRM8fwsyLl-dvtc6mNl6Wf3C4hCRxyVnHjvK4BwLI8rQHX5CKaA7NdQ0KQAiIVU0setmMkgc-0iGFnUE4Dr_rAdHdrC9Gv90OYcJIi25ewIXTCbJmTlkIdSv3tRQlHPkp_YFdyk2ciSwNVXQWEP6RI8BxAuDHWYjN8Nq1muWKa3f06UvlBAB8sHy_M0nAdy__SQGjN2N3XHq0Rii-9UgMMEo5nalb2O8g-Bx4xyCstnCLoo59PVrEC0kxJsEJbwAAAABqvRGtAA")


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
