import os
import pandas as pd
import matplotlib.pyplot as plt


def interpret_shape(series: pd.Series) -> str:
    skew_value = float(series.skew())
    if skew_value > 0.5:
        return "right-skewed"
    if skew_value < -0.5:
        return "left-skewed"
    return "approximately symmetric"


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    input_path = os.path.join(project_root, "data", "raw", "distribution_comparison_sample.csv")
    combined_plot_path = os.path.join(project_root, "outputs", "histogram_overview.png")
    report_path = os.path.join(project_root, "outputs", "histogram_interpretation_report.txt")

    df = pd.read_csv(input_path)
    numeric_columns = ["delivery_time_min", "daily_orders", "customer_rating", "refund_amount"]

    print("Loaded dataset for histogram visualization.")
    print("Numeric columns selected:", numeric_columns)

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()

    interpretations = []

    for index, column in enumerate(numeric_columns):
        series = df[column].dropna()
        axes[index].hist(series, bins=6, edgecolor="black", color="#4C72B0")
        axes[index].set_title(f"Histogram: {column}")
        axes[index].set_xlabel(column)
        axes[index].set_ylabel("Frequency")

        shape_label = interpret_shape(series)
        interpretations.append(
            {
                "column": column,
                "min": float(series.min()),
                "max": float(series.max()),
                "std_dev": float(series.std()),
                "skew": float(series.skew()),
                "shape": shape_label,
            }
        )

    plt.tight_layout()
    plt.savefig(combined_plot_path)
    plt.close(fig)

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("Histogram Interpretation Report\n")
        report.write("=============================\n")
        report.write(f"Input file: {input_path}\n")
        report.write(f"Histogram image: {combined_plot_path}\n\n")

        report.write("Column-wise observations:\n")
        for item in interpretations:
            report.write(
                f"- {item['column']}: shape={item['shape']}, min={item['min']:.2f}, "
                f"max={item['max']:.2f}, std_dev={item['std_dev']:.2f}, skew={item['skew']:.2f}\n"
            )

        report.write("\nWhy this matters:\n")
        report.write("- Histograms reveal skew, concentration, and unusual tails that summary values alone can hide.\n")
        report.write("- These visuals help identify columns that may need deeper inspection before analysis.\n")

    print(f"Histogram plot saved to: {combined_plot_path}")
    print(f"Interpretation report saved to: {report_path}")


if __name__ == "__main__":
    main()
