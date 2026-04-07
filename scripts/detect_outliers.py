import os
import pandas as pd
import matplotlib.pyplot as plt


def iqr_bounds(series: pd.Series) -> tuple[float, float, float, float, float]:
    q1 = float(series.quantile(0.25))
    q3 = float(series.quantile(0.75))
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return q1, q3, iqr, lower, upper


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    input_path = os.path.join(project_root, "data", "raw", "outlier_detection_sample.csv")
    boxplot_path = os.path.join(project_root, "outputs", "outlier_boxplots.png")
    scatter_path = os.path.join(project_root, "outputs", "outlier_scatter.png")
    flagged_path = os.path.join(project_root, "data", "processed", "outlier_flags.csv")
    report_path = os.path.join(project_root, "outputs", "outlier_detection_report.txt")

    df = pd.read_csv(input_path)
    numeric_columns = ["transaction_amount", "delivery_time_min", "customer_visits"]

    # Visual inspection: boxplots for each numeric column.
    plt.figure(figsize=(10, 6))
    df[numeric_columns].boxplot(grid=True)
    plt.title("Outlier Inspection via Boxplots")
    plt.ylabel("Value")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(boxplot_path)
    plt.close()

    # Visual inspection: scatter plot of two key variables.
    plt.figure(figsize=(8, 5))
    plt.scatter(df["transaction_amount"], df["delivery_time_min"], edgecolors="black", alpha=0.8)
    plt.title("Outlier Inspection via Scatter Plot")
    plt.xlabel("transaction_amount")
    plt.ylabel("delivery_time_min")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(scatter_path)
    plt.close()

    flags = pd.DataFrame({"record_id": df["record_id"]})
    summary_lines = []

    for col in numeric_columns:
        q1, q3, iqr, lower, upper = iqr_bounds(df[col])
        flag_col = f"{col}_iqr_flag"
        flags[flag_col] = (df[col] < lower) | (df[col] > upper)

        flagged_values = df.loc[flags[flag_col], ["record_id", col]]
        summary_lines.append(
            f"- {col}: q1={q1:.2f}, q3={q3:.2f}, iqr={iqr:.2f}, lower={lower:.2f}, upper={upper:.2f}, flagged={int(flags[flag_col].sum())}"
        )

        # Simple threshold checks as additional indicators.
        if col == "transaction_amount":
            threshold_flag = df[col] > 500
            flags[f"{col}_threshold_flag"] = threshold_flag
        elif col == "delivery_time_min":
            threshold_flag = df[col] > 60
            flags[f"{col}_threshold_flag"] = threshold_flag
        elif col == "customer_visits":
            threshold_flag = df[col] > 20
            flags[f"{col}_threshold_flag"] = threshold_flag

    flags["any_outlier_flag"] = flags.drop(columns=["record_id"]).any(axis=1)
    flagged_records = df.loc[flags["any_outlier_flag"]].copy()
    flagged_records = flagged_records.merge(flags, on="record_id", how="left")
    flagged_records.to_csv(flagged_path, index=False)

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("Outlier Detection Report\n")
        report.write("========================\n")
        report.write(f"Input file: {input_path}\n")
        report.write(f"Boxplot image: {boxplot_path}\n")
        report.write(f"Scatter image: {scatter_path}\n")
        report.write(f"Flagged records file: {flagged_path}\n\n")

        report.write("IQR rule summary:\n")
        for line in summary_lines:
            report.write(line + "\n")

        report.write("\nInterpretation notes:\n")
        report.write("- Outlier flags are indicators for review, not automatic deletion signals.\n")
        report.write("- Some outliers may be valid rare events rather than data errors.\n")
        report.write("- Next steps should be decided using domain context and source validation.\n")

    print(f"Boxplot saved to: {boxplot_path}")
    print(f"Scatter plot saved to: {scatter_path}")
    print(f"Flagged records saved to: {flagged_path}")
    print(f"Report saved to: {report_path}")


if __name__ == "__main__":
    main()
