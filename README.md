# S66-0326-CrashCoders-Applied-Data-Science-CrashLens

Applied Data Science project for crash analysis and predictive modeling.

---

## Question, Data, Insight in Our Project Approach

We treat data science as a flow from a clear question, to trustworthy evidence, to useful insight.

### Starting with the question

We start by defining the decision we want to support, not by opening a dataset first. For us, this is the most important step because it sets boundaries for the whole project. A clear question tells us what matters, what does not, and how we will judge whether the analysis was actually useful.

If we skip this step, we can still produce charts and model outputs, but they may not solve a real problem.

### Using data as evidence

After the question is clear, we treat data as evidence for that question. This means we do not just load columns and run analysis. We first check where the data came from, what each field represents, whether important values are missing, and whether the quality is good enough for reliable conclusions.

Understanding data before analysis helps us avoid false confidence. It also helps us decide whether we need more sources before making claims.

### Turning findings into insight

We consider insight to be the interpretation that can guide action. Numbers alone are not insight. A result becomes insight only when we connect it back to the question and explain what someone should do differently because of it.

For example, saying "weekend nighttime crashes are much higher in one district" is a result. The insight is that safety resources should be prioritized in that district during those hours because that is where near-term impact is likely to be highest.

### How we apply this to a realistic context

In a city road safety planning context, our guiding question would be: which crash conditions and locations should be prioritized first to reduce severe injuries?

To answer that, we would use:

- Police crash records for location, time, severity, weather, light condition, and road characteristics.
- Traffic exposure data so high traffic areas are not automatically treated as high risk.
- Infrastructure data such as speed limits, signal placement, crossings, and lighting.

These sources could come from city open data portals, police reports, and GIS or public works databases.

The most useful insight for decision-making would be a ranked set of high-impact intervention zones, with clear reasons and recommended actions such as lighting upgrades, signal timing changes, or speed calming. That type of output helps leaders allocate resources where safety impact is expected to be strongest.

---

## 🎯 Milestone 1: Environment Verification Status

**Status:** ✅ **VERIFIED AND READY**  
**Verification Date:** March 28, 2026  
**Branch:** `milestone1-environment-verification`

### System Configuration

| Component              | Version             | Status        |
| ---------------------- | ------------------- | ------------- |
| **Operating System**   | macOS 26.3 (Darwin) | ✅ Verified   |
| **Python**             | 3.13.9 (Anaconda)   | ✅ Installed  |
| **Conda**              | 25.11.1             | ✅ Functional |
| **Active Environment** | base                | ✅ Activated  |
| **Jupyter Notebook**   | 7.4.5               | ✅ Running    |
| **JupyterLab**         | 4.4.7               | ✅ Available  |

### Python Installation Verification

**Terminal Commands Executed:**

```bash
$ python --version
Python 3.13.9

$ which python
/Users/fibafathima/anaconda3/bin/python

$ python -c "import sys; print('✓ Python callable'); print(f'✓ Version: {sys.version.split()[0]}')"
✓ Python callable
✓ Version: 3.13.9
```

**Python REPL Tests:** ✓ PASSED

- Basic arithmetic operations
- Module imports (sys, platform)
- String and list operations
- All core functionality working

### Conda Environment Verification

**Terminal Commands Executed:**

```bash
$ conda --version
conda 25.11.1

$ conda info --envs
# conda environments:
base                 *   /Users/fibafathima/anaconda3
                       /opt/anaconda3

$ echo $CONDA_DEFAULT_ENV
base
```

**Environment Status:**

- ✅ Base environment active
- ✅ Conda accessible from terminal
- ✅ Environment variables correctly set
- ✅ Package manager functional

### Jupyter Notebook/Lab Verification

**Terminal Commands Executed:**

```bash
$ which jupyter
/Users/fibafathima/anaconda3/bin/jupyter

$ jupyter --version
Selected Jupyter core packages...
IPython          : 9.7.0
ipykernel        : 6.31.0
jupyterlab       : 4.4.7
notebook         : 7.4.5

$ jupyter kernelspec list
Available kernels:
  python3    /Users/fibafathima/anaconda3/share/jupyter/kernels/python3
```

**Jupyter Functionality:**

- ✅ Jupyter Notebook launches successfully
- ✅ JupyterLab accessible via browser
- ✅ Python kernel connected and responsive
- ✅ Code cells execute without errors
- ✅ Output rendering works correctly

### Essential Data Science Packages

| Package      | Version | Status       |
| ------------ | ------- | ------------ |
| NumPy        | 2.3.5   | ✅ Installed |
| Pandas       | 2.3.3   | ✅ Installed |
| Matplotlib   | 3.10.6  | ✅ Installed |
| Scikit-learn | 1.7.2   | ✅ Installed |
| IPython      | 9.7.0   | ✅ Installed |
| Jupyter Core | 5.8.1   | ✅ Installed |

### Verification Evidence

The following files provide proof of verification:

1. **`environment_verification.ipynb`** - Interactive Jupyter notebook with all verification tests
2. **`verify_setup.sh`** - Automated bash script for complete environment validation
3. **`verify_environment.py`** - Python script for package and dependency checks
4. **`environment.yml`** - Conda environment specification for reproducibility

### How to Verify This Setup

**Quick Verification:**

```bash
# Run the complete verification script
bash verify_setup.sh

# Or verify individual components
python --version
conda --version
jupyter notebook --version

# Launch Jupyter to test
jupyter notebook
```

**Detailed Verification:**

```bash
# Open the verification notebook
jupyter notebook environment_verification.ipynb

# Run all cells to validate environment
```

---

## Project Overview

### Final Project Insights, Assumptions, and Limitations

### Final Insights

- Early data quality checks (missing values, duplicates, and format consistency) significantly improved reliability before any deeper analysis.
- Comparing distributions across columns helped highlight where behavior differs: some variables are stable while others show wider spread and higher variability.
- Histogram and boxplot views made skewness and outlier behavior easier to detect than summary statistics alone.
- Time-based line plots revealed trend direction and abrupt shifts that would be missed in static snapshots.
- Scatter plots helped surface relationship patterns between variables and exposed unusual observations that deserve investigation.

Overall, the major insight from this project is that strong preprocessing and EDA discipline creates trustworthy foundations. Most useful findings came from combining multiple simple methods, not from one metric or one chart.

### Assumptions

- The sample datasets used in milestones are assumed to be representative enough for demonstrating core EDA concepts and workflows.
- Date parsing and formatting assumptions were made using standard parsing behavior and consistent output formats.
- Outlier detection rules (especially IQR and threshold checks) were treated as indicators rather than final truth.
- Relationship and trend interpretations were based on observed patterns in available samples, assuming no hidden domain constraints outside the dataset.
- The workflow assumes contributors run scripts in the documented environment and that generated outputs remain reproducible.

These assumptions were reasonable for milestone-based development, but they should be validated with real production data before high-stakes decisions.

### Limitations

- Most datasets in this repository are small and educational, so conclusions should be treated as methodological demonstrations rather than production findings.
- Visual interpretations (for trend direction, skew, and relationship patterns) are informative but can still be sensitive to sample size and data quality.
- Outlier detection in this project is rule-based and visual; it does not include domain-specific validation or root-cause investigation.
- Time-series analysis here is exploratory and does not include seasonality decomposition or forecasting.
- Scatter-plot relationship checks are descriptive only; they do not establish causation.

Because of these limitations, results should be interpreted as exploratory evidence that guides next questions, not as final decision rules.

### Clarity and Trust Notes

- Each milestone keeps outputs explicit in `data/processed` and `outputs` so reviewers can trace what was generated.
- Reports are written in plain language to make findings understandable without reading every script.
- Decisions (such as flagging outliers without removing them) were kept intentional and explainable to preserve transparency.

This project applies data science techniques to analyze crash data and build predictive models for safety assessment.

### Future Work (Upcoming Milestones)

- Data collection and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model development and training
- Dashboard/application creation

---

## Development Environment

**Setup Instructions for Team Members:**

```bash
# Clone the repository
git clone <repository-url>
cd CrashCoders-Applied-Data-Science-CrashLens

# Create environment from spec (optional)
conda env create -f environment.yml

# Activate environment
conda activate base

# Verify setup
bash verify_setup.sh
```

---

**Milestone 1 Completion:** ✅ Complete  
**Next Milestone:** Data Collection & Preprocessing  
**Last Updated:** March 28, 2026
