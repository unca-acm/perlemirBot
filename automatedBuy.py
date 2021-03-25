#Automated Buys

#todo remove unnecessary imports? Maybe look into header file?
import apiconfig as cfg
import cbpro
import json
import botclass
import sys
import schedule
from botclass import bot
import time
from daemon import runner
from apscheduler.schedulers.background import BackgroundScheduler
import apscheduler
import daemon


#automatedDeposit is a child class, inherits 'bot' methods.
class automatedBuy(bot):
    def __init__(self, frequency, timeToRun, fiatAmount, pairing):
        super().__init__()
        self.fiatAmount = fiatAmount
        self.frequency = frequency   #run every X days (starting on time the bot is created)
        self.pairing = pairing     #pairing is'BTC-USD' or 'ETH-USD' etc.
        self.timeToRun = timeToRun  #User chooses an hour, Military time: 0-23. Buy happens on the hour.
        self.sched = BackgroundScheduler(daemon=True)

    def getTimeToRun(self):
        '''getter for time to run. Military time: 0-23'''
        return self.timeToRun()

    def setTimeToRun(self, newTime):
        '''setter for time to run. Military time: 0-23 '''
        self.timeToRun = newTime
        # Todo: check that input is within 0-23

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
        transaction = self.marketBuy(self.fiatAmount, self.pairing)
        #todo: this should record the purchase json automatically via the marketBuy method - needs testing.
        return transaction


    def run(self):
        '''initiate the bot to start running'''
        #define our job.
        def job():
            if self.isActive == True:
                print("Automated Buy Triggered...")
                self.triggerBuy
                print("...Automated Buy Occurred")
            else:
                print("Scheduled time has arrived, however Bot is currently not Active.")

        self.sched.add_job(job, 'cron', hour=self.timeToRun, day=self.frequency)
        self.sched.add_job(lambda: self.sched.print_jobs(), 'interval', seconds=5)   #this prints current jobs ever 5 seconds. Used for debugging
        self.sched.start()
        print(f"Automated Buy sequence initiated. Will purchase {self.fiatAmount} in fiat worth of {self.pairing} every {self.frequency} days at {self.timeToRun}:00")


