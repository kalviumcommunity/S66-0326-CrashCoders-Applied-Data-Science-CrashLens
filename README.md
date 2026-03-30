# S66-0326-CrashCoders-Applied-Data-Science-CrashLens

Applied Data Science project for crash analysis and predictive modeling.

---

## 🎯 Milestone 1: Environment Verification Status

**Status:** ✅ **VERIFIED AND READY**  
**Verification Date:** March 28, 2026  
**Branch:** `milestone1-environment-verification`

### System Configuration

| Component | Version | Status |
|-----------|---------|--------|
| **Operating System** | macOS 26.3 (Darwin) | ✅ Verified |
| **Python** | 3.13.9 (Anaconda) | ✅ Installed |
| **Conda** | 25.11.1 | ✅ Functional |
| **Active Environment** | base | ✅ Activated |
| **Jupyter Notebook** | 7.4.5 | ✅ Running |
| **JupyterLab** | 4.4.7 | ✅ Available |

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

| Package | Version | Status |
|---------|---------|--------|
| NumPy | 2.3.5 | ✅ Installed |
| Pandas | 2.3.3 | ✅ Installed |
| Matplotlib | 3.10.6 | ✅ Installed |
| Scikit-learn | 1.7.2 | ✅ Installed |
| IPython | 9.7.0 | ✅ Installed |
| Jupyter Core | 5.8.1 | ✅ Installed |

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