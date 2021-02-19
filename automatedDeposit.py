#this will be the script that makes automated deposits
import apiconfig as cfg
import cbpro
import json
import botclass
import sys
import schedule
from botclass import bot

#pseudocode:
#    receive amount to deposit
#    receive frequency of deposit
#    make bot object
#    make it work

#trying to use inheritance here
class automatedDeposit(bot):
    def __init__(self, frequency, amount, paymentMethodIndex):
        apiKey = cfg.api['API_KEY']
        apiSecret = cfg.api['API_SECRET']
        apiPassphrase = cfg.api['API_PASSPHRASE']
        sandbox = cfg.api['SANDBOX']
        super().__init__(apiKey, apiSecret, apiPassphrase, sandbox)
        self.frequency = frequency
        self.amount = amount
        self.paymentMethodIndex = paymentMethodIndex
        #TODO: add check here to make sure amount is > 10
        #also add a check to make sure API config file is correct
        #perhaps here is also a good place to query API and make sure the account is active and has privileges.


    def triggerDeposit(self, paymentMethodID):
        '''makes a deposit. paymentMethodID is the ID of the method, not the INDEX of all payment methods.
        Before/when this method is called, seek into the array of paymentMethods using the index given this bot, and find the [id] key pairing to get this.'''
        retStatement = self.apiClient.deposit(self.amount, 'USD', paymentMethodID)
        return retStatement


#get primary payment method ID
#paymentMethods = (myBot.apiClient.get_payment_methods())

#print(paymentMethods)
#primaryMethodID = paymentMethods[0]['id']
#print(f'primary method id is {primaryMethodID}')

#TODO: insert logic for frequency

#this does the actual deposit:
#response = myBot.apiClient.deposit(10, 'USD', primaryMethodID)
#print(response)
#TODO: save response in JSON