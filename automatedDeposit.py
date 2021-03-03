#this will be the script that makes automated deposits

#todo remove unnecessary imports?
import apiconfig as cfg
import cbpro
import json
import botclass
import sys
import schedule
from botclass import bot

#automatedDeposit is a child class, inherits 'bot' methods.
class automatedDepositBot(bot):
    def __init__(self, dayOfWeek, amount, paymentMethodIndex):
        super().__init__()
        self.dayOfWeek = dayOfWeek
        # days of week are enumerated, 0-6, Sun - Sat, Respectively
        self.amount = amount
        self.paymentMethodIndex = paymentMethodIndex
        #TODO: add check here to make sure amount is > 10
        #todo: perhaps add check to make sure this API key has deposit privileges
        #todo: amount needs to be >$10, add check here?

    def setAmount(self, newAmount):
        '''setter for automated deposit amount'''
        self.amount =newAmount
        #todo: add check to make sure amount is > 10

    def getAmount(self):
        '''getter for automated deposit amount'''
        return self.amount

    def setDayOfWeek(self, newDay):
        '''setter for automated deposit frequency'''
        self.dayOfWeek = newDay

    def getDayOfWeek(self):
        '''getter for automated deposit amount'''
        return self.dayOfWeek

    def getAmount(self):
        '''getter for automated deposit amount'''
        return self.amount

    def getPaymentMethodIndex(self):
        '''getter for payment method. The paymentMethod variable is the INDEX of the entire array of possible payment methods on the account.'''
        '''to get the actual info for this payment method, you need to call: self.getAllPaymentMethods()[self.paymentMethodIndex]'''
        return self.paymentMethodIndex

    def setPaymentMethodIndex(self, newPaymentMethodIndex):
        '''setter for payment method. The paymentMethod variable is the INDEX of the entire array of possible payment methods on the account.'''
        self.paymentMethodIndex = newPaymentMethodIndex

    def getChosenPaymentMethodID(self):
        'returns chosen payment method ID'
        allMethods = self.getAllPaymentMethods
        objectMethods = allMethods()
        return objectMethods[self.paymentMethodIndex]['id']

    def triggerDeposit(self, paymentMethodID):
        '''makes a deposit. paymentMethodID is the ID of the method, not the INDEX of all payment methods.'''
        #Before/when this method is called, seek into the array of paymentMethods using the index given this bot, and find the [id] key pairing to get this.
        paymentMethodID = self.getAllPaymentMethods()[self.paymentMethodIndex]['id']
        retStatement = self.apiClient.deposit(self.amount, 'USD', paymentMethodID)
        #todo: record the return into a json
        return retStatement

    def run(self):
        while self.isActive:
            print(f"Automated Deposit Bot sequence initiated. Will deposit {self.amount} USD weekly on the selected day of the week, at 1AM")
            job=self.triggerDeposit
            #TODO: save response in JSON
            #TODO: add a switch here. The switch will determine which schedule call based upon the day of thr week (which is enumerated 0-6)
            # schedule.every().wednesday.at("01:00").do(job)
            # schedule.every().thursday.at("01:00").do(job)
            #etc

#todo: maybe add a way to return the time that next deposit will occur. Maybe look into the Schedule library and see if this is built in?

