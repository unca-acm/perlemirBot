#Automated Buys

import apiconfig as cfg
import cbpro
import json
import botclass
import sys
import schedule
from botclass import bot


#pseudocode
#    receive asset to buy (ETH/BTC/Other)
#    receive amount in USD to purchase
#    Buys have $10 minimum so make sure amount is >$10 (or perhaps write logic in to batch until reaches $10 minimum)
#    receive frequency to make purchase
#    create bot  (inherit bot from botclass?)
#    make the buys on set schedule
#    Record information about transaction into a JSON - either just the transaction ID, or more info (entire return statement) - TBD

#trying to use the same inheritance as automatedDeposit to keep things consistent
class automatedBuy(bot):
    def __init__(self, frequency, amount):
        apiKey = cfg.api['API_KEY']
        apiSecret = cfg.api['API_SECRET']
        apiPassphrase = cfg.api['API_PASSPHRASE']
        sandbox = cfg.api['SANDBOX']
        super().__init__(apiKey, apiSecret, apiPassphrase, sandbox)
        self.frequency = frequency
        self.amount = amount


myBot = automatedBuy(10,10)     #creating bot
print(myBot)
payment_methods = bot.apiClient.get_payment_methods()   #should get the account to buy with (API documentation)
account = bot.apiClient.get_primary_account()
payment_method = client.get_payment_methods()[0]


def job():          #the function of doing one buy BTC (got from api documentation)
    buy = account.buy(amount=bot.amount,
                    currency="BTC",
                    payment_method=payment_method.id)


schedule.every(bot.frequency).days.do(job) #setting the schedule to run at set frequency
while True:                                 #running the bot
    schedule.run_pending()
    time.sleep(1)
