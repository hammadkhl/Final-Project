import socket

def run_server():
    host = "0.0.0.0"
    port = int(input("Host: Enter port to listen on (e.g. 5000): ").strip())
    secret = int(input("Host: Pick a secret number (1–10): ").strip())
    low = input("Host: Enter low-end spectrum label: ").strip()
    high = input("Host: Enter high-end spectrum label: ").strip()
    clue = input("Host: Enter your clue word: ").strip()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"Waiting for player to connect on port {port}…")
        conn, addr = s.accept()
        with conn:
            print(f"Player connected from {addr}")
            # send spectrum and clue
            conn.sendall(f"{low}|{high}|{clue}".encode())

            while True:
                data = conn.recv(1024).decode().strip()
                if not data:
                    break
                print(f"Player guessed: {data}")
                try:
                    guess = int(data)
                except ValueError:
                    resp = "INVALID"
                else:
                    resp = "YES" if guess == secret else "NO"

                conn.sendall(resp.encode())
                if resp == "YES":
                    print("Player got it right—ending game.")
                    break

    print("Server shutting down.")