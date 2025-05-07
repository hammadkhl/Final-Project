import socket

def run_client():
    host = input("Client: Enter host IP (e.g. 127.0.0.1): ").strip()
    port = int(input("Client: Enter host port: ").strip())

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        data = s.recv(1024).decode()
        low, high, clue = data.split("|", 2)

        print(f"\nSpectrum: {low} ←———→ {high}")
        print(f"Clue word: {clue}\n")

        while True:
            guess = input("Your guess (1–10): ").strip()
            s.sendall(guess.encode())
            resp = s.recv(1024).decode()
            if resp == "YES":
                print("✅ Correct! You got it!")
                break
            elif resp == "NO":
                print("✗ Wrong—try again.")
            else:
                print("✗ Invalid guess; send a number 1–10.")

    print("Client exiting.")
