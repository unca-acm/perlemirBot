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
    def __init__(self, dayOfWeek, amount, paymentMethodID):
        super().__init__()
        self.dayOfWeek = dayOfWeek
        # days of week are enumerated, 0-6, Sun - Sat, Respectively
        self.amount = amount
        self.paymentMethodID = paymentMethodID
#        self.paymentMethodID = self.getChosenPaymentMethodID
        #TODO: add check here to make sure amount is > 10
        #todo: perhaps add check to make sure this API key has deposit privileges
        #todo: amount needs to be >$10, add check here?
        #todo: API has to query list of payment methods first so that we can pass the ID of the method as param

    def setAmount(self, newAmount):
        '''setter for automated deposit amount'''
        self.amount = newAmount
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

    def getPaymentMethodID(self):
        '''getter for payment method ID'''
        return self.paymentMethodID

    def setPaymentMethod(self, newPaymentMethodID):
        '''setter for payment method ID. Need to query account for all of these.'''
        #todo: this is old code but keeping for posterity. We were using index of payment method arrays, now we are using ID directly
        #allMethods = self.getAllPaymentMethods
        #objectMethods = allMethods()
        #self.paymentMethodID = objectMethods[self.paymentMethodIndex]['id']
        self.paymentMethodID = newPaymentMethodID
        #return self.paymentMethodID

    def getChosenPaymentMethodID(self):
        '''returns chosen payment method ID'''
        return self.paymentMethodID

    def triggerDeposit(self):
        '''makes a deposit. paymentMethodID is the ID of the payment method'''
        retStatement = self.apiClient.deposit(self.amount, 'USD', self.paymentMethodID)
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

