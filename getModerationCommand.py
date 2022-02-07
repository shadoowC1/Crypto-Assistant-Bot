def getModerationCommand(command) :

    commands = ["/ban" , "/delete"]

    for i in range (0 , 2) :

        if commands[i] == command :

            return commands[i]

    return 0
