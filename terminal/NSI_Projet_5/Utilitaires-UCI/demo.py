import subprocess
import time
import GUI_helper as h

def send_uci_command(process, command):
    process.stdin.write(command + "\n")
    process.stdin.flush()

def receive_uci_response(process):
    response = process.stdout.readline().strip()
    return response

if __name__ == "__main__":
    process = subprocess.Popen(["python", "server.py"],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               universal_newlines=True,
                               text=True)

    h.quick_eval(globals(),locals())

    # Send UCI commands and receive responses
    send_uci_command(process, "uci")
    response = receive_uci_response(process)
    print("Response:", response)

    send_uci_command(process, "isready")
    response = receive_uci_response(process)
    print("Response:", response)

    # Send additional UCI commands and receive responses as needed
    # ...

    # Terminate the server process
    send_uci_command(process, "quit")
    process.terminate()