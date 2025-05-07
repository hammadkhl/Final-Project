import os
import zipfile

# Directory where game files will be written
base = os.path.join(os.path.dirname(__file__), "wavelength_game")

# Map of filename → file-contents
files = {
    "config.py": """# config.py
# Configuration settings for the Wavelength-style game.

SPECTRUM_RANGE = (1, 10)
DEFAULT_EASY_ROUNDS = 5
MAX_HARD_ROUNDS = 3
SCOREBOARD_FILE = "scoreboard.json"
""",
    "clue_database.py": """# clue_database.py
clue_database = [
    {"word": "lava", "spectrum": ("Cold", "Hot"), "position": 10},
    # … rest of entries …
]
""",
    "utils.py": """# utils.py
import random
import json
from config import SPECTRUM_RANGE, SCOREBOARD_FILE

# … utility functions …
""",
    "game_modes.py": """# game_modes.py
import random
import logging
from utils import get_clues_for_position, update_scoreboard, get_random_secret

# … play_easy and play_hard …
""",
    "cli.py": """# cli.py
import argparse
from game_modes import play_easy, play_hard
from config import DEFAULT_EASY_ROUNDS

# … argument parsing and main_cli …
""",
    "main.py": """# main.py
import logging
from cli import main_cli

# … setup_logging and main() …
""",
    "requirements.txt": "# No external dependencies required.\n",
}

# Ensure output directory exists
os.makedirs(base, exist_ok=True)

# Write each file
for filename, content in files.items():
    path = os.path.join(base, filename)
    with open(path, "w") as f:
        f.write(content)

# Create zip archive
zip_path = os.path.join(os.path.dirname(__file__), "wavelength_game.zip")
with zipfile.ZipFile(zip_path, "w") as archive:
    for filename in files:
        archive.write(os.path.join(base, filename), arcname=filename)

print(f"Packaged modular game files into {zip_path}")