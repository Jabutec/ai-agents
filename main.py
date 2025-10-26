from agents.file_cleaner_agent import FileCleanerAgent

def main():
    # List of folders you want the agent to clean
    folders_to_clean = [
        r"C:\Users\mokoe\Downloads",
        r"C:\Users\mokoe\Desktop",
        r"C:\Users\mokoe\Documents"
    ]

    for folder in folders_to_clean:
        print("\n==============================")
        print(f"🧹 Cleaning folder: {folder}")
        print("==============================")

        cleaner = FileCleanerAgent(folder)
        cleaner.run()

if __name__ == "__main__":
    main()
