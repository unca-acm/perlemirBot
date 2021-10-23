# PerlemirBot!

This is the bot scripting for the Perlemir cryptocurrency trading utility, built by the UNCA chapter of ACM.


# Project goals/features

The MVP is a script that will enable DCA cryptocurrency investing. Beyond that, more active trading strategies, to be determined. In consideration: Grid trading, departure from SMA and/or EMA, Momentum trackers. We will be using the coinbase pro exchange API.


## Current Status

MVP goal is to have automatedDeposit and automatedBuy classes completed so that we can enable DCA investing. After the MVP is functional, we will begin work on more dynamic trading bots.

We are currently developing a back-end internal API for this project in another repo. Get in touch if you want to help!

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

