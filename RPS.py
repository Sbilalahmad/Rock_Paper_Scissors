# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
from collections import defaultdict

def player(prev_play, opponent_history=[], my_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)
    else:
        # Reset histories if it's the first game of the match
        opponent_history.clear()
        my_history.clear()

    # Counter strategies for specific bots
    # Strategy to beat Quincy (R, R, P, P, S, repeat)
    if len(opponent_history) >= 5:
        last_five = "".join(opponent_history[-5:])
        if last_five in ["RRPPS", "PPSRR", "PSRRP", "SRRPPS", "RPPSR"]:
            pos = len(opponent_history) % 5
            if pos == 0:
                predicted_move = "R"
            elif pos == 1:
                predicted_move = "R"
            elif pos == 2:
                predicted_move = "P"
            elif pos == 3:
                predicted_move = "P"
            elif pos == 4:
                predicted_move = "S"
            if predicted_move == "R":
                my_next_move = "P"
            elif predicted_move == "P":
                my_next_move = "S"
            else:
                my_next_move = "R"
            my_history.append(my_next_move)
            return my_next_move

    # Strategy to beat Abbey (uses last two moves to predict next)
    if len(opponent_history) >= 4:
        last_two = "".join(opponent_history[-2:])
        counts = defaultdict(int)
        for i in range(len(opponent_history) - 2):
            hist_two = "".join(opponent_history[i:i+2])
            if hist_two == last_two:
                counts[opponent_history[i+2]] += 1
        if counts:
            predicted_move = max(counts, key=counts.get)
            if predicted_move == "R":
                my_next_move = "P"
            elif predicted_move == "P":
                my_next_move = "S"
            else:
                my_next_move = "R"
            my_history.append(my_next_move)
            return my_next_move

    # Strategy to beat Kris (plays to beat our last move)
    if len(my_history) >= 1:
        my_last_move = my_history[-1]
        if my_last_move == "R":
            predicted_move = "P"
        elif my_last_move == "P":
            predicted_move = "S"
        else:
            predicted_move = "R"
        if predicted_move == "R":
            my_next_move = "P"
        elif predicted_move == "P":
            my_next_move = "S"
        else:
            my_next_move = "R"
        my_history.append(my_next_move)
        return my_next_move

    # Strategy to beat Mrugesh (counts our most frequent move and plays to beat it)
    if len(my_history) >= 3:
        my_counts = defaultdict(int)
        for move in my_history:
            my_counts[move] += 1
        if my_counts:
            my_most_frequent = max(my_counts, key=my_counts.get)
            predicted_move = {"R": "P", "P": "S", "S": "R"}[my_most_frequent]
            if predicted_move == "R":
                my_next_move = "P"
            elif predicted_move == "P":
                my_next_move = "S"
            else:
                my_next_move = "R"
            my_history.append(my_next_move)
            return my_next_move

    # Default strategy: counter the opponent's most frequent move
    if opponent_history:
        opp_counts = defaultdict(int)
        for move in opponent_history:
            opp_counts[move] += 1
        if opp_counts:
            opp_most_frequent = max(opp_counts, key=opp_counts.get)
            my_next_move = {"R": "P", "P": "S", "S": "R"}[opp_most_frequent]
            my_history.append(my_next_move)
            return my_next_move

    # Fallback: random move
    my_next_move = random.choice(["R", "P", "S"])
    my_history.append(my_next_move)
    return my_next_move