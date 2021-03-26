# PerlemirBot!

This is the bot scripting for the Perlemir cryptocurrency trading utility, built by the UNCA chapter of ACM.


# Project goals/features

The MVP is a script that will enable DCA cryptocurrency investing. Beyond that, more active trading strategies, to be determined. In consideration: Grid trading, departure from SMA and/or EMA, Momentum trackers. We will be using the coinbase pro exchange API.


## Current Status

AutomatedDeposit and automatedBuy bots are built but need QA/testing. Next step is to collaborate with API team regarding instantiation of bots as daemons. 


## Project TODO
- [ ] Collaborate with API team regarding instantiating bots as daemons.
- [ ] Collaborate with API team on json data transferring and transactionID queries
- [ ] Finish figuring out payment methods for deposit (perhaps requires non-sandbox testing)
- [ ] determine file structure and naming convention for storing json info 
- [ ] research constant price feeds for active trading (websocket?)
- [ ] grid trading script?
- [ ] EMA/SMA script?



## Configuration

To use, add your Coinbase Pro API credentials to the apiconfig.py file

To use in sandbox mode (either for development or for fun), change the "SANDBOX" flag in apiconfig.py to "true". If "SANDBOX" is false, bot will be live on the coinbase server.

For sandbox mode you will need to make a new API key at:
https://public.sandbox.pro.coinbase.com/

Note about sandbox: you can't deposit funds from fake bank account, but you *can* import funds from the fake coinbase account (click "Trade", go to BTC-USD, select "deposit" > *"USD" > "Coinbase.com")

## Related
We have a webdev team creating a front end dashboard, in addition to a team creating an internal API.

## Tech Stack/Requirements

These scripts will be written in python3.

Required Libraries:
- [ ] cbpro
- [ ] apsched

## API reference
-When changing a parameter of a bot that uses scheduling, the resetJobs() func needs to be called. This is only necessary for scheduling-related changes (not for amounts, etc). 

-There are some preconditions for variable ranges that are not checked in the constructor (although we do check them in the setters). It is assumed the client dashboard will make this check before passing constructor params to the bots. 

## Notes on Usage
-Deposits and purchases both have a \$10 minimum 


## Licensing

This project will be published under the MIT license




<br><br><small>Disclaimer: Cryptocurrency markets are very volatile and there is risk involved with investing. This project is intended for educational purposes and/or for personal use. Not financial advice. May the force be with you</small>

