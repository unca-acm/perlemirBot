#this will be the script that makes automated deposits
import apiconfig as cfg
import cbpro
import json
import botclass
import sys
import schedule

#USAGE: automatedDeposit.py USDamount Frequency

#pseudocode:
#    receive amount to deposit
#    receive frequency of deposit
#    make bot object
#    make it work

#trying to use inheritance here
class automatedDeposit(botclass):
    def __init__(self, frequency, amount):
        apiKey = cfg.api['API_KEY']
        apiSecret = cfg.api['API_SECRET']
        apiPassphrase = cfg.api['API_PASSPHRASE']
        sandbox = cfg.api['SANDBOX']
        super().init(apiKey, apiSecret, apiPassphrase, sandbox)
        self.frequency = frequency
        self.amount=amount
        #TODO: add check here to make sure amount is > 10


#get API info from config file
apiKey = cfg.api['API_KEY']
apiSecret = cfg.api['API_SECRET']
apiPassphrase =cfg.api['API_PASSPHRASE']
sandbox = cfg.api['SANDBOX']

#make a new bot object
myBot = botclass.bot(apiKey, apiSecret, apiPassphrase, sandbox)
print(myBot)

#get primary payment method ID
paymentMethods = (myBot.apiClient.get_payment_methods())
#print(paymentMethods)
primaryMethodID = paymentMethods[0]['id']
print(f'primary method id is {primaryMethodID}')

#TODO: insert logic for frequency

#this does the actual deposit:
response = myBot.apiClient.deposit(amount, 'USD', primaryMethodID)
print(response)
#TODO: save response in JSON