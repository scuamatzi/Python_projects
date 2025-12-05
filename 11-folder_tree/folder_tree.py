#!/usr/bin/python3
"""
Creates a directory structure of a folder using tree command
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path


def get_user_input():
    """Get filename prefix, path and level depth for tree command from user"""
    valid_levels = [1, 2, 3, 4]

    filename_prefix = input(
        "Enter the base name for the output file (e.g., hd3home): "
    ).strip()

    if not filename_prefix:
        print("Error: Filename prefix cannot be empty.")
        sys.exit(1)

    target_path = input("Enter the path folder to analyze: ").strip()
    if not target_path:
        print("Error: Path cannot be empty.")
        sys.exit(1)

    levels = input("Enter how many levels of depth for tree command [1-4]: ").strip()
    if not levels:
        print("Error: invalid number")
    try:
        levels_int = int(levels)
    except Exception as e:
        print(f"Error: It's not a number: {e}")
        sys.exit(1)

    if not levels_int in valid_levels:
        print("Error: Number must be between 1-4")
        sys.exit(1)

    return filename_prefix, target_path, levels_int


def create_filename_with_date(prefix, levels):
    """Create filename with current date in YYYYMMDD format and levels of depth for tree command"""
    current_date = datetime.now().strftime("%Y%m%d")
    return f"{prefix}_l{levels}_{current_date}.txt"


def validate_path(path):
    """Check if the given path exists and is a directory."""
    path_obj = Path(path)
    if not path_obj.exists():
        print(f"Error: Path '{path}' does not exist!")
        return False

    if not path_obj.is_dir():
        print(f"Error: path '{path}' is not a directory!")
        return False

    return True


def run_tree_command(path, output_filename, levels):
    """
    Execute the tree command with 'n' levels of depth.
    Returns True if successful, False otherwise.
    """
    try:
        print(f"\nAnalyzing directory structure of {path}: \n")
        result = subprocess.run(
            ["tree", "-L", str(levels), path],
            capture_output=True,
            text=True,
            check=True,
        )

        # Save output to file
        with open(output_filename, "w") as f:
            f.write(result.stdout)

        return True

    except subprocess.CalledProcessError as e:
        print(f"Error running tree command {e}")
        if e.stderr:
            print(f"Command stderr: {e.stderr}")
        return False

    except FileNotFoundError:
        print("Error: 'tree' command not found. Please install it using:")
        print("  Ubuntu/Debian: sudo apt install tree")
        print("  macOS: brew install tree")
        print("  CentOS/RHEL: sudo yum install tree")
        return False

    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


def main():
    print("=== Folder structure with tree command ===")

    # Get user input
    filename_prefix, target_path, levels = get_user_input()

    # Validate target path
    if not validate_path(target_path):
        sys.exit(1)

    # Create output filename
    output_filename = create_filename_with_date(filename_prefix, levels)
    print(f"\nOutput will be saved to file: {output_filename}")

    # Run the tree command and save output
    if run_tree_command(target_path, output_filename, levels):
        print(f"\n✓ Success! Directory structure saved to '{output_filename}'")
    else:
        print("\n✗ Failed to create directory structure.")
        sys.exit(1)


if __name__ == "__main__":
    main()
