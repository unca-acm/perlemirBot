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
        #todo: are we using day of week, or other frequency? Make sure this is consistent.

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
            print(f"Automated Deposit Bot sequence initiated. Will deposit {self.amount} USD every {self.frequency} days")
            job=self.triggerDeposit
            #schedule.every().(self.dayOfWeek).(self.frequency).days.do(job)
            #TODO: save response in JSON


#todo: maybe add a way to return the time that next deposit will occur. Maybe look into the Schedule library and see if this is built in?

#TODO: insert logic for frequency - determine how user enters the frequency and what interval, and then how to create that call to the scheduler.
