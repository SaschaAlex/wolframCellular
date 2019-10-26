getrule = lambda rule : [True if i  == '1' else False for i in "{:08b}".format(rule) ]

getgame = lambda board : [True if i  == '1' else False for i in "{:31b}".format(board) ]

getbin = lambda bools : ['1' if i else '0' for i in bools]

getint = lambda bools : [1 if i else 0 for i in bools]

def game(rule,inital,itr):
    """
    rule and initial are a number that can be writen in a 8-bit
    register and itr the number of iteration. The function return
    and 2D-array with integers : {0, 1}
    """
    rule = getrule(rule)[::-1]
    board = getgame(inital)
    games = [getint(board)]
    max_i= len(board)
    for _ in range(itr):
        new_baord = [0]*max_i
        for index in range(max_i): # an iteration
            triple = [board[(index-1) % max_i]  ,board[(index) ],board[(index+1) %  max_i]]
            value = int(''.join(getbin(triple)),2)
            new_baord[index]  = rule[value]
        board = new_baord
        games.append(getint(new_baord))

    return games

def out(states):
    for i in states:
        print(i)