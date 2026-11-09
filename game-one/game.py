
import random
 
ROCK, PAPER, SCISSORS = 0, 1, 2
NAMES = ["rock", "paper", "scissors"]
 
 
 
def round_result(move1, move2):
    """Return "win", "lose", or "tie" for player 1."""
    if move1 == move2:
        return "tie"
    if (move1, move2) in [(ROCK, SCISSORS), (SCISSORS, PAPER), (PAPER, ROCK)]:
        return "win"
    return "lose"
 
 
def update_scores(score1, score2, result):
    """Return the new (score1, score2) after one round."""
    if result == "win":
        score1 += 1
    elif result == "lose":
        score2 += 1
    return score1, score2
 
 
def match_winner(score1, score2):
    """Return "Player 1", "Player 2", or "Draw"."""
    if score1 > score2:
        return "Player 1"
    if score2 > score1:
        return "Player 2"
    return "Draw"
 
 

def beat_last_strategy(round_number, opponent_previous):
    """Play the move that beats the opponent's last move. Start with paper."""
    if opponent_previous == -1:
        return PAPER
    return (opponent_previous + 1) % 3
 
 
def rotate_strategy(round_number, opponent_previous):
    """Rock, paper, scissors in order by round number."""
    return (round_number - 1) % 3
 
 
def computer_move(round_number, opponent_previous):
    """Random move. Each one is equally likely."""
    return random.randint(0, 2)
 
 
def human_move(round_number, opponent_previous):
    """Ask the person until they type 0, 1, or 2."""
    while True:
        text = input(f"Round {round_number} - 0=rock 1=paper 2=scissors: ")
        if text in ["0", "1", "2"]:
            return int(text)
        print("Please type 0, 1, or 2.")
 
 
def choose_player(choice):
    """Menu choice -> player function, or None if not a choice."""
    players = {"1": human_move, "2": beat_last_strategy, "3": rotate_strategy}
    return players.get(choice)
 
 

 
def play_game(player1, player2, rounds=5):
    """Play the match, print each round, return the final scores."""
    score1, score2 = 0, 0
    last1, last2 = -1, -1
    for round_number in range(1, rounds + 1):
        # Both moves are chosen before anything is shown.
        move1 = player1(round_number, last2)
        move2 = player2(round_number, last1)
        result = round_result(move1, move2)
        score1, score2 = update_scores(score1, score2, result)
        print(f"Round {round_number}: {NAMES[move1]} vs {NAMES[move2]} "
              f"-> {result}. Score {score1}-{score2}")
        last1, last2 = move1, move2
    winner = match_winner(score1, score2)
    print("The match is a draw." if winner == "Draw" else f"{winner} wins the match!")
    return score1, score2
 
 
if __name__ == "__main__":
    choice = input("Player 1: 1=human  2=beat-last strategy  3=rotate strategy: ")
    while choose_player(choice) is None:
        choice = input("Please type 1, 2, or 3: ")
    play_game(choose_player(choice), computer_move)
 