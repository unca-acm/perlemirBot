import apiconfig as cfg
import cbpro
import json
import sys
import schedule
import botclass
from botclass import bot


newBot = botclass.bot()
pay= newBot.getAllPaymentMethods()
print(pay[1]['id'])
