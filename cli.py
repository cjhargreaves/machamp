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
            parts = line[len("submit "):].split("--vram ", 1)
            command = parts[0].strip()
            vram_mb = int(parts[1].strip()) if len(parts) > 1 else 0
            scheduler.submit(command, vram_mb=vram_mb)
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
