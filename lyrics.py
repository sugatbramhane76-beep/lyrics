import time
import sys
import os
import winsound
import random

# -----------------------------
# COLORS
# -----------------------------

PURPLE = "\033[95m"
PINK = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

# -----------------------------
# SETTINGS
# -----------------------------

MUSIC_FILE = "background_music.wav"

lyrics = [
    ("Tum se kiran dhoop ki...", 2),
    ("           tum se siyaah raat hai...", 2),
    ("tum bin main bin baat ka...", 2),
    ("           tum ho tabhi kuch baat hai...", 3),
]



# -----------------------------
# SCREEN
# -----------------------------

os.system("cls")

print()
print(PURPLE + BOLD + "═" * 65 + RESET)
print(PINK + BOLD + "              🎵  T U M   S E  🎵" + RESET)
print(CYAN + BOLD + "             ✨ A MUSICAL MOMENT ✨" + RESET)
print(PURPLE + BOLD + "═" * 65 + RESET)
print()

time.sleep(2)

# -----------------------------
# CHECK MUSIC FILE
# -----------------------------

if not os.path.exists(MUSIC_FILE):
    print(PINK + BOLD + "❌ Music file not found!" + RESET)
    print("Please put 'background_music.wav' in the same folder.")
    sys.exit()

# -----------------------------
# PLAY BACKGROUND MUSIC
# -----------------------------

winsound.PlaySound(
    MUSIC_FILE,
    winsound.SND_FILENAME | winsound.SND_ASYNC
)

# -----------------------------
# LYRICS
# -----------------------------

symbols = ["♡", "♥", "✨", "♪", "💜"]

for line, delay in lyrics:

    print()

    decoration = random.choice(symbols)

    print(
        PURPLE + BOLD +
        "        " + decoration + "  " +
        "═" * 45 +
        RESET
    )

    print()

    # Highlighted lyric
    print(
        PINK + BOLD +
        "              ✦  " +
        RESET,
        end=""
    )

    # Typewriter effect
    for character in line:
        sys.stdout.write(
            WHITE + BOLD + character + RESET
        )
        sys.stdout.flush()
        time.sleep(0.07)

    print()

    print(
        PURPLE + BOLD +
        "        " + decoration + "  " +
        "═" * 45 +
        RESET
    )

    time.sleep(delay)

# -----------------------------
# STOP MUSIC
# -----------------------------

winsound.PlaySound(None, winsound.SND_PURGE)

print()
print(PURPLE + BOLD + "═" * 65 + RESET)
print(
    PINK + BOLD +
    "              💜 ✨ END OF SONG ✨ 💜"
    + RESET
)
print(PURPLE + BOLD + "═" * 65 + RESET)
