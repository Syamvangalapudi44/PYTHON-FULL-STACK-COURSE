import random

def dice():
    return random.randint(1, 6)

player1_score, player2_score = 0, 0

winning_point = 100

ladders = {
    6: 25, 12: 31, 35: 90, 46: 60,
    51: 74, 78: 99, 82: 96
}



snakes = {
    24: 5, 45: 18, 66: 33, 74: 37,
    88: 77, 93: 57, 98: 21
}

while player1_score < winning_point and player2_score < winning_point:
    
    input("Syam's turn. Press Enter to roll dice...")
    roll = dice()
    print("Syam rolled:", roll)
    player1_score += roll

    if player1_score in ladders:
        print("Ladder! Climb up ")
        player1_score = ladders[player1_score]
    elif player1_score in snakes:
        print("Snake! Go down ")
        player1_score = snakes[player1_score]

    print("Syam score:", player1_score, "\n")

    if player1_score >= winning_point:
        print("Syam wins! ")
        break

    input("Tarun's turn. Press Enter to roll dice...")
    roll = dice()
    print("Tarun rolled:", roll)
    player2_score += roll

    if player2_score in ladders:
        print("Ladder! Climb up ")
        player2_score = ladders[player2_score]
    elif player2_score in snakes:
        print("Snake! Go down ")
        player2_score = snakes[player2_score]

    print("Tarun score:", player2_score, "\n")

    if player2_score >= winning_point:
        print("Tarun wins! ")
        break








