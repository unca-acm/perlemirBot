#Automated Buys

#todo remove unnecessary imports?
import apiconfig as cfg
import cbpro
import json
import botclass
import sys
import schedule
from botclass import bot

#automatedDeposit is a child class, inherits 'bot' methods.
class automatedBuy(bot):
    def __init__(self, frequency, timeToRun, fiatAmount, pairing):
        super().__init__()
        self.amount = fiatAmount
        self.frequency = frequency   #run every X days
        self.pairing = pairing     #pairing is'BTC-USD' or 'ETH-USD' etc.
        self.timeToRun  #Military time: "10:30" format.

    def getTimeToRun(self):
        '''getter for time to run. Military time: "10:30" format. '''
        return self.timeToRun()

    def setTimeToRun(self, newTime):
        '''setter for time to run. Military time: "10:30" format. '''
        self.timeToRun = newTime

    def getFiatAmount(self):
        '''getter for automated purchase amount (in fiat)'''
        return self.fiatAmount

    def setFiatAmount(self, newAmount):
        '''setter for automated purchase amount (in fiat)'''
        self.fiatAmount = newAmount
        #todo: add check to make sure amount is > 10

    def setFrequency(self, newFreq):
        '''setter for frequency'''
        self.frequency = newFreq

    def getFrequency(self):
        '''getter for frequency'''
        return self.frequency

    def getPairing(self):
        return self.pairing

    def setPairing(self, newpair):
        self.pairing = newpair
        #todo: discuss whether this is necessary. In theory, you probably just want to make a new bot if you want to change currency, as opposed to altering existing bot.

    def triggerBuy(self):
        '''this is the method that the scheduler library will call to perform desired action'''
        transaction = self.marketBuy(self.amount, self.pairing)
        #todo: this should record the purchase json automatically via the marketBuy method - needs testing.
        return transaction

    def run(self):
        while self.isActive:
            print(f"Automated Buy sequence initiated. Will purchase {self.fiatAmount} in fiat worth of {self.pairing} every {self.frequency} days at {self.timeToRun}")
            #todo: change this print statement to reflect accurate frequency
            job=self.triggerDeposit
            #TODO: save response in JSON (probably not necessary, happens inside marketBuy)
            schedule.every(self.frequency).days.at(self.timeToRun).do(job)
            #todo: test that this syntax will work

