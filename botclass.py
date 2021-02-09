import cbpro
import json
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
        return f"this is a bot toString. The api key for this bot client is {self.apikey}"

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
        thisOrderReturn = self.apiClient.place_market_order(product_id='BTC-USD',
                                          side='buy',
                                          funds=USDValue) #could also use "size" to specify BTC amount                  s
        #print the return response from the api request - will give the transaction ID if it went through, or the error if it didn't.
        print(thisOrderReturn)
        #add details of this buy to our json file
        with open('marketBuys.json') as marketbuys_jsonfile:
            data = json.load(marketbuys_jsonfile)
            temp = data['market_buys']
            newOrderToAdd = thisOrderReturn
            temp.append(newOrderToAdd)
        write_json(data, 'marketBuys.json') #this overwrites the marketBuys file with the new json that has the order appended to it.

#this writes json. takes object 'data' and places it in 'filename'. Will overwrite if 'filename' exists!
def write_json(data, filename):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)
