import os
import pandas as pd
import matplotlib.pyplot as plt


def trend_direction(series: pd.Series) -> str:
    start_value = float(series.iloc[0])
    end_value = float(series.iloc[-1])
    change_ratio = (end_value - start_value) / max(abs(start_value), 1.0)

    if change_ratio > 0.05:
        return "upward trend"
    if change_ratio < -0.05:
        return "downward trend"
    return "roughly stable trend"


def largest_day_change(df: pd.DataFrame, value_column: str) -> tuple[str, float]:
    changes = df[value_column].diff().abs()
    idx = int(changes.idxmax())
    return df.loc[idx, "date"].strftime("%Y-%m-%d"), float(changes.loc[idx])


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    input_path = os.path.join(project_root, "data", "raw", "time_trend_sample.csv")
    plot_path = os.path.join(project_root, "outputs", "time_trend_line_plots.png")
    ordered_data_path = os.path.join(project_root, "data", "processed", "time_trend_sample_ordered.csv")
    report_path = os.path.join(project_root, "outputs", "time_trend_interpretation_report.txt")

    df = pd.read_csv(input_path)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.sort_values("date").reset_index(drop=True)

    df.to_csv(ordered_data_path, index=False)

    metrics = ["daily_active_users", "avg_session_minutes", "error_rate"]

    fig, axes = plt.subplots(3, 1, figsize=(11, 10), sharex=True)

    for ax, metric in zip(axes, metrics):
        ax.plot(df["date"], df[metric], marker="o", linewidth=2)
        ax.set_title(f"Trend: {metric}")
        ax.set_ylabel(metric)
        ax.grid(True, linestyle="--", alpha=0.5)

    axes[-1].set_xlabel("date")
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close(fig)

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("Line Plot Trend Interpretation Report\n")
        report.write("====================================\n")
        report.write(f"Input file: {input_path}\n")
        report.write(f"Ordered data file: {ordered_data_path}\n")
        report.write(f"Line plot image: {plot_path}\n\n")

        report.write("Trend observations:\n")
        for metric in metrics:
            direction = trend_direction(df[metric])
            anomaly_date, anomaly_change = largest_day_change(df, metric)
            report.write(
                f"- {metric}: {direction}; largest day-to-day change on {anomaly_date} "
                f"with absolute change {anomaly_change:.2f}\n"
            )

        report.write("\nNotes:\n")
        report.write("- Data is ordered by date before plotting to preserve temporal meaning.\n")
        report.write("- Sudden spikes or drops are indicators to investigate context, not immediate conclusions.\n")

    print(f"Ordered dataset saved to: {ordered_data_path}")
    print(f"Line plot saved to: {plot_path}")
    print(f"Interpretation report saved to: {report_path}")


if __name__ == "__main__":
    main()
