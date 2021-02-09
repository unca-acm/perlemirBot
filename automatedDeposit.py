#this will be the script that makes automated deposits
import apiconfig as cfg
import cbpro
import json
import botclass
import sys

#USAGE: automatedDeposit.py USDamount Frequency

#pseudocode:
#    receive amount to deposit
#    receive frequency of deposit
#    make bot object
#    make it work

#check arguments
numArgs = len(sys.argv)
if numArgs < 3:
    print("Not enough arguments, must enter USD amount to deposit and frequency")
    exit()
amount = sys.argv[1]
if amount <10
    print("Error: Minimum deposit is $10")
    exit()

#TODO: use sys.aargv[2] for frequency

#get API info from config file
apiKey = cfg.api['API_KEY']
apiSecret = cfg.api['API_SECRET']
apiPassphrase =cfg.api['API_PASSPHRASE']

#make a new bot object
myBot = botclass.bot(apiKey, apiSecret, apiPassphrase)
print(myBot)

#get primary payment method ID
paymentMethods = (myBot.apiClient.get_payment_methods())
primaryMethodID = paymentMethods[0]['id']
print(primaryMethodID)

#TODO: insert logic for frequency

#this does the actual deposit:
response = myBot.apiClient.deposit(amount, 'USD', primaryMethodID)
print(response)
#TODO: save response in JSON