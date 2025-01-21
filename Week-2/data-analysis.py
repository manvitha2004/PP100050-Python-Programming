import pandas as pd
import matplotlib.pyplot as plt

def data_analyzer():
    print("\n Welcome to DataX - The Basic Data Analysis Tool \n")
    
    file_path = input("Enter the path to the CSV file: ")
    try:
        data = pd.read_csv(file_path)
        print("\n File loaded successfully!\n")
        print(f"Columns available for analysis: {', '.join(data.columns)}")
    except FileNotFoundError:
        print("\n Error: File not found. Please check the file path and try again.")
        return
    except Exception as e:
        print(f"\n Error: {e}")
        return

    while True:
        col_name = input("\nEnter the column name to analyze (or 'exit' to quit): ")
        if col_name.lower() == "exit":
            print("\nThank you for using DataX!")
            break

        if col_name not in data.columns:
            print(f" Column '{col_name}' not found. Please try again.")
            continue

        try:
            numeric_data = pd.to_numeric(data[col_name], errors="coerce").dropna()
            if numeric_data.empty:
                print(f" Column '{col_name}' does not contain valid numerical data.")
                continue

            avg = numeric_data.mean()
            max_val = numeric_data.max()
            min_val = numeric_data.min()

            print(f"\n Analysis of '{col_name}':")
            print(f"  ➡️ Average: {avg:.2f}")
            print(f"  ➡️ Maximum: {max_val:.2f}")
            print(f"  ➡️ Minimum: {min_val:.2f}")

            visualize = input("Would you like to visualize this data? (y/n): ").lower()
            if visualize == "y":
                visualize_col(numeric_data, col_name)

        except Exception as e:
            print(f" Error analyzing column '{col_name}': {e}")

def visualize_col(data, column_name):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=20, color="skyblue", edgecolor="black")
    plt.title(f"Distribution of '{column_name}'", fontsize=16)
    plt.xlabel(column_name, fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()

if __name__ == "__main__":
    data_analyzer()
