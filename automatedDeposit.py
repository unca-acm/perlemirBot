"""
Automated Deposit Bot
Utility: Makes a deposit of {X} USD from {x} paymentMethodID on {x} day of the week, every week.
Remember to call resetJobs() whenever adjusting params that affect the scheduler.
"""

#todo remove unnecessary imports?
import apiconfig as cfg
import cbpro
import json
import botclass
import sys
import schedule
from apscheduler.schedulers.background import BackgroundScheduler
from botclass import bot

#automatedDeposit is a child class, inherits 'bot' methods.
class automatedDepositBot(bot):
    def __init__(self, amount, dayOfWeek, paymentMethodID):
        #NOTE: paymentMethodID needs to be established and known in order to construct this bot. Easiest way is to create a temp super 'bot' instance.
        super().__init__()
        self.dayOfWeek = dayOfWeek  # dayOfWeek is enumerated: 0-6 = Mon - Sun, Respectively
        self.amount = amount
        #TODO: add check here to make sure amount is > 10, OR have that happen on dashboard side. We check it in the setter.
        self.paymentMethodID = paymentMethodID
        self.sched = BackgroundScheduler(daemon=True)
        self.currentJob = None # This is to have a global pointer to the scheduler's job. It is used to retrieve the next run time (or potentially other utility in future)
        #todo: perhaps add check to make sure this API key has deposit privileges

    def setAmount(self, newAmount):
        '''setter for automated deposit amount'''
        if(newAmount < 10) or (newAmount < 0) or (not isinstance(newAmount, int)):
            print("Error, amount to deposit must be an integer >10")
            raise Exception("newAmount must be an integer >10")
            #todo: test this exception.
        else:
            self.amount = newAmount

    def getAmount(self):
        '''getter for automated deposit amount'''
        return self.amount

    def setDayOfWeek(self, newDay):
        '''setter for automated deposit frequency'''
        if(newDay < 0) or (newDay > 6) or (not isinstance(newDay, int)):
            print("Error, new day must be an integer 0-6 inclusive")
            raise Exception("Error, newDay must be an integer 0-6 inclusive")
            #todo: test this exception.
        else:
            self.dayOfWeek = newDay

    def getDayOfWeek(self):
        '''getter for automated deposit amount'''
        return self.dayOfWeek

    def getPaymentMethodID(self):
        '''getter for payment method ID'''
        return self.paymentMethodID

    def setPaymentMethod(self, newPaymentMethodID):
        '''setter for payment method ID. Need to query account for all of these.'''
        self.paymentMethodID = newPaymentMethodID
        """
        # Below is old code but keeping for posterity.
        # Previously, we were selecting an index from an array of payment methods.
        # Now, we are using ID directly (acquired elsewhere)
        """
        #allMethods = self.getAllPaymentMethods
        #objectMethods = allMethods()
        #self.paymentMethodID = objectMethods[self.paymentMethodIndex]['id']
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
        '''This is just used for pretty printing. Not necessary for code to function. '''
        switcher = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday",
        }
        return switcher.get(arg, "invalid day enumeration")

    def resetJobs(self):
        '''This will remove current jobs and restart with new params'''
        ''' You must call this every time you are changing a param that affects the schedule '''
        print("Cancelling the following jobs:")
        self.sched.print_jobs()
        self.sched.shutdown()
        print("\nRescheduling jobs:")
        self.run()

    def getNextRunTime(self):
        if self.currentJob is not None:
            return self.currentJob.next_run_time
        else:
            return None

    def killBot(self):
        '''shutdown the scheduler'''
        #todo: not sure if this is necessary - need to test if this automatically occurs when API deletes the bot object. Just here as reminder to test later.
        self.sched.shutdown()

    def run(self):
        """ Begins bot functionality: defines job, starts scheduler, adds job to schedule. """
        def job():
            if(self.isActive == True):
                print("Automated Deposit Triggered...")
                self.triggerDeposit()
                print("...Automated Deposit Occurred")
            else:
                print("Scheduled time has arrived, however Bot is not currently Active.")
        self.sched.start()
        self.currentJob = self.sched.add_job(job, 'cron', hour='1', day_of_week=self.dayOfWeek)
        #print(currentJob.id)
        print(f"Automated Deposit Bot sequence initiated. Will deposit {self.amount} USD weekly on {self.numberToDay(self.dayOfWeek)} at 1AM")
        self.sched.print_jobs()
