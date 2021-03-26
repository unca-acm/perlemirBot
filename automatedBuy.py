"""
Automated Buy Bot
Utility: Makes a purchase of a {X} currency every {X} days at {X} o'clock.
Remember to call resetJobs() whenever adjusting params that affect the scheduler.
"""

#todo remove unnecessary imports? Maybe look into header file options?
import apiconfig as cfg
import cbpro
import json
import botclass
import sys
from botclass import bot
import time
from apscheduler.schedulers.background import BackgroundScheduler
import apscheduler
import daemon

# automatedDeposit is a child class, inherits 'bot' methods.
class automatedBuy(bot):
    def __init__(self, fiatAmount, pairing, frequency, timeToRun,):
        super().__init__()
        self.fiatAmount = fiatAmount
        self.frequency = frequency   #run every X days
        self.pairing = pairing     #pairing is'BTC-USD' or 'ETH-USD' etc.
        self.timeToRun = timeToRun  #User chooses an hour, Military time: 0-23. Buy happens on the hour.
        # todo: precondition is that timeToRun is within range 0-23. We check this when the setter runs, but need to determine if we also check here, or if that check should happen on the dashboard?
        self.currentJob  = None # this is to have a pointer to the scheduler's job. it is used to retrieve the next run time.
        self.sched = BackgroundScheduler(daemon=True)


    def getTimeToRun(self):
        '''getter for time to run. Military time: 0-23'''
        return self.timeToRun()

    def setTimeToRun(self, newTime):
        '''setter for time to run. Military time: 0-23 '''
        if(newTime > 23) or (newTime < 0) or (not isinstance(newTime, int)):
            print("Error, time to run must be an integer: 0-23 inclusive")
            raise Exception("timeToRun must be an integer 0-23 inclusive")
            #todo: test this exception.
        else:
            self.timeToRun = newTime

    def getFiatAmount(self):
        '''getter for automated purchase amount (in fiat)'''
        return self.fiatAmount

    def setFiatAmount(self, newAmount):
        '''setter for automated purchase amount (in fiat)'''
        self.fiatAmount = newAmount
        #todo: add check to make sure amount is > 10
        #todo: alternatively, we can implement batching.

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
        # todo: discuss whether this is necessary. In theory, you probably just want to make a new bot if you want to change currency, as opposed to altering existing bot.

    def triggerBuy(self):
        '''this is the method that the scheduler library will call to perform desired action'''
        transaction = self.marketBuy(self.fiatAmount, self.pairing)
        # todo: this should record the json return automatically via marketBuy method in super class - needs testing.
        return transaction

    def resetJobs(self):
        '''This will remove current jobs and restart with new params'''
        ''' You must call this every time you are changing a param that affects the schedule, such as dayOfWeek' '''
        ''' not necessary for changing amount '''
        print("Cancelling the following jobs:")
        self.sched.print_jobs()
        self.sched.shutdown()
        print("\nRescheduling jobs:")
        self.run()

    def getNextRunTime(self):
        if(self.curentJob is not None):
            return(self.currentJob.next_run_time)
        else:
            return None

    def killBot(self):
        '''cancels the scheduler'''
        # todo: not sure if this is necessary - need to test if this automatically happens when API deletes the bot object. Just here as reminder to test later.
        self.sched.shutdown()

    def run(self):
        '''initiate the bot to start running'''
        #define our job.
        def job():
            '''This function is what the scheduler calls whenever the scheduled time comes up.'''
            if self.isActive == True:
                print("Automated Buy Triggered...")
                self.triggerBuy()
                print("...Automated Buy Occurred.")
            else:
                print("Scheduled time has arrived, however Bot is not currently Active.")

        self.sched.start()
        self.currentJob = self.sched.add_job(job, 'cron', hour=self.timeToRun, day=self.frequency)
        #self.sched.add_job(lambda: self.sched.print_jobs(), 'interval', seconds=5)   #this prints current jobs ever 5 seconds. Used for debugging
        print(f"Automated Buy sequence initiated. Will purchase {self.fiatAmount} in fiat worth of {self.pairing} every {self.frequency} days at {self.timeToRun}:00")
        self.sched.print_jobs()
