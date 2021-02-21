import apiconfig as cfg
from botclass import bot


#grid trading is a simple strategy used for assets that reliably trade sideways with predictable volatility inside an noticeable range.
#super simple to understand, but not likely to make money *unless* you examine market trends beforehand appropriately.

class gridTrader(bot):
    def __init__(self, frequency, amount, pairing, bottom, top, percentage):
        apiKey = cfg.api['API_KEY']
        apiSecret = cfg.api['API_SECRET']
        apiPassphrase = cfg.api['API_PASSPHRASE']
        sandbox = cfg.api['SANDBOX']
        super().__init__(apiKey, apiSecret, apiPassphrase, sandbox)
        self.amount = amount
        self.pairing = pairing
        self.bottom = bottom
        self.top = top
        self.percentage
        #consideration: add duration? Or perhaps do that via dashboard? Or just run-til-stop?

        pesudocode:
        {amount} is the starting stack
        when price reaches bottom, buy percentage of current stack (amount)
        when price reaches top, sell percentage of stack.
        goal here is to increase stack.
        Potential: add stop loss so that you can only lose profits, and never more than a percentage of initial investment.
