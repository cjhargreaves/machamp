import sys
import time

from scheduler import Scheduler

scheduler = Scheduler()


def main():
    scheduler.start()

    print("Commands: submit <command> | status | quit")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nStopping.")
            scheduler.stop()
            break

        if not line:
            continue
        elif line == "quit":
            scheduler.stop()
            break
        elif line == "status":
            scheduler.status()
        elif line.startswith("submit "):
            command = line[len("submit "):]
            scheduler.submit(command)
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
