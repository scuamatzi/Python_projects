import os
import random


def randomize_and_numbering():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    all_files = [f for f in os.listdir(current_dir) if os.path.isfile(f)]

    mp3_files = [file for file in all_files if file.endswith(".mp3")]

    if not mp3_files:
        print("\nNo mp3 files found in current directory.")
        return

    # randomize_files = random.sample(all_files, len(all_files))
    # print(randomize_files[0], randomize_files[1], randomize_files[2])
    numbers = [f"{i:02d}" for i in range(1, len(mp3_files) + 1)]
    randomize_numbers = random.sample(numbers, len(numbers))
    # print(numbers)

    new_mp3_files = [
        f"{randomize_numbers[i]}-{mp3_files[i]}" for i in range(len(mp3_files))
    ]

    # print(new_mp3_files)

    # print(len(new_mp3_files))

    for i in range(len(mp3_files)):
        # Check if new mp3 filename exists
        if os.path.exists(new_mp3_files[i]):
            print(
                f"Skipping '{mp3_files[i]}' -> '{new_mp3_files[i]}, already exists!!'"
            )
            continue

        try:
            # Rename file
            os.rename(mp3_files[i], new_mp3_files[i])
            print(f"Renamed: '{mp3_files[i]}' -> '{new_mp3_files[i]}'")
        except Exception as e:
            print(f"Error renaiming '{mp3_files[i]}': {e}")


def main():
    print("\nThis script will rename mp3 files like:  cancion.mp3 -> 01-cancion.mp3")
    print("But first it will randomize the order of the songs.")
    print("\nThis proccess can not be undone.")
    confirmation = input("\nContinue with the script? (y/n):  ").strip().lower()

    if confirmation in ["y", "yes"]:
        randomize_and_numbering()
    else:
        print("Operation cancelled!")


if __name__ == "__main__":
    main()
