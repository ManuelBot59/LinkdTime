# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core import Start

if __name__ == "__main__":
    try:
        Start.MAIN.String(1)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("\nExit from Program\n")
