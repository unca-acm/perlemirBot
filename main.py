import cbpro
import json
import apiconfig as cfg

print('The taxation of trade routes to outlaying star systems is in dispute.')

#get API info from config file
apiKey = cfg.api['API_KEY']
apiSecret = cfg.api['API_SECRET']
apiPassphrase =cfg.api['API_PASSPHRASE']

#bot object type definition
class bot:
    'Object for api client bot'
    #constructor
    def __init__(self, apikey, apisecret, apipassphrase):
        self.apikey = apikey
        self.apisecret = apisecret
        self.apipassphrase = apipassphrase
        self.apiClient = cbpro.AuthenticatedClient(apikey, apisecret, apipassphrase)


    #Instance Methods

    #this is essentially our toString for the object.
    def __str__(self):
        return f"this is string format. The api key for this bot client is{self.apikey}"

    #Getters and Setters
    def setApikey(self, apikey):
            self.apikey = apikey

    def getApikey(self, apikey):
            return self.apikey

    #Actions
    #make purchase
    def purchase(self, amount, currency):
        print('purchase made so coin much wow')
        print( f'in theory you just purchased {amount} worth of {currency}')

    def marketBuy(self, USDValue):
        details = self.apiClient.place_market_order(product_id='BTC-USD',
                                          side='buy',
                                          funds=USDValue) #could also use "size" to specify BTC amount                  s
        print(details)


#make a new bot object ()
myBot = bot(apiKey, apiSecret, apiPassphrase)
myBot.purchase(5, 'BTC')
print(myBot)
#myBot.purchase(5, 'BTC')
#myBot.marketBuy(1)
#myBot.marketBuy(1)


#apiClient = cbpro.AuthenticatedClient(API_KEY, API_SECRET,API_PASSPHRASE)

#for funding_account in apiClient.get_payment_methods():
#    print('the id number for {} is: {}'.format(funding_account['name'], funding_account['id']))

#clientAccounts = apiClient.get_accounts()
#print(clientAccounts)