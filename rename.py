import os
import re


def rename_files(directory_path):
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            match = re.match(r"(\d+)\. (.+)", filename)
            if match:
                number = match.group(1).zfill(4)
                title = match.group(2).lower().replace(" ", "-").replace(".", "")
                new_filename = f"{number}-{title}.py"
                os.rename(
                    os.path.join(directory_path, filename),
                    os.path.join(directory_path, new_filename),
                )
                print(f"Renamed '{filename}' to '{new_filename}'")


if __name__ == "__main__":
    rename_files(".")
