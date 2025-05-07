import json
import random

from config import SPECTRUM_RANGE, SCOREBOARD_FILE

def get_random_secret():
    """Pick a secret number in the configured spectrum range."""
    return random.randint(*SPECTRUM_RANGE)

def get_clues_for_position(position):
    """Return all clue dicts matching the given position."""
    from clue_database import clue_database
    return [c for c in clue_database if c["position"] == position]

def load_scoreboard():
    """Load or initialize the scoreboard (wins/losses by mode)."""
    default = {
        "Easy":   {"wins": 0, "losses": 0},
        "Medium": {"wins": 0, "losses": 0},
        "Harvard":{"wins": 0, "losses": 0},
    }
    try:
        with open(SCOREBOARD_FILE) as f:
            data = json.load(f)
            for m in default:
                data.setdefault(m, default[m])
            return data
    except Exception:
        return default

def save_scoreboard(sb):
    """Persist the scoreboard back to disk."""
    with open(SCOREBOARD_FILE, "w") as f:
        json.dump(sb, f, indent=2)

def update_scoreboard(mode, won):
    """Increment win/loss for the given mode."""
    sb = load_scoreboard()
    if won:
        sb[mode]["wins"] += 1
    else:
        sb[mode]["losses"] += 1
    save_scoreboard(sb)