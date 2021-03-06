import cbpro
import json
import uuid
import os
import apiconfig as cfg

#todo: place json writes into ./json folder for all methods (this folder was added to the gitignore)

def write_json(data, filename):
    '''this writes json. takes object 'data' and places it in 'filename'.
    Important: Will overwrite if 'filename' exists!'''
    with open(filename, 'w+') as f:
        json.dump(data, f, indent=4)

#bot object type definition
class bot:
    'Object for api client bot'
    #constructor
    def __init__(self):
        self.apiKey = cfg.api['API_KEY']
        self.apiSecret = cfg.api['API_SECRET']
        self.apiPassphrase = cfg.api['API_PASSPHRASE']
        self.sandbox = cfg.api['SANDBOX']
        if self.sandbox=='True':
            self.api_url='https://api-public.sandbox.pro.coinbase.com/'
        else:
            self.api_url= 'https://api.pro.coinbase.com'
        self.apiClient = cbpro.AuthenticatedClient(self.apiKey, self.apiSecret, self.apiPassphrase, self.api_url)
        self.uuid=uuid.uuid4()
        self.isActive=True
    #todo: inside constructor, check that API key credentials are valid. Perhaps throw an exception if not.

    #Instance Methods

    def __str__(self):
        '''this is essentially our toString for the object.'''
        return f"this is a bot toString. The uuid for this bot client is {self.uuid}"

    #Getters and Setters

    def setActivity(self, booleanInput):
        '''Changes bot isActive to True or False.
        Bots perform automated functions while isActive=True. This allows for pausing of bots without destroying/initiating new ones'''
        self.isActive = booleanInput

    def getActivity(self):
        '''getter for boolean isActive'''
        return self.isActive

    def setApiCredentials(self, apikey, apisecret, apipass):
            self.apiKey = apikey
            self.apiSecret = apisecret
            self.apiPass = apipass

    def getAllPaymentMethods(self):
        'Returns array of all payment methods'
        allPaymentMethods = (self.apiClient.get_payment_methods())
        return allPaymentMethods
        #Note: For automated deposits, we will need user to tell us which of these methods to use
        #The internal API will call this method (on a temp bot?), list all payment methods by name, and pass the chosen paymentMethodID as param in order to make the automatedDeposit bot.

    #Actions

    def marketBuy(self, USDValue, pairing):
        '''place market buy, writes the return to file'''
        thisOrderReturn = self.apiClient.place_market_order(product_id=pairing,
                                          side='buy',
                                          funds=USDValue) #could also use "size" to specify BTC amount, whereas 'funds' = fiat
        #add details of this buy to our json file
        #establish filename
        marketBuysJsonFile = str(self.uuid) + '_marketbuys.json'
        #todo Considerations: perhaps we should swap this filename and put "marketbuys" at the beginning. Or maybe store these inside a folder.
        #if file doesnt exist, create it with this as first entry
        if not os.path.isfile(marketBuysJsonFile):
            marketbuys={'market_buys': [thisOrderReturn]}
            write_json(marketbuys, marketBuysJsonFile)
        #else, append this entry
        else:
            f = open(marketBuysJsonFile)
            data = json.load(f)
            temp=data['market_buys']
            temp.append(thisOrderReturn)
            write_json(temp, marketBuysJsonFile)
        return thisOrderReturn

    def marketSell(self, USDValue, pairing):
        '''place market sale order, writes the return to file '''
        thisOrderReturn = self.apiClient.place_market_order(product_id=pairing,
                                          side='sell',
                                          funds=USDValue) #could also use "size" to specify BTC amount
        jsonFilename = str(self.uuid) + '_marketSells.json'
        #Considerations: perhaps we should swap this filename and put "marketbuys" at the beginning. Or maybe store these inside a folder.
        #if file doesnt exist, create it with this as first entry, else create it
        if not os.path.isfile(jsonFilename):
            data={'market_sells': [thisOrderReturn]}
            write_json(data, jsonFilename)
        else:
            f = open(jsonFilename)
            data = json.load(f)
            temp=data['market_sells']
            temp.append(thisOrderReturn)
            write_json(temp, jsonFilename)
        return thisOrderReturn
