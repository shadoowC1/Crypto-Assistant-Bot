def getReply(replyMarkup_command) :

    about_feyorra = "Feyorra is the utility token of the leading micro wallet faucetPay.io and pasino.com On top of that it comes with important DeFi features like staking, liquidity mining and more . \ncheck more about feyorra here:"

    locked_tokens = "All lp tokens and company funds locks can be found here: "

    latest =  "Feyoora Latest News are published via Twitter ."

    liquidity_mining = "You can lock some of your cryptocurrency to contribute to the liquidity of a feyorra trading pair and receive rewards from fees that are charged to traders. on top of that you can lock you lp tokens to receive extra rewards , more informations available at:"

    verify_stake = "Verify your stakes at Pasino  and earn a share of the house edge! Pasino pays out 0.25% of the total betting volume to all verified stakers.\n"+"     \n" + "Payouts are made in over 10 different cryptocurrencies. House edge-sharing is your gateway to an additional passive income. "

    stake = "There are several ways to stake feyorra :"

    exchanges = "Feyorra is currently listed on :"

    contract = "Feyorra is erc-20 etablished under ethereum blockchain :"

    replies = {"/about_feyorra":about_feyorra ,"/about_feyorra@FeyorraBot":about_feyorra , "/locked_tokens":locked_tokens , "/locked_tokens@FeyorraBot":locked_tokens , "/latest":latest , "/latest@FeyorraBot":latest , "/liquidity_mining":liquidity_mining , "/liquidity_mining@FeyorraBot":liquidity_mining , "/verify_stake":verify_stake , "/verify_stake@FeyorraBot":verify_stake , "/stake":stake , "/stake@FeyorraBot":stake , "/exchanges":exchanges , "/exchanges@FeyorraBot":exchanges , "/contract":contract , "/contract@FeyorraBot":contract }

    return replies[replyMarkup_command]
