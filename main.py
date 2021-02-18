import cbpro
import json
import apiconfig as cfg
import botclass
from automatedDeposit import automatedDeposit

print('The taxation of trade routes to outlaying star systems is in dispute.')

#get API info from config file
apiKey = cfg.api['API_KEY']
apiSecret = cfg.api['API_SECRET']
apiPassphrase =cfg.api['API_PASSPHRASE']
sandbox = cfg.api['SANDBOX']

#make a new bot object ()
myBot = botclass.bot(apiKey, apiSecret, apiPassphrase, sandbox)
myBot.purchase(5, 'BTC')
print(myBot)
myBot.marketBuy(10, 'BTC-USD')
#For testing: this will give an error because $5 is the minimum order. That error will be appended to the marketBuys.json file.

#print(formerDetails["id"])


depositBot = automatedDeposit(10, 10)
depositBot.getApikey()