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
        # dayOfWeek is enumerated: 0-6 = Sun - Sat, Respectively
        self.amount = amount
        self.paymentMethodID = paymentMethodID
        #TODO: add check here to make sure amount is > 10
        #todo: perhaps add check to make sure this API key has deposit privileges

    def setAmount(self, newAmount):
        '''setter for automated deposit amount'''
        self.amount = newAmount
        #todo: add check to make sure amount is > 10
        #todo: Alternatively, batch.

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

    def numberToDay(self, arg):
        switcher = {
            0: "Sunday",
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday",
        }
        return switcher.get(arg, "invalid day enumeration")

    def run(self):
        dayString = self.numberToDay(self.dayOfWeek)
        print(f"Automated Deposit Bot sequence initiated. Will deposit {self.amount} USD weekly on {dayString} at 1AM")
        if self.isActive:
            def job():
                self.triggerDeposit
            if(self.dayOfWeek == 0):
                schedule.every().sunday.at("01:00").do(job)
            elif(self.dayOfWeek==1):
                schedule.every().monday.at("01:00").do(job)
            elif (self.dayOfWeek == 2):
                    schedule.every().tuesday.at("01:00").do(job)
            elif (self.dayOfWeek == 3):
                    schedule.every().wednesday.at("01:00").do(job)
            elif(self.dayOfWeek==4):
                schedule.every().thursday.at("01:00").do(job)
            elif (self.dayOfWeek == 5):
                schedule.every().friday.at("01:00").do(job)
            elif (self.dayOfWeek == 6):
                schedule.every().saturday.at("01:00").do(job)


#todo: maybe add a way to return the time that next deposit will occur.

