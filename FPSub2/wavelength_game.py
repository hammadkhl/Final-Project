from game_modes       import play_easy, play_medium, play_harvard
import two_player_server, two_player_client

def main():
    print("\n🎉 Welcome to Wavelength-Style Guessing Game!\n")
    while True:
        choice = input("Choose mode: [E]asy, [M]edium, [H]arvard, [T]wo-player, [Q]uit: ").strip().upper()
        if choice == "E":
            play_easy()
        elif choice == "M":
            play_medium()
        elif choice == "H":
            play_harvard()
        elif choice == "T":
            sub = input("Two-Player: Host or Join? [H]/[J]: ").strip().upper()
            if sub == "H":
                two_player_server.run_server()
            elif sub == "J":
                two_player_client.run_client()
            else:
                print("❗ Invalid—enter H or J.")
        elif choice == "Q":
            print("\nGoodbye—and thanks for playing!\n")
            break
        else:
            print("❗ Invalid choice. Enter E, M, H, T, or Q.")

if __name__ == "__main__":
    main()
