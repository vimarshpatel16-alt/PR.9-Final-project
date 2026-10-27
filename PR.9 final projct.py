
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 55)
print("     GLOBAL HAPPINESS REPORT ANALYSIS")
print("=" * 55)

try:
 
    url = "https://raw.githubusercontent.com/VStanys/CSV-WHR/main/world-happiness-report.csv"

    df = pd.read_csv(url)

    print("\nDataset loaded successfully!")
    print("\nFirst 5 rows:")
    print(df.head())

    print("\nDataset shape:", df.shape)
    print("\nColumn names:")
    print(df.columns.tolist())

    df.columns = df.columns.str.strip()

    df = df.dropna(subset=["Country name", "Life Ladder"])

    latest_year = df["year"].max()
    latest = df[df["year"] == latest_year].copy()

    print("\nLatest year:", latest_year)

    top10 = latest.nlargest(10, "Life Ladder")

    print("\nTop 10 Happiest Countries:")
    print(top10[["Country name", "Life Ladder"]].to_string(index=False))

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=top10,
        x="Life Ladder",
        y="Country name"
    )

    plt.title("Top 10 Happiest Countries")
    plt.xlabel("Happiness Score")
    plt.ylabel("Country")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))

    sns.histplot(data=latest, x="Life Ladder", bins=20, kde=True)

    plt.title("Distribution of Happiness Scores")
    plt.xlabel("Happiness Score")
    plt.ylabel("Number of Countries")
    plt.tight_layout()
    plt.show()

    gdp_data = latest.dropna(subset=["Log GDP per capita"])

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=gdp_data,
        x="Log GDP per capita",
        y="Life Ladder"
    )

    plt.title("GDP vs Happiness")
    plt.xlabel("Log GDP per Capita")
    plt.ylabel("Happiness Score")
    plt.tight_layout()
    plt.show()

    support_data = latest.dropna(subset=["Social support"])

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=support_data,
        x="Social support",
        y="Life Ladder"
    )

    plt.title("Social Support vs Happiness")
    plt.xlabel("Social Support")
    plt.ylabel("Happiness Score")
    plt.tight_layout()
    plt.show()

    factors = [
        "Life Ladder",
        "Log GDP per capita",
        "Social support",
        "Healthy life expectancy at birth",
        "Freedom to make life choices",
        "Generosity",
        "Perceptions of corruption"
    ]

    available = [col for col in factors if col in latest.columns]

    plt.figure(figsize=(10, 7))

    sns.heatmap(
        latest[available].corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Between Happiness Factors")
    plt.tight_layout()
    plt.show()

    trend = df.groupby("year")["Life Ladder"].mean().reset_index()
    plt.figure(figsize=(10, 5))

    plt.plot(
        trend["year"],
        trend["Life Ladder"],
        marker="o"
    )

    plt.title("Average Happiness Over Time")
    plt.xlabel("Year")
    plt.ylabel("Average Happiness Score")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print("\nHAPPINESS DATA SUMMARY")
    print("-" * 40)

    print("Total countries in latest year:",
          latest["Country name"].nunique())

    print("Average happiness score:",
          round(latest["Life Ladder"].mean(), 2))

    print("Highest happiness score:",
          round(latest["Life Ladder"].max(), 2))

    print("Lowest happiness score:",
          round(latest["Life Ladder"].min(), 2))

    df.to_csv("happiness_cleaned_data.csv", index=False)

    top10.to_csv("top_10_happiest_countries.csv", index=False)

    print("\nCleaned dataset saved successfully!")
    print("Top 10 countries saved successfully!")
    print("\nProject completed successfully!")

except Exception as e:
    print("\nAn error occurred:", e)
    print("Check your internet connection and dataset URL.")
