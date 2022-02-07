def getDataCommand(command) :

    commands = ["/price" , "/price@FeyorraBot" , "/total_supply" , "/total_supply@FeyorraBot" , "/circulating_supply" , "/circulating_supply@FeyorraBot" ,  "/apy" , "/apy@FeyorraBot" , "/total_staked_amount" , "/total_staked_amount@FeyorraBot" , "/total_stakers" ,  "/total_stakers@FeyorraBot" ]

    for i in range (0 , 12) :

        if commands[i] == command :

            return commands[i]

    return 0 
