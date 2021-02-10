# PerlemirBot!

This is the bot scripting for the Perlemir cryptocurrency trading utility, built by the UNCA chapter of ACM.


# Project goals/features

The MVP is a script that will enable DCA cryptocurrency investing. Beyond that, more active trading strategies, to be determined. In consideration: Grid trading, departure from SMA and/or EMA, Momentum trackers. We will be using the coinbase pro exchange API.


## Current Status

This project is in its infancy. Stay tuned.

## Project TODO
- [ ] Create header file for all imports ELIAS
- [ ] Research callbacks / periodic executions ALEX
- [ ] bot class object getters: ALAN & ELIAS
  
    -[ ] Account ID
     
    -[ ] primary funding account
     
    -[ ] API privileges 
     
    -[ ] Wallets
- [ ] bot class object Setters:
     
  -[ ] TBD
  
- [ ] bot class object: buy/sell
- [ ] bot class object: json writing/reading (saving and reading transaction ID data)
 -[ ] determine data/file structure for storing json info
- [ ] automated deposit script
- [ ] DCA automated buys script
- [ ] research constant price feeds for active trading (websocket?)
- [ ] grid trading script?
- [ ] EMA/SMA script?



## Configuration

To use, add your Coinbase Pro API credentials to the apiconfig.py file

To use in sandbox mode (either for development or for fun), change the "SANDBOX" flag in apiconfig.py to "true". If "SANDBOX" is false, bot will be live on the coinbase server.

For sandbox mode you will need to make a new API key at:
https://public.sandbox.pro.coinbase.com/

## Related 

We have a webdev team creating a front end dashboard, in addition to a team creating an internal API.

## Tech Stack/Requirements

These scripts will be written in python3.

Libraries needed:
 - cbpro
 - requests


## API reference

TBD



## Notes on Usage
-Deposits and purchases both have a \$10 minimum 

## Licensing

This project will be published under the MIT license




<br><br><small>Disclaimer: Cryptocurrency markets are very volatile and there is risk involved with investing. This project is intended for educational purposes and/or for personal use. Not financial advice. May the force be with you</small>

