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
class automatedDepositBot(bot):
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

    def setAmount(self, newAmount):
        '''setter for automated deposit amount'''
        self.amount =newAmount
        #todo: add check to make sure amount is > 10

    def getAmount(self):
        '''getter for automated deposit amount'''
        return self.amount

    def setFrequency(self, newFrequency):
        '''setter for automated deposit frequency'''
        self.frequency = newFrequency

    def getFrequency(self):
        '''getter for automated deposit amount'''
        return self.frequency

    def getAmount(self):
        '''getter for automated deposit amount'''
        return self.amount

    def getPaymentMethod(self):
        '''getter for payment method. The paymentMethod variable is the INDEX of the entire array of possible payment methods on the account.'''
        '''to get the actual info for this payment method, you need to call: self.getAllPaymentMethods()[self.paymentMethodIndex]'''
        return self.paymentMethodIndex

    def setPaymentMethod(self, newPaymentMethodIndex):
        '''setter for payment method. The paymentMethod variable is the INDEX of the entire array of possible payment methods on the account.'''
        self.paymentMethodIndex = newPaymentMethodIndex

    def triggerDeposit(self, paymentMethodID):
        '''makes a deposit. paymentMethodID is the ID of the method, not the INDEX of all payment methods.'''
        #Before/when this method is called, seek into the array of paymentMethods using the index given this bot, and find the [id] key pairing to get this.
        paymentMethodID = self.getAllPaymentMethods()[self.paymentMethodIndex]['id']
        #this line of code needs to be tested,

        retStatement = self.apiClient.deposit(self.amount, 'USD', paymentMethodID)
        #todo: record the return into a json
        return retStatement

    def run(self):
        while self.isActive:
            print(f"Automated Deposit Bot sequence initiated. Will deposit {self.amount} USD every {self.frequency} days")
            schedule.every(self.frequency).days.do(self.triggerDeposit)

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