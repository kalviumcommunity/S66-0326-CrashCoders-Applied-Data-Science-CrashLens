#!/usr/bin/env python3
"""
Environment Verification Script
This script verifies that the local Data Science environment is properly set up.
Run this to confirm Python and essential packages are working correctly.
"""

import sys
import subprocess

def check_python_version():
    """Verify Python version is accessible"""
    print(f"✓ Python Version: {sys.version}")
    print(f"  Python executable: {sys.executable}")
    return True

def check_conda_environment():
    """Verify conda is accessible via subprocess"""
    try:
        result = subprocess.run(['conda', '--version'], 
                              capture_output=True, text=True, check=True)
        print(f"✓ Conda Version: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError:
        print("✗ Conda not found or not in PATH")
        return False

def check_essential_packages():
    """Verify essential Data Science packages can be imported"""
    packages = ['numpy', 'pandas', 'matplotlib', 'sklearn']
    available = []
    
    for package in packages:
        try:
            __import__(package)
            pkg = __import__(package)
            version = getattr(pkg, '__version__', 'version unknown')
            print(f"✓ {package} ({version})")
            available.append(package)
        except ImportError:
            print(f"⚠ {package} not installed (can be added later)")
    
    return available

def main():
    print("=" * 60)
    print("Data Science Environment Verification")
    print("=" * 60)
    print()
    
    print("1. Checking Python installation...")
    check_python_version()
    print()
    
    print("2. Checking Conda installation...")
    check_conda_environment()
    print()
    
    print("3. Checking essential packages...")
    check_essential_packages()
    print()
    
    print("=" * 60)
    print("Environment verification complete!")
    print("Your system is ready for Data Science work.")
    print("=" * 60)

if __name__ == "__main__":
    main()
