#Automated Buys

pseudocode
    receive asset to buy (ETH/BTC/Other)
    receive amount in USD to purchase
    Buys have $10 minimum so make sure amount is >$10 (or perhaps write logic in to batch until reaches $10 minimum)
    receive frequency to make purchase
    create bot  (inherit bot from botclass?)
    make the buys on set schedule
    Record information about transaction into a JSON - either just the transaction ID, or more info (entire return statement) - TBD

