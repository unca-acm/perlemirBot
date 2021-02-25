# PerlemirBot!

This is the bot scripting for the Perlemir cryptocurrency trading utility, built by the UNCA chapter of ACM.


# Project goals/features

The MVP is a script that will enable DCA cryptocurrency investing. Beyond that, more active trading strategies, to be determined. In consideration: Grid trading, departure from SMA and/or EMA, Momentum trackers. We will be using the coinbase pro exchange API.


## Current Status

Goal is for MVP to be finished by Friday, March 5. MVP means automatedDeposit and automatedBuy, so that we can enable DCA investing. After the MVP is functional, we will begin work on more dynamic trading bots.

## Project TODO
- [ ] Finish automatedBuy bot
- [ ] Collaborate with API team on json data transferring and transactionID queries
- [ ] Finish figuring out payment methods for deposit (perhaps requires non-sandbox testing)
- [ ] For both current bot projects, figure out 'schedule' library, and determine what increment we want to use and/or allow
 -[ ] determine file structure and naming convention for storing json info 
-[ ] We need to work on querying CB with transaction IDs to get current info (specifically, updates on amount purchased)
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
All necessary libraries are included in the provided virtual environment.

## API reference
TBD


## Notes on Usage
-Deposits and purchases both have a \$10 minimum 

## Licensing

This project will be published under the MIT license




<br><br><small>Disclaimer: Cryptocurrency markets are very volatile and there is risk involved with investing. This project is intended for educational purposes and/or for personal use. Not financial advice. May the force be with you</small>

