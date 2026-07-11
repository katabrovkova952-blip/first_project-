import copy
from functools import lru_cache
import random


SIZE = 4


# ==========================
# MOVE ENGINE
# ==========================

def compress(row):
    row = [x for x in row if x]
    return row + [0]*(SIZE-len(row))


def merge(row):
    score = 0
    result=[]

    i=0

    while i < len(row):

        if i+1 < len(row) and row[i]==row[i+1]:

            value=row[i]*2
            result.append(value)
            score+=value
            i+=2

        else:
            result.append(row[i])
            i+=1

    return result+[0]*(SIZE-len(result)),score


def move_row(row):

    row=compress(row)
    row,score=merge(row)

    return row,score


def move_left(board):

    score=0
    new=[]

    for row in board:

        r,s=move_row(row)

        new.append(r)
        score+=s

    return new,score


def move_right(board):

    new=[]

    for row in board:

        r,s=move_row(row[::-1])

        new.append(r[::-1])

    return new,sum(
        move_left(board)[1:2]
    )


def transpose(board):

    return [
        list(x)
        for x in zip(*board)
    ]


def move_up(board):

    b=transpose(board)
    b,s=move_left(b)

    return transpose(b),s


def move_down(board):

    b=transpose(board)
    b,s=move_right(b)

    return transpose(b),s


MOVES={
    "ВЛІВО":move_left,
    "ВПРАВО":move_right,
    "ВГОРУ":move_up,
    "ВНИЗ":move_down
}


# ==========================
# HELPERS
# ==========================

def tuple_board(board):
    return tuple(
        tuple(r)
        for r in board
    )


def list_board(board):
    return [
        list(r)
        for r in board
    ]


def empty(board):

    return [
        (i,j)
        for i in range(4)
        for j in range(4)
        if board[i][j]==0
    ]


# ==========================
# HIGH SCORE HEURISTIC
# ==========================


snake=[
    [16,15,14,13],
    [9,10,11,12],
    [8,7,6,5],
    [1,2,3,4]
]


def snake_score(board):

    value=0

    for i in range(4):
        for j in range(4):

            if board[i][j]:

                value+=(
                    board[i][j]
                    *
                    snake[i][j]
                )

    return value


def max_corner(board):

    m=max(
        max(row)
        for row in board
    )

    corners=[
        board[0][0],
        board[0][3],
        board[3][0],
        board[3][3]
    ]

    return 10000 if m in corners else -10000


def empty_bonus(board):

    return len(empty(board))*500


def merge_bonus(board):

    score=0

    for i in range(4):
        for j in range(3):

            if board[i][j]==board[i][j+1]:
                score+=board[i][j]


    for j in range(4):
        for i in range(3):

            if board[i][j]==board[i+1][j]:
                score+=board[i][j]


    return score*30


def smooth(board):

    penalty=0

    for i in range(4):
        for j in range(3):

            if board[i][j] and board[i][j+1]:

                penalty-=abs(
                    board[i][j]-board[i][j+1]
                )


    return penalty


def evaluate(board):

    return (
        snake_score(board)
        +
        max_corner(board)
        +
        empty_bonus(board)
        +
        merge_bonus(board)
        +
        smooth(board)
    )


import math
import random
from collections import defaultdict


# ==========================
# RANDOM TILE
# ==========================

def add_random_tile(board):

    cells = empty(board)

    if not cells:
        return board


    i,j=random.choice(cells)

    value = 4 if random.random()<0.1 else 2

    new=copy.deepcopy(board)

    new[i][j]=value

    return new


# ==========================
# GAME OVER
# ==========================

def has_moves(board):

    for move in MOVES.values():

        new,_=move(board)

        if new!=board:
            return True

    return False


# ==========================
# RANDOM ROLLOUT
# ==========================

def rollout_move(board):

    best=None
    best_score=-float("inf")


    for name,move in MOVES.items():

        new,gained=move(board)

        if new!=board:

            value=evaluate(new)+gained*100

            if value>best_score:

                best_score=value
                best=name


    return best


def rollout(board,score):

    board=copy.deepcopy(board)


    while has_moves(board):


        # 70% розумний хід
        if random.random()<0.7:

            move = rollout_move(board)


        else:

            move=random.choice(
                list(MOVES.keys())
            )


        new,gained=MOVES[move](board)


        if new==board:
            continue


        board=new
        score+=gained


        board=add_random_tile(board)



    return score


# ==========================
# MCTS NODE
# ==========================

class Node:


    def __init__(self,board,score,parent=None):

        self.board=board
        self.score=score

        self.parent=parent

        self.children=[]

        self.visits=0

        self.reward=0



    def expand(self):

        if self.children:
            return


        for name,move in MOVES.items():


            new,gained=move(self.board)


            if new!=self.board:


                self.children.append(

                    (
                        name,

                        Node(
                            add_random_tile(new),
                            self.score+gained,
                            self
                        )

                    )

                )



    def best_child(self):

        return max(

            self.children,

            key=lambda child:

            (
                child[1].reward /
                (child[1].visits+1)

                +

                1.41 *

                math.sqrt(

                    math.log(self.visits+1)
                    /
                    (child[1].visits+1)

                )

            )

        )


# ==========================
# MCTS SEARCH
# ==========================


def mcts(board,score,iterations=3000):


    root=Node(
        copy.deepcopy(board),
        score
    )


    root.expand()



    for _ in range(iterations):


        node=root



        # SELECT

        while node.children:

            name,node=node.best_child()



        # EXPAND

        node.expand()



        if node.children:

            name,node=random.choice(
                node.children
            )


        # SIMULATE

        result=rollout(
            node.board,
            node.score
        )


        # BACKPROPAGATE

        while node:


            node.visits+=1

            node.reward+=result

            node=node.parent



    best=max(

        root.children,

        key=lambda x:x[1].visits

    )


    return best[0]

# ==========================
# EXPECTIMAX
# ==========================


@lru_cache(maxsize=300000)
def expectimax(board_tuple,depth,player):

    board=list_board(board_tuple)


    if depth==0:

        return evaluate(board)



    if player:


        best=-float("inf")


        for move in MOVES.values():

            new,score=move(board)


            if new!=board:

                value=expectimax(
                    tuple_board(new),
                    depth-1,
                    False
                )

                best=max(best,value+score*100)


        return best



    else:


        cells=empty(board)


        if not cells:

            return evaluate(board)


        total=0


        for i,j in cells:


            for tile,prob in (
                (2,0.9),
                (4,0.1)
            ):


                new=copy.deepcopy(board)

                new[i][j]=tile


                total+=(
                    prob*
                    expectimax(
                        tuple_board(new),
                        depth-1,
                        True
                    )
                )


        return total/len(cells)


# ==========================
# DEPTH CONTROL
# ==========================


def choose_depth(score):

    if score < 10000:
        return 5

    if score < 30000:
        return 6

    return 7


# ==========================
# MAIN
# ==========================


def final_best_move(board, current_score):


    # спочатку Expectimax

    candidates=[]


    for name,move in MOVES.items():

        new,gained=move(board)


        if new!=board:


            value=expectimax(
                tuple_board(new),
                4,
                False
            )


            candidates.append(
                (
                    value,
                    name
                )
            )



    candidates.sort(reverse=True)


    # беремо топ-3 ходи

    top_moves=[
        x[1]
        for x in candidates[:3]
    ]


    # MCTS перевіряє їх

    return mcts(
        board,
        current_score,
        iterations=5000
    )


def print_board(board):

    for row in board:

        print(
            " ".join(
                str(x).rjust(5)
                for x in row
            )
        )
# ── ЯК КОРИСТУВАТИСЯ ────────────────────────────────────

board = [
    [256, 1024, 512, 64],
    [16, 64, 32, 8],
    [4, 32, 8, 4],
    [16, 8, 2, 2],
]
# move, confidence = final_best_move(board, current_score=22000)

score = 0


print_board(board)


move = final_best_move(board, score)


print("Роби хід:", move)

