import cbpro
import json
import apiconfig as cfg
import botclass
from automatedDeposit import automatedDepositBot
from automatedBuy import automatedBuy

print('The taxation of trade routes to outlaying star systems is in dispute.')

#get API info from config file
apiKey = cfg.api['API_KEY']
apiSecret = cfg.api['API_SECRET']
apiPassphrase =cfg.api['API_PASSPHRASE']
sandbox = cfg.api['SANDBOX']
#this is actually unnecessary, as the parent bot class does this automatically. This block can be removed, leaving now for posterity.


#make a new generic bot object ()
myBot = botclass.bot()

print(myBot)
#toString test.

myBot.purchase(5, 'BTC')
#purchase doesn't do anything, was is just a silly debug test method.

#test purchasing BTC, selling BTC
#Remember $10 minimum! Will give error and append that error to our json is not enough money to make the purchase.
myBot.marketBuy(10, 'BTC-USD')
myBot.marketBuy(10, 'BTC-USD')
myBot.marketSell(10, 'BTC-USD')
#todo: the json files for these two methods (buy and sell) have diferent formatting. Make them consistent.

#now testing automateDeposit bot, which is child of botclass bot (inherits all of its methods etc)
depositBot = automatedDepositBot(10, 10, 0)
#test get entire array of payment methods
print(depositBot.getAllPaymentMethods())
#test get chosen method's ID
myid = depositBot.getChosenPaymentMethodID()
print(myid)
#test make the deposit
print(depositBot.triggerDeposit(myid))
#This is giving a "user login required" error, unsure why
#todo look into this error! Not sure if account specific, or problem with code logic.


#testing automatedBuy bot
buybot = automatedBuy(1, 10, 'BTC-USD')
print(buybot)
print(buybot.triggerBuy())