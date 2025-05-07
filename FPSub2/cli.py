# cli.py
import argparse
from game_modes import play_easy, play_hard
from config import DEFAULT_EASY_ROUNDS, MAX_HARD_ROUNDS

def parse_args():
    parser = argparse.ArgumentParser(description="Wavelength-style guessing game.")
    parser.add_argument("--mode", choices=["easy", "hard"], required=True, help="Game mode to play.")
    parser.add_argument("--rounds", type=int, default=DEFAULT_EASY_ROUNDS,
                        help="Number of rounds for easy mode.")
    parser.add_argument("--show-scoreboard", action="store_true",
                        help="Display the current scoreboard and exit.")
    return parser.parse_args()

def show_scoreboard():
    from utils import load_scoreboard
    sb = load_scoreboard()
    print("Scoreboard:")
    for mode, stats in sb.items():
        print(f"  {mode.title()}: {stats['wins']} wins, {stats['losses']} losses")

def main_cli():
    args = parse_args()
    if args.show_scoreboard:
        show_scoreboard()
    else:
        if args.mode == "easy":
            play_easy(args.rounds)
        else:
            play_hard()