def get_winner(p1_choice, p2_choice):
    if p1_choice == p2_choice:
        return None  # tie
    elif p1_choice == "rock":
        if p2_choice == "scissors":
            return "Player 1"
        else:
            return "Player 2"
    elif p1_choice == "paper":
        if p2_choice == "rock":
            return "Player 1"
        else:
            return "Player 2"
    elif p1_choice == "scissors":
        if p2_choice == "paper":
            return "Player 1"
        else:
            return "Player 2"
