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

    def numberToDay(argument):
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
        func = switcher.get(argument)
        return func()

    def run(self):
        while self.isActive:
            print(f"Automated Deposit Bot sequence initiated. Will deposit {self.amount} USD weekly on {self.numberToDay(self.dayOfWeek)} at 1AM")
            job = self.triggerDeposit
            if(self.dayOfWeek == 0):
                schedule.every().Sunday.at("01:00").do(job)
            elif(self.dayOfWeek==1):
                schedule.every().Monday.at("01:00").do(job)
            elif (self.dayOfWeek == 2):
                    schedule.every().Tuesday.at("01:00").do(job)
            elif (self.dayOfWeek == 3):
                    schedule.every().Wednesday.at("01:00").do(job)
            elif(self.dayOfWeek==4):
                schedule.every().Thursday.at("01:00").do(job)
            elif (self.dayOfWeek == 5):
                schedule.every().Friday.at("01:00").do(job)
            elif (self.dayOfWeek == 6):
                schedule.every().Saturday.at("01:00").do(job)
            #TODO: save response in JSON


#todo: maybe add a way to return the time that next deposit will occur. Maybe look into the Schedule library and see if this is built in?

