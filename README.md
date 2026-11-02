# Python Programming Demonstration — University of Tartu MSc Application (2025)

**Status:** Historical project — no longer maintained.

## Overview

This repository contains a Python programming demonstration originally prepared in March 2025 to support my admission application to the **Master of Science in Computer Science programme at the University of Tartu, Estonia**.

The demonstration illustrates basic programming skills involving synthetic data generation, data manipulation, spreadsheet automation, and the use of Python libraries.

## Functionality

The Python script generates simulated semiconductor wafer-testing data for 25 wafers, with four test sites per wafer (100 records in total).

Each test site is assigned a testing volume of 250 units. Randomized failure counts are generated across eight categories (`Bin2` through `Bin9`), and the remaining units are recorded as passing.

The script performs two stages of processing:

**Part 1 — Data generation:** Creates the synthetic dataset using NumPy and Pandas and exports it to `Generated_XLSX.xlsx`.

**Part 2 — Spreadsheet analysis:** Uses OpenPyXL to add Excel formulas identifying the maximum failure-bin count for each test site, formats the data as an Excel table, and saves the result to `ANALYZED_XLSX.xlsx`.

The generated data is entirely synthetic and does not represent actual semiconductor test measurements.

## Requirements and execution

The script requires Python 3 and the following third-party libraries: `numpy`, `pandas`, and `openpyxl`.

Install the dependencies:

`python -m pip install numpy pandas openpyxl`

Run the script:

`python ut-ee_mar-2025_programming-demo.py`

Both Excel workbooks are generated in the current working directory. Existing files with the same names will be overwritten.

The generated data may differ between executions because no fixed random seed is used. Excel formulas may require opening the analyzed workbook in a compatible spreadsheet application for calculation.

## Historical note

This repository is preserved as a record of the programming demonstration submitted during my 2025 university admission application.

The original Python source code has been retained for historical reference. This is not an actively developed or maintained software project.
