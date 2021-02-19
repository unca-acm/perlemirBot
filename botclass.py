import cbpro
import json
import uuid
import os


# this writes json. takes object 'data' and places it in 'filename'. Will overwrite if 'filename' exists!
def write_json(data, filename):
    with open(filename, 'w+') as f:
        json.dump(data, f, indent=4)

#bot object type definition
class bot:
    'Object for api client bot'
    #constructor
    def __init__(self, apikey, apisecret, apipassphrase, sandbox):
        self.apikey = apikey
        self.apisecret = apisecret
        self.apipassphrase = apipassphrase
        if sandbox=='True':
            self.api_url='https://api-public.sandbox.pro.coinbase.com/'
        else:
            self.api_url= 'https://api.pro.coinbase.com'
        self.apiClient = cbpro.AuthenticatedClient(apikey, apisecret, apipassphrase, self.api_url)
        self.uuid=uuid.uuid4()

    #Instance Methods

    def __str__(self):
        '''this is essentially our toString for the object.'''
        return f"this is a bot toString. The uuid for this bot client is {self.uuid}"





    #Getters and Setters
    def setApiCredentials(self, apikey, apisecret, apipass):
            self.apikey = apikey
            self.apisecret = apisecret
            self.apipass = apipass

    #perhaps having this method is bad security, remove later?
    def getApikey(self):
            return self.apikey

    def getPaymentMethod(self):
        'returns [0]th payment method'
        primaryMethodID = self.apiClient.paymentMethods[0]['id']
        print(f'primary method id is {primaryMethodID}')
        return primaryMethodID
        #I am assuming that [0]th payment method is primary. Need to double check this is accurate.
        #Perhaps list them all here since this is parent class, then give option to choose which one to use for each child bot?

    def getAllPaymentMethods(self):
        'Returns array of all payment methods'
        allPaymentMethods = (self.apiClient.get_payment_methods())
        print(allPaymentMethods)
        return allPaymentMethods

    #Actions
    #make purchase
    def purchase(self, amount, currency):
        print('purchase made so coin much wow')
        print( f'in theory you just purchased {amount} worth of {currency}')

    #    if os.path.isfile(marketBuysJsonFile):
    def marketBuy(self, USDValue, pairing):
        thisOrderReturn = self.apiClient.place_market_order(product_id=pairing,
                                          side='buy',
                                          funds=USDValue) #could also use "size" to specify BTC amount
        #print the return response from the api request - will give the transaction ID if it went through, or the error if it didn't.
        print(thisOrderReturn)
        #add details of this buy to our json file
        #establish filename
        marketBuysJsonFile = str(self.uuid) + '_marketbuys.json'
        #Considerations: perhaps we should swap this filename and put "marketbuys" at the beginning. Or maybe store these inside a folder.
        #if file doesnt exist, create it with this as first entry
        if not os.path.isfile(marketBuysJsonFile):
            print(f"debug: making file {marketBuysJsonFile}")
            marketbuys={'market_buys': [thisOrderReturn]}
            write_json(marketbuys, marketBuysJsonFile)
        #else, append this entry
        else:
            print(f"debug: file exists")
            f = open(marketBuysJsonFile)
            data = json.load(f)
            temp=data['market_buys']
            temp.append(thisOrderReturn)
            write_json(temp, marketBuysJsonFile)
