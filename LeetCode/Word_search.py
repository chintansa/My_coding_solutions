board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]


word = "ABCB"

word_set = list(set([i for i in word]))

board_str = ''.join([''.join(i) for i in board])


flag=0

for i in word_set:
    if(board_str.count(i) < word.count(i)):
        flag=1
        print('false')
        # break
    



if(flag==0):
    print('true')