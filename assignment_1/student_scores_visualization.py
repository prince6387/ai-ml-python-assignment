import requests
import pandas as pd
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


API_URL = "https://example.com/api/students/scores"

SAMPLE = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meena", "John", "Sara"],
    "score": [82, 67, 91, 74, 88]
})


def fetch_scores():
    """Fetch student scores from API."""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        return pd.DataFrame(response.json())

    except (requests.RequestException, ValueError):
        print("API unavailable, using sample data.")
        return SAMPLE.copy()


def main():
    df = fetch_scores()

    df["score"] = pd.to_numeric(
        df["score"],
        errors="coerce"
    )

    df = df.dropna(subset=["score"])

    average = df["score"].mean()

    print(f"Average score: {average:.2f}")

    plt.figure(figsize=(8, 5))

    plt.bar(
        df["name"],
        df["score"]
    )

    plt.axhline(
        average,
        linestyle="--",
        label=f"Average = {average:.2f}"
    )

    plt.xlabel("Student")
    plt.ylabel("Test Score")
    plt.title("Student Test Scores")
    plt.legend()

    plt.tight_layout()

    plt.savefig(
        "scores_chart.png",
        dpi=150
    )


if __name__ == "__main__":
    main()
