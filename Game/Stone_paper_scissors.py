import random

CHOICES = ["Stone", "Paper", "Scissors"]

WINS_AGAINST = {
    "Stone":    "Scissors",   
    "Paper":    "Stone",      
    "Scissors": "Paper",      
}

WIN_MESSAGE = {
    ("Stone",    "Scissors"): "Stone crushes Scissors",
    ("Paper",    "Stone"):    "Paper covers Stone",
    ("Scissors", "Paper"):   "Scissors cuts Paper",
}


def display_banner():
    """Print the game title banner."""
    print("\n" + "=" * 42)
    print("   STONE – PAPER – SCISSORS ")
    print("=" * 42)


def display_menu():
    """Print the main menu and return the validated user choice."""
    print("\n MAIN MENU")
    print("  1. Play a round")
    print("  2. View scoreboard")
    print("  3. Reset scores")
    print("  4. Quit")
    return input("\nEnter your choice (1-4): ").strip()


def display_choices():
    """Print the move menu and return the player's chosen move."""
    print("\n  Choose your move:")
    for idx, choice in enumerate(CHOICES, start=1):
        print(f"  {idx}. {choice}")
    return input("\nEnter 1, 2 or 3: ").strip()


# ──────────────────────────────────────────────
#  Core game logic
# ──────────────────────────────────────────────
def get_computer_choice() -> str:
    return random.choice(CHOICES)


def get_player_choice() -> str | None:
    
    raw = display_choices()
    if raw in ("1", "2", "3"):
        return CHOICES[int(raw) - 1]
    print("Invalid choice – please enter 1, 2, or 3.")
    return None


def determine_winner(player: str, computer: str) -> str:
    
    if player == computer:
        return "draw"
    if WINS_AGAINST[player] == computer:
        return "player"
    return "computer"


def play_round(scores: dict) -> None:
    player_choice = get_player_choice()
    if player_choice is None:
        return                          # bad input → skip round

    computer_choice = get_computer_choice()

    print(f"\n  You chose    : {player_choice}")
    print(f"  Computer chose: {computer_choice}")
    print("-" * 36)

    result = determine_winner(player_choice, computer_choice)

    if result == "draw":
        print("   It's a DRAW!")
    elif result == "player":
        reason = WIN_MESSAGE[(player_choice, computer_choice)]
        print(f"  YOU WIN!  ({reason})")
        scores["player"] += 1
    else:
        reason = WIN_MESSAGE[(computer_choice, player_choice)]
        print(f"   COMPUTER WINS!  ({reason})")
        scores["computer"] += 1

    scores["rounds"] += 1


# ──────────────────────────────────────────────
#  Scoreboard helpers
# ──────────────────────────────────────────────
def display_scoreboard(scores: dict) -> None:
    """Print the current scoreboard."""
    print("\n📊  SCOREBOARD")
    print("=" * 28)
    print(f"  Rounds played : {scores['rounds']}")
    print(f"   Your wins  : {scores['player']}")
    print(f"   CPU wins   : {scores['computer']}")
    draws = scores["rounds"] - scores["player"] - scores["computer"]
    print(f"  🤝 Draws      : {draws}")
    print("=" * 28)


def reset_scores(scores: dict) -> None:
    """Zero out all score counters."""
    scores["player"] = 0
    scores["computer"] = 0
    scores["rounds"] = 0
    print("\n  Scores have been reset.")


# ──────────────────────────────────────────────
#  Main program loop
# ──────────────────────────────────────────────
def main():
    scores = {"player": 0, "computer": 0, "rounds": 0}
    display_banner()

    while True:
        action = display_menu()

        if action == "1":
            play_round(scores)
        elif action == "2":
            display_scoreboard(scores)
        elif action == "3":
            reset_scores(scores)
        elif action == "4":
            display_scoreboard(scores)
            print("\n Thanks for playing – goodbye!\n")
            break
        else:
            print(" Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()