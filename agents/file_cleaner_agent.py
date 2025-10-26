import os
import shutil
from datetime import datetime

class FileCleanerAgent:
    def __init__(self, target_directory):
        self.target_directory = target_directory
        self.file_types = {
            "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
            "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
            "Videos": [".mp4", ".mov", ".avi", ".mkv"],
            "Audio": [".mp3", ".wav", ".flac"],
            "Archives": [".zip", ".rar", ".7z"],
            "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"]
        }

    def scan_directory(self):
        """Return files only, skip folders."""
        return [f for f in os.listdir(self.target_directory)
                if os.path.isfile(os.path.join(self.target_directory, f))]

    def organize_files(self):
        """Organize files into folders by type."""
        for file_name in self.scan_directory():
            file_path = os.path.join(self.target_directory, file_name)

            # Skip hidden/system files
            if file_name.startswith("."):
                continue

            moved = False
            for folder, extensions in self.file_types.items():
                if file_name.lower().endswith(tuple(extensions)):
                    folder_path = os.path.join(self.target_directory, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, file_name))
                    print(f"✅ Moved: {file_name} → {folder}")
                    moved = True
                    break

            if not moved:
                print(f"⚠️ Skipped (unknown type): {file_name}")

    def log_action(self, message):
        """Log to logs/actions.log."""
        log_path = os.path.join("logs", "actions.log")
        with open(log_path, "a") as log_file:
            log_file.write(f"{datetime.now()} - {message}\n")

    def run(self):
        print(f"🚀 Starting cleanup in: {self.target_directory}")
        self.organize_files()
        self.log_action(f"Cleanup completed in {self.target_directory}")
        print("✨ Cleaning complete!")
