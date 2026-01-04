from collections import Counter

def analyze_log(file_path):
    total_lines = 0
    levels = Counter()

    try:
        with open(file_path, "r") as file:
            for line in file:
                total_lines += 1

                if ":" in line:
                    level = line.split(":", 1)[0].strip().upper()
                    levels[level] += 1

        print("\n=== Log Analysis Report ===")
        print(f"Total log entries: {total_lines}")

        for level, count in levels.items():
            print(f"{level}: {count}")

    except FileNotFoundError:
        print("Log file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("=== Log Analyzer Tool ===")
    path = input("Enter path to log file: ").strip()
    analyze_log(path)


if __name__ == "__main__":
    main()
