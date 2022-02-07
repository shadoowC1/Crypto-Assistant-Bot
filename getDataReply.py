def getDataReply(data_command) :

    price = "Current price : "

    total_supply =  "Total supply : "

    circulating_supply = "Circulating supply : "

    apy = "Current apy : "

    total_staked_amount =  "Total staked amount : "

    total_stakers = "Total stakers : "

    replies = {"/price":price , "/price@FeyorraBot":price , "/total_supply":total_supply , "/total_supply@FeyorraBot":total_supply , "/circulating_supply":circulating_supply , "/circulating_supply@FeyorraBot":circulating_supply ,  "/apy":apy , "/apy@FeyorraBot":apy , "/total_staked_amount":total_staked_amount , "/total_staked_amount@FeyorraBot":total_staked_amount , "/total_stakers":total_stakers ,  "/total_stakers@FeyorraBot":total_stakers }

    return replies[data_command]
