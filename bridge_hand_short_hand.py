def bridge_hand_shorthand(hand):
    spades = []
    hearts = []
    diamonds = []
    clubs = []
    for i in range(0,len(hand)):
        if hand[i][1] == 'spades':
            spades.append(hand[i][0])
        if hand[i][1] == 'hearts':
            hearts.append(hand[i][0])
        if hand[i][1] == 'diamonds':
            diamonds.append(hand[i][0])
        if hand[i][1] == 'clubs':
            clubs.append(hand[i][0])
    result = ''

    # Spades
    if len(spades)==0:
        result = result + '-'
    else:
        for i in range(0,len(spades)):
            if spades[i] == 'ace':
                result = result +'A'
        for i in range(0,len(spades)):
            if spades[i] == 'king':
                result = result +'K'
        for i in range(0,len(spades)):
            if spades[i] == 'queen':
                result = result +'Q'
        for i in range(0,len(spades)):
            if spades[i] == 'jack':
                result = result +'J'
        for i in range(0,len(spades)):
            if (spades[i] != 'jack')&(spades[i] != 'queen')&(spades[i] != 'king')&(spades[i] != 'ace'):
                result = result +'x'
    result = result +' '

    # hearts
    if len(hearts)==0:
        result = result + '-'
    else:
        for i in range(0,len(hearts)):
            if hearts[i] == 'ace':
                result = result +'A'
        for i in range(0,len(hearts)):
            if hearts[i] == 'king':
                result = result +'K'
        for i in range(0,len(hearts)):
            if hearts[i] == 'queen':
                result = result +'Q'
        for i in range(0,len(hearts)):
            if hearts[i] == 'jack':
                result = result +'J'
        for i in range(0,len(hearts)):
            if (hearts[i] != 'jack')&(hearts[i] != 'queen')&(hearts[i] != 'king')&(hearts[i] != 'ace'):
                result = result +'x'
    result = result +' '

    # diamonds
    if len(diamonds)==0:
        result = result + '-'
    else:
        for i in range(0,len(diamonds)):
            if diamonds[i] == 'ace':
                result = result +'A'
        for i in range(0,len(diamonds)):
            if diamonds[i] == 'king':
                result = result +'K'
        for i in range(0,len(diamonds)):
            if diamonds[i] == 'queen':
                result = result +'Q'
        for i in range(0,len(diamonds)):
            if diamonds[i] == 'jack':
                result = result +'J'
        for i in range(0,len(diamonds)):
            if (diamonds[i] != 'jack')&(diamonds[i] != 'queen')&(diamonds[i] != 'king')&(diamonds[i] != 'ace'):
                result = result +'x'
    result = result +' '

    # clubs
    if len(clubs)==0:
        result = result + '-'
    else:
        for i in range(0,len(clubs)):
            if clubs[i] == 'ace':
                result = result +'A'
        for i in range(0,len(clubs)):
            if clubs[i] == 'king':
                result = result +'K'
        for i in range(0,len(clubs)):
            if clubs[i] == 'queen':
                result = result +'Q'
        for i in range(0,len(clubs)):
            if clubs[i] == 'jack':
                result = result +'J'
        for i in range(0,len(clubs)):
            if (clubs[i] != 'jack')&(clubs[i] != 'queen')&(clubs[i] != 'king')&(clubs[i] != 'ace'):
                result = result +'x'
    return(result)
