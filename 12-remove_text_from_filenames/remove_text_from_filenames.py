import os
import sys


def remove_text_from_filenames():
    """Remove specified text from filenames in the current directory"""

    text_to_remove = input("Enter text you want to remove from filenames: ").strip()

    if not text_to_remove:
        print("No text entered, exiting...")
        sys.exit(1)

    # Get current directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Get all files in the directory
    files = [
        f
        for f in os.listdir(current_dir)
        if os.path.isfile(os.path.join(current_dir, f))
    ]

    if not files:
        print("No files found in the current directory.")
        return

    print(f"\nFound {len(files)} in the current directory.")
    print(f"Looking for text: '{text_to_remove}'")
    print("-" * 50)

    renamed_count = 0
    skipped_count = 0

    for filename in files:
        # Check if the text exists in the filename
        if text_to_remove in filename:
            new_filename = filename.replace(text_to_remove, "")

            # Remove any double spaces that might have been created
            new_filename = new_filename.replace("  ", " ")

            # Remove space before .mp3
            new_filename = new_filename.replace(" .", ".")

            # Get full paths
            old_path = os.path.join(current_dir, filename)
            new_path = os.path.join(current_dir, new_filename)

            # Check if new filename already exists
            if os.path.exists(new_path):
                print(f"Skippin '{filename}' -> '{new_filename}' already exists!! ")
                skipped_count += 1
                continue

            try:
                # Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed: '{filename}' -> '{new_filename}'")
                renamed_count += 1
            except Exception as e:
                print(f"Error renaming '{filename}': {e}")
                skipped_count += 1
        else:
            skipped_count += 1

    print("-" * 50)
    print(f"\nSummary:")
    print(f"Successfully renamed: {renamed_count} file(s)")
    print(f"Skipped: {skipped_count} file(s)")

    if renamed_count > 0:
        print("\nNote: All renames have been completed successfully.")
    else:
        print("\nNo files were renamed.")


def main():
    """Cut text given from filename in directory."""

    print("\nThis script will remove specified text from filenames")
    print("in the current directory where this script is located.")
    print("\nWARNING: This action cannot be undone!")
    print("\nExample: 'My song (Audio).mp3' -> 'My song.mp3'")

    # Ask for confirmation
    confirmation = input("\Do you want to continue? (y/n): ").strip().lower()

    if confirmation in ["y", "yes"]:
        remove_text_from_filenames()
    else:
        print("Operation Cancelled!")


if __name__ == "__main__":
    main()
