# main.py
import logging
from cli import main_cli

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

def main():
    setup_logging()
    main_cli()

if __name__ == "__main__":
    main()