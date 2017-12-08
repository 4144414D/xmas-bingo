""""
GitHub: https://github.com/4144414D/xmas-bingo
Email: adam@nucode.co.uk

Usage:
    xmas-bingo <number-of-songs> [-o]
    xmas-bingo --all
    xmas-bingo --version
    xmas-bingo --help

 Options:
    --help              Show this screen.
    --version           Show the version.
    -o, --output        Save winning boards to a file.
    -a, --all           Determine results of all numbers of songs.
"""
VERSION="0.1"

from docopt import docopt

def print_board(board):
    board = '{0:025b}'.format(board)
    return board[0:5]+'\n'+board[5:10]+'\n'+board[10:15]+'\n'+board[15:20]+'\n'+board[20:25]+'\n'

def check_win(board,winning_boards):
    for winning_board in winning_boards:
        if board & winning_board == winning_board: return True
    return False

def create_pool(songs):
        #poor way to determine options
        pool = []
        for x in range(16777215): #16777215 highest 24 bit number
             candidate = '{0:024b}'.format(x)
             if candidate.count('1') == songs:
                 candidate = candidate[:12] + '1' + candidate[12:]
                 pool.append(int(candidate,2))
        return pool

def create_winning_boards():
    winning_boards = []
    winning_boards.append(int('1111100000000000000000000',2))
    winning_boards.append(int('0000011111000000000000000',2))
    winning_boards.append(int('0000000000111110000000000',2))
    winning_boards.append(int('0000000000000001111100000',2))
    winning_boards.append(int('0000000000000000000011111',2))
    winning_boards.append(int('1000010000100001000010000',2))
    winning_boards.append(int('0100001000010000100001000',2))
    winning_boards.append(int('0010000100001000010000100',2))
    winning_boards.append(int('0001000010000100001000010',2))
    winning_boards.append(int('0000100001000010000100001',2))
    winning_boards.append(int('1000001000001000001000001',2))
    winning_boards.append(int('0000100010001000100010000',2))
    return winning_boards

def all():
    for songs in range(25):
        print "Testing results with",
        print songs,
        print "song(s)"
        main(songs,False)
        print

def main(songs,output):
    pool = create_pool(songs)
    winning_boards = create_winning_boards()
    count = 0
    wins = 0
    if output: f = open('winning_boards.txt','w')
    for board in pool:
        count += 1
        if check_win(board,winning_boards):
            wins += 1
            if output: f.write(print_board(board)+'\n')
    print "Total Count:",
    print count
    print "Wins:",
    print wins
    print "Winning percentage:",
    print (100.0/count)*wins,
    if output: f.close()

if __name__ == '__main__':
        arguments = docopt(__doc__, version=VERSION)
        if arguments['--all']:
            all()
        else:
            songs = int(arguments['<number-of-songs>'])
            main(songs,arguments['--output'])
