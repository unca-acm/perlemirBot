import cbpro
print('The taxation of trade routes to outlaying star systems is in dispute.')

API_KEY = 'xxxxxxxxxxxxxxxxx'
API_SECRET = 'xxxxxxxxxxxxxxxxxxxx'
API_PASSPHRASE ='xxxx'


#bot object type
class bot:
    'Object for api client bot'
    #constructor
    def __init__(self, apikey, apisecret, apipassphrase):
        self.apikey = apikey
        self.apisecret = apisecret
        self.apipassphrase = apipassphrase
        self.apiClient = cbpro.AuthenticatedClient(apikey, apisecret, apipassphrase)
    #class variables
    #apikey= 'api_key_input'
    #apisecret = 'api_secret_input'
    #apipassphrase = 'api_passphrase_input'


    #Instance Methods

    #getters and setters
    def setApikey(self, apikey):
            self.apikey = apikey

    def getApikey(self, apikey):
            return self.apikey

    #this is essentially our toString for the object.
    def __str__(self):
        return f"this is string format. The api key for this bot client is{self.apikey}"

    #make purchase
    def purchase(self, amount, currency):
        print('purchase made so coin much wow')

    def marketBuy(self, USDValue):
        details = self.apiClient.place_market_order(product_id='BTC-USD',
                                          side='buy',
                                          funds=USDValue) #could also use "size" to specify BTC amount                  s
        print(details)
        return f"Succesfully purchased {USDValue} in BTC"


#make a new bot object (will receive these params as args)
myBot = bot(API_KEY, API_SECRET, API_PASSPHRASE)

myBot.purchase(5, 'BTC')
myBot.marketBuy(1)
myBot.marketBuy(1)


#apiClient = cbpro.AuthenticatedClient(API_KEY, API_SECRET,API_PASSPHRASE)

#for funding_account in apiClient.get_payment_methods():
#    print('the id number for {} is: {}'.format(funding_account['name'], funding_account['id']))

#clientAccounts = apiClient.get_accounts()
#print(clientAccounts)