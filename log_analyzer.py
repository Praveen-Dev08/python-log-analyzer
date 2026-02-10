import csv
import matplotlib.pyplot as plt


def analyze_log(file_path):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    with open(file_path, "r") as f:
        for line in f:
            for key in counts:
                if key in line:
                    counts[key] += 1

    return counts


def save_txt_report(counts):
    with open("report.txt", "w") as f:
        for k, v in counts.items():
            f.write(f"{k}: {v}\n")


def save_csv_report(counts):
    with open("report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Type", "Count"])
        for k, v in counts.items():
            writer.writerow([k, v])


def show_graph(counts):
    plt.bar(counts.keys(), counts.values())
    plt.title("Log Summary")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.show()


while True:
    print("\n=== LOG ANALYZER ===")
    print("1. Analyze log")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter log file name: ")

        try:
            result = analyze_log(name)

            print("\nSummary:")
            for k, v in result.items():
                print(k, v)

            save_txt_report(result)
            save_csv_report(result)
            show_graph(result)

            print("\n✅ Reports generated")

        except FileNotFoundError:
            print("❌ File not found")

    elif choice == "2":
        break