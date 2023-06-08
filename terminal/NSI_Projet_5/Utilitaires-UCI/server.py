import sys
import echecs
import enum
import UCI_serialize as uc

DEBUG = True
LOG = sys.stderr

if "raw_input" in dir(globals()):
    globals()["input"] = raw_input

try:
    import colorama
except Exception:
    pass

if "colorama" not in globals():
    globals()["colorama"] = type("colorama", (object,), {
        "Fore": type("Fore", (object,), {
            'BLACK': '\x1b[30m', 'BLUE': '\x1b[34m', 'CYAN': '\x1b[36m', 'GREEN': '\x1b[32m', 'LIGHTBLACK_EX': '\x1b[90m', 'LIGHTBLUE_EX': '\x1b[94m', 'LIGHTCYAN_EX': '\x1b[96m', 'LIGHTGREEN_EX': '\x1b[92m', 'LIGHTMAGENTA_EX': '\x1b[95m', 'LIGHTRED_EX': '\x1b[91m', 'LIGHTWHITE_EX': '\x1b[97m', 'LIGHTYELLOW_EX': '\x1b[93m', 'MAGENTA': '\x1b[35m', 'RED': '\x1b[31m', 'RESET': '\x1b[39m', 'WHITE': '\x1b[37m', 'YELLOW': '\x1b[33m'
        })
    })
else:
    colorama.init()

class LogLevel(enum.Enum):
    DEBUG = enum.auto()
    INFO = enum.auto()
    WARNING = enum.auto()
    CRASH = enum.auto()

def log(level, text):
    level_str = str(level).split(".")[1]  # Get the level string without the enum class name
    level_color = colorama.Fore.YELLOW  # Default color
    
    if level == LogLevel.DEBUG:
        level_color = colorama.Fore.BLUE
    elif level == LogLevel.WARNING:
        level_color = colorama.Fore.MAGENTA
    elif level == LogLevel.CRASH:
        level_color = colorama.Fore.RED
    if DEBUG or level == LogLevel.CRASH:
        print("["+level_color+level_str+colorama.Fore.RESET+"] : "+text)


def process_uci_command(command, board):
    # Parse the UCI command and its parameters
    parts = command.split()
    if len(parts) == 0:
        return "Unknown command"
    
    cmd = parts[0]
    
    try:
        input_cmd = InputCommand(cmd)
    except ValueError:
        return "Unknown command"
    
    log(LogLevel.DEBUG,input_cmd)

    return uc.output_command.readyok
    
    # input 'debug', 'go', 'isready', 'ponderhit', 'position', 'quit', 'register', 'setoption', 'stop', 'uci', 'ucinewgame'
    # output 'bestmove', 'copyprotection', 'id', 'info', 'option', 'readyok', 'registration', 'type', 'uciok'

def main():
    log(LogLevel.INFO,"server start")
    board = echecs.EchecsBoard()
    
    while True:
        command = input()
        
        if command == "quit":
            break
        
        response = process_uci_command(command, board)
        log(LogLevel.DEBUG,"return : "+reponse)
        print(response)
        sys.stdout.flush()  # Flush stdout to ensure the response is sent
    print("exit")

if __name__ == "__main__":
    main()