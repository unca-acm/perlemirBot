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
myBot.marketBuy(10, 'BTC-USD')
myBot.marketBuy(10, 'BTC-USD')
myBot.marketSell(10, 'BTC-USD')
myBot.marketSell(10, 'BTC-USD')

print(myBot.getAllPaymentMethods())
#printing these for use later.

#todo: test all other additional myBot methods here:
#todo
#todo
#todo


# ~~~~Testing automatedDeposit bot ~~~~
#creating auto deposit bot for testing.
#the payment ID parameter is hardcoded in for testing. Got it (manually) from the myBot.getAllPaymentMethods call.
#autoDepTester = automatedDepositBot(0, 10, 'b22911ee-ef35-5c97-bdd4-aef3f65618d9')

#autoDepTester.run()
#todo: these "run()" functions have a while loop.
# talk to API team and see if they can cancel the func
# otherwise, they can just set isActive=False and trigger wont happen. But loop keeps running.

#print(autoDepTester.triggerDeposit())
#todo: This is giving a "user login required" error.
# I think this means user needs to reconnect bank via the coinbase UI
# I think this will work outside sandbox mode

#todo: test all other methods for bugs. It's mostly just getters/setters.



# ~~~~Testing automatedBuy~~~~

buybotTest = automatedBuy(7, 22, 10, 'BTC-USD')
# create bot to buy $10 BTC every 7 days at 22:00
#todo: test all other methods for hidden bugs (mostly getters/setters)

buybotTest.run()

#print(buybotTest.triggerBuy())
