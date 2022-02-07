def getReplyMarkupCommand(command) :

    commands = ["/about_feyorra" , "/about_feyorra@FeyorraBot" , "/locked_tokens" , "/locked_tokens@FeyorraBot" , "/latest" , "/latest@FeyorraBot" , "/liquidity_mining" , "/liquidity_mining@FeyorraBot" ,"/verify_stake" , "/verify_stake@FeyorraBot" , "/stake" , "/stake@FeyorraBot" , "/exchanges" , "/exchanges@FeyorraBot" , "/contract" , "/contract@FeyorraBot" ]

    for i in range(0,16) :

        if commands[i] == command :

            return commands[i]

    return 0 
