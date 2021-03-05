import cbpro
import json
import apiconfig as cfg
import botclass
from automatedDeposit import automatedDepositBot
from automatedBuy import automatedBuy

print('The taxation of trade routes to outlaying star systems is in dispute.')


# ~~~~Testing main bot class~~~~

# make a new generic bot object ()
myBot = botclass.bot()

print(myBot)
# toString test.

# test market buy/sell BTC, selling BTC, 2x each
# $10 minimum. Will give error and append that error to our json if there is not enough money to make the purchase.
myBot.marketBuy(10, 'BTC-USD')
myBot.marketBuy(10, 'BTC-USD')
myBot.marketSell(10, 'BTC-USD')
myBot.marketSell(10, 'BTC-USD')

print(myBot.getAllPaymentMethods())

#todo: test all other additional myBot methods here:
#todo
#todo
#todo


# ~~~~Testing automatedDeposit bot ~~~~
#creating auto deposit bot for testing.
#the payment ID parameter is hardcoded in for testing. Got it (manually) from the myBot.getAllPaymentMethods call.
autoDepTester = automatedDepositBot(0, 10, 'b22911ee-ef35-5c97-bdd4-aef3f65618d9')

autoDepTester.run()


print(autoDepTester.triggerDeposit())
#todo: This is giving a "user login required" error, unsure why
#todo look into this error: Not sure if account specific, or problem with code logic.

#todo: test all other methods for bugs. It's mostly just getters/setters.



# ~~~~Testing automatedBuy~~~~

buybotTest = automatedBuy(2, "05:00", 10, 'BTC-USD')
#buy $10 BTC every 2 days at 5am

#todo: test all other methods for hidden bugs (mostly getters/setters)

buybotTest.run()

print(buybotTest.triggerBuy())

#print(buybot)
#print(buybot.triggerBuy())