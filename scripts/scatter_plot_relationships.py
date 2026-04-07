import os
import pandas as pd
import matplotlib.pyplot as plt


def relationship_label(x: pd.Series, y: pd.Series) -> str:
    if len(x) < 2:
        return "insufficient points"
    slope = (float(y.iloc[-1]) - float(y.iloc[0])) / max(float(x.iloc[-1]) - float(x.iloc[0]), 1e-9)
    if slope > 0:
        return "positive relationship pattern"
    if slope < 0:
        return "negative relationship pattern"
    return "no clear directional pattern"


def detect_outliers_iqr(series: pd.Series) -> int:
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return int(((series < lower) | (series > upper)).sum())


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    input_path = os.path.join(project_root, "data", "raw", "scatter_relationships_sample.csv")
    plot_path = os.path.join(project_root, "outputs", "scatter_relationships_overview.png")
    report_path = os.path.join(project_root, "outputs", "scatter_relationships_report.txt")

    df = pd.read_csv(input_path)

    pairs = [
        ("study_hours", "test_score"),
        ("sleep_hours", "test_score"),
        ("stress_level", "test_score"),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    report_lines = []

    for ax, (x_col, y_col) in zip(axes, pairs):
        ax.scatter(df[x_col], df[y_col], alpha=0.8, edgecolors="black")
        ax.set_title(f"{x_col} vs {y_col}")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.grid(True, linestyle="--", alpha=0.4)

        sorted_df = df.sort_values(x_col)
        pattern = relationship_label(sorted_df[x_col], sorted_df[y_col])
        x_outliers = detect_outliers_iqr(df[x_col])
        y_outliers = detect_outliers_iqr(df[y_col])

        report_lines.append(
            f"- {x_col} vs {y_col}: {pattern}; potential outliers -> {x_col}: {x_outliers}, {y_col}: {y_outliers}"
        )

    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close(fig)

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("Scatter Plot Relationship Report\n")
        report.write("================================\n")
        report.write(f"Input file: {input_path}\n")
        report.write(f"Scatter image: {plot_path}\n\n")
        report.write("Relationship observations:\n")
        for line in report_lines:
            report.write(line + "\n")
        report.write("\nNotes:\n")
        report.write("- Each point represents one observation across two numeric variables.\n")
        report.write("- Scatter plots are used to inspect relationship direction, clusters, and isolated points.\n")
        report.write("- Visual patterns should guide questions before statistical modeling.\n")

    print(f"Scatter plot image saved to: {plot_path}")
    print(f"Relationship report saved to: {report_path}")


if __name__ == "__main__":
    main()
