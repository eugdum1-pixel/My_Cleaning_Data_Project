"""
================================================================================
PROJECT 1: DATA CLEANING & PREPARATION FOR AI TRAINING
================================================================================
Dataset: GlobalWeatherRepository.csv
Purpose: Clean and prepare weather data for MySQL analysis and Tableau visualization

BATTLEPLAN - WHAT I NEED TO DO IN THIS SCRIPT:
================================================================================
STEP 1: Import necessary Python libraries (pandas, numpy, matplotlib, seaborn)
STEP 2: Load the raw GlobalWeatherRepository.csv file from J: drive
STEP 3: Explore the data - check shape, columns, data types, first/last rows
STEP 4: Perform Data Quality Assessment:
        - Count missing values in each column
        - Identify duplicate rows
        - Check for outliers in numerical columns (temperature, precipitation, etc.)
        - Verify data types are correct
STEP 5: Clean the data:
        - Handle missing values (fill, drop, or interpolate based on column)
        - Remove duplicate rows
        - Fix outliers (cap extreme values or remove impossible data)
        - Standardize column names (lowercase, no spaces)
        - Convert data types if needed
STEP 6: Create visualizations to show before/after comparison:
        - Missing values heatmap (before cleaning)
        - Distribution plots for key variables
        - Summary statistics comparison
STEP 7: Validate the cleaned data (ensure quality improved)
STEP 8: Export cleaned dataset as GlobalWeather_CLEANED.csv
================================================================================

WHY THIS MATTERS:
- Raw data is almost never perfect - it has errors, missing values, inconsistencies
- AI/ML models need clean data to work properly (garbage in = garbage out)
- This project demonstrates professional data preparation skills
- The cleaned data will be used in MySQL and Tableau projects

HOW TO RUN THIS SCRIPT:
1. Make sure you have pandas, numpy, matplotlib, seaborn installed
2. Update the file path if your J: drive location is different
3. Run each cell in order (this is a Jupyter notebook)
4. Check the visualizations folder for before/after charts
"""

# ============================================================================
# STEP 1: IMPORT LIBRARIES
# ============================================================================
# WHY: These libraries provide tools for data manipulation and visualization
# - pandas: for reading CSV files and working with tabular data
# - numpy: for numerical operations and handling missing values
# - matplotlib & seaborn: for creating charts and visualizations

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')  # Hide warning messages for cleaner output

# Set display options to see more data
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 100)

print("✓ Libraries imported successfully!")
print(f"Pandas version: {pd.__version__}")
print(f"Numpy version: {np.__version__}")

# ============================================================================
# STEP 2: LOAD THE RAW DATA
# ============================================================================
# WHY: We need to read the CSV file into a pandas DataFrame to work with it
# The DataFrame is like an Excel spreadsheet in Python

# File path - UPDATE THIS if your location is different
data_path = r"J:\........................LEARN_AI\______JustIT-2025-10-27_Regional_DATA\_Final_Project_work\Cleaning_Data_Economic_Datasets\....Proiecte-Portfolio\Case Study The Global Weather Analysis\GlobalWeatherRepository.csv"

print("\n" + "="*80)
print("LOADING RAW DATA...")
print("="*80)

# Read the CSV file
df_raw = pd.read_csv(data_path)

print(f"✓ Data loaded successfully!")
print(f"Dataset shape: {df_raw.shape[0]:,} rows × {df_raw.shape[1]} columns")
print(f"Memory usage: {df_raw.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# ============================================================================
# STEP 3: INITIAL DATA EXPLORATION
# ============================================================================
# WHY: Before cleaning, we need to understand what we're working with
# This helps us identify what problems exist in the data

print("\n" + "="*80)
print("INITIAL DATA EXPLORATION")
print("="*80)

print("\n📋 COLUMN NAMES:")
print("-" * 80)
for i, col in enumerate(df_raw.columns, 1):
    print(f"{i:2d}. {col}")

print("\n📊 DATA TYPES:")
print("-" * 80)
print(df_raw.dtypes)

print("\n🔍 FIRST 5 ROWS:")
print("-" * 80)
print(df_raw.head())

print("\n🔍 LAST 5 ROWS:")
print("-" * 80)
print(df_raw.tail())

print("\n📈 BASIC STATISTICS:")
print("-" * 80)
print(df_raw.describe())

# ============================================================================
# STEP 4: DATA QUALITY ASSESSMENT
# ============================================================================
# WHY: We need to identify all the problems before we can fix them
# This is like a "health check" for the data

print("\n" + "="*80)
print("DATA QUALITY ASSESSMENT")
print("="*80)

# 4.1: Check for missing values
print("\n🔴 MISSING VALUES ANALYSIS:")
print("-" * 80)
missing_values = df_raw.isnull().sum()
missing_percent = (missing_values / len(df_raw)) * 100
missing_df = pd.DataFrame({
    'Column': missing_values.index,
    'Missing_Count': missing_values.values,
    'Missing_Percent': missing_percent.values
})
missing_df = missing_df[missing_df['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False)

if len(missing_df) > 0:
    print(missing_df.to_string(index=False))
    print(f"\n⚠️  Total columns with missing values: {len(missing_df)}")
else:
    print("✓ No missing values found!")

# 4.2: Check for duplicate rows
print("\n🔴 DUPLICATE ROWS ANALYSIS:")
print("-" * 80)
duplicates = df_raw.duplicated().sum()
print(f"Number of duplicate rows: {duplicates:,}")
if duplicates > 0:
    print(f"⚠️  {duplicates:,} duplicate rows found ({duplicates/len(df_raw)*100:.2f}% of data)")
else:
    print("✓ No duplicate rows found!")

# 4.3: Check for outliers in numerical columns
print("\n🔴 OUTLIERS ANALYSIS (Numerical Columns):")
print("-" * 80)
numerical_cols = df_raw.select_dtypes(include=[np.number]).columns.tolist()
print(f"Numerical columns found: {len(numerical_cols)}")

# We'll check for outliers using IQR (Interquartile Range) method
# Outliers are values that fall outside 1.5 * IQR from Q1 and Q3
for col in numerical_cols[:5]:  # Check first 5 numerical columns as example
    Q1 = df_raw[col].quantile(0.25)
    Q3 = df_raw[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df_raw[(df_raw[col] < lower_bound) | (df_raw[col] > upper_bound)][col]
    
    if len(outliers) > 0:
        print(f"  {col}: {len(outliers):,} outliers ({len(outliers)/len(df_raw)*100:.2f}%)")
        print(f"    Range: [{df_raw[col].min():.2f}, {df_raw[col].max():.2f}]")
        print(f"    Expected range: [{lower_bound:.2f}, {upper_bound:.2f}]")

# 4.4: Data type verification
print("\n🔴 DATA TYPE ISSUES:")
print("-" * 80)
print("Checking if any columns need type conversion...")
# This will be specific to your dataset - we'll identify issues after seeing the data

# Save the initial data quality report
print("\n💾 Saving initial data quality report...")
with open('portfolio_projects/project1_data_cleaning/data_quality_report_BEFORE.txt', 'w') as f:
    f.write("="*80 + "\n")
    f.write("DATA QUALITY REPORT - BEFORE CLEANING\n")
    f.write("="*80 + "\n")
    f.write(f"Generated: {datetime.now()}\n\n")
    f.write(f"Dataset Shape: {df_raw.shape[0]:,} rows × {df_raw.shape[1]} columns\n\n")
    f.write("MISSING VALUES:\n")
    f.write(missing_df.to_string(index=False) if len(missing_df) > 0 else "No missing values\n")
    f.write(f"\n\nDUPLICATE ROWS: {duplicates:,}\n")

print("✓ Report saved!")

# ============================================================================
# STEP 5: DATA CLEANING
# ============================================================================
# WHY: Now we fix all the problems we identified
# We'll create a copy of the data so we can compare before/after

print("\n" + "="*80)
print("STARTING DATA CLEANING PROCESS")
print("="*80)

# Create a copy to preserve the original
df_clean = df_raw.copy()

print(f"\n📊 Starting with: {df_clean.shape[0]:,} rows × {df_clean.shape[1]} columns")

# 5.1: Handle missing values
# STRATEGY: Different columns need different approaches
# - For numerical data: fill with median (more robust than mean)
# - For categorical data: fill with mode (most common value) or 'Unknown'
# - If >50% missing: consider dropping the column
# - If entire row is mostly empty: drop the row

print("\n🔧 Step 5.1: Handling missing values...")
initial_rows = len(df_clean)

# Example: Fill numerical columns with median
for col in numerical_cols:
    if df_clean[col].isnull().sum() > 0:
        median_value = df_clean[col].median()
        df_clean[col].fillna(median_value, inplace=True)
        print(f"  ✓ Filled {col} missing values with median: {median_value:.2f}")

# For categorical columns, fill with mode or 'Unknown'
categorical_cols = df_clean.select_dtypes(include=['object']).columns.tolist()
for col in categorical_cols:
    if df_clean[col].isnull().sum() > 0:
        if df_clean[col].mode().shape[0] > 0:
            mode_value = df_clean[col].mode()[0]
            df_clean[col].fillna(mode_value, inplace=True)
            print(f"  ✓ Filled {col} missing values with mode: '{mode_value}'")
        else:
            df_clean[col].fillna('Unknown', inplace=True)
            print(f"  ✓ Filled {col} missing values with 'Unknown'")

print(f"  ✓ Missing values handled! Rows remaining: {len(df_clean):,}")

# 5.2: Remove duplicate rows
print("\n🔧 Step 5.2: Removing duplicate rows...")
df_clean.drop_duplicates(inplace=True)
removed_duplicates = initial_rows - len(df_clean)
print(f"  ✓ Removed {removed_duplicates:,} duplicate rows")
print(f"  ✓ Rows remaining: {len(df_clean):,}")

# 5.3: Handle outliers
# STRATEGY: For weather data, we need to be careful
# - Temperatures: cap at reasonable global extremes (-90°C to 60°C)
# - Precipitation: remove negative values (impossible)
# - We'll cap rather than remove to preserve data

print("\n🔧 Step 5.3: Handling outliers...")
# This will be customized based on your specific columns
# Example for temperature columns:
temp_cols = [col for col in df_clean.columns if 'temp' in col.lower() or 'temperature' in col.lower()]
for col in temp_cols:
    # Cap temperatures at reasonable extremes
    df_clean[col] = df_clean[col].clip(lower=-90, upper=60)
    print(f"  ✓ Capped {col} to range [-90, 60]")

# 5.4: Standardize column names
print("\n🔧 Step 5.4: Standardizing column names...")
# Make all column names lowercase and replace spaces with underscores
df_clean.columns = df_clean.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')
print(f"  ✓ Column names standardized")

# 5.5: Convert data types if needed
print("\n🔧 Step 5.5: Converting data types...")
# Example: Convert date columns to datetime
date_cols = [col for col in df_clean.columns if 'date' in col.lower()]
for col in date_cols:
    try:
        df_clean[col] = pd.to_datetime(df_clean[col], errors='coerce')
        print(f"  ✓ Converted {col} to datetime")
    except:
        print(f"  ⚠️  Could not convert {col} to datetime")

print("\n" + "="*80)
print("✅ DATA CLEANING COMPLETE!")
print("="*80)
print(f"Final dataset: {df_clean.shape[0]:,} rows × {df_clean.shape[1]} columns")
print(f"Rows removed: {df_raw.shape[0] - df_clean.shape[0]:,} ({(df_raw.shape[0] - df_clean.shape[0])/df_raw.shape[0]*100:.2f}%)")

# ============================================================================
# STEP 6: CREATE BEFORE/AFTER VISUALIZATIONS
# ============================================================================
# WHY: Visual proof that our cleaning worked
# These charts will be great for your presentation!

print("\n" + "="*80)
print("CREATING VISUALIZATIONS")
print("="*80)

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# 6.1: Missing values comparison
print("\n📊 Creating missing values comparison...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Before
missing_before = df_raw.isnull().sum()
if missing_before.sum() > 0:
    missing_before[missing_before > 0].plot(kind='barh', ax=ax1, color='red')
    ax1.set_title('Missing Values - BEFORE Cleaning', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Count')
else:
    ax1.text(0.5, 0.5, 'No Missing Values', ha='center', va='center', fontsize=16)
    ax1.set_title('Missing Values - BEFORE Cleaning', fontsize=14, fontweight='bold')

# After
missing_after = df_clean.isnull().sum()
if missing_after.sum() > 0:
    missing_after[missing_after > 0].plot(kind='barh', ax=ax2, color='green')
    ax2.set_title('Missing Values - AFTER Cleaning', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Count')
else:
    ax2.text(0.5, 0.5, 'No Missing Values ✓', ha='center', va='center', fontsize=16, color='green')
    ax2.set_title('Missing Values - AFTER Cleaning', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('portfolio_projects/project1_data_cleaning/visualizations/missing_values_comparison.png', dpi=300, bbox_inches='tight')
print("  ✓ Saved: missing_values_comparison.png")
plt.close()

# 6.2: Data quality summary
print("\n📊 Creating data quality summary...")
fig, ax = plt.subplots(figsize=(10, 6))

metrics = ['Total Rows', 'Total Columns', 'Missing Values', 'Duplicate Rows']
before_values = [df_raw.shape[0], df_raw.shape[1], df_raw.isnull().sum().sum(), df_raw.duplicated().sum()]
after_values = [df_clean.shape[0], df_clean.shape[1], df_clean.isnull().sum().sum(), df_clean.duplicated().sum()]

x = np.arange(len(metrics))
width = 0.35

bars1 = ax.bar(x - width/2, before_values, width, label='Before', color='#ff6b6b')
bars2 = ax.bar(x + width/2, after_values, width, label='After', color='#51cf66')

ax.set_xlabel('Metrics', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Data Quality Metrics - Before vs After Cleaning', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()
ax.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height):,}',
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('portfolio_projects/project1_data_cleaning/visualizations/quality_metrics_comparison.png', dpi=300, bbox_inches='tight')
print("  ✓ Saved: quality_metrics_comparison.png")
plt.close()

print("\n✅ All visualizations created and saved!")

# ============================================================================
# STEP 7: VALIDATE CLEANED DATA
# ============================================================================
# WHY: Final check to make sure everything is good

print("\n" + "="*80)
print("VALIDATION CHECKS")
print("="*80)

print("\n✓ Checking for remaining issues...")
print(f"  Missing values: {df_clean.isnull().sum().sum()}")
print(f"  Duplicate rows: {df_clean.duplicated().sum()}")
print(f"  Total rows: {len(df_clean):,}")
print(f"  Total columns: {len(df_clean.columns)}")

# ============================================================================
# STEP 8: EXPORT CLEANED DATA
# ============================================================================
# WHY: Save the cleaned data for use in MySQL and Tableau projects

print("\n" + "="*80)
print("EXPORTING CLEANED DATA")
print("="*80)

output_path = 'portfolio_projects/project1_data_cleaning/GlobalWeather_CLEANED.csv'
df_clean.to_csv(output_path, index=False)

print(f"\n✅ SUCCESS! Cleaned data exported to:")
print(f"   {output_path}")
print(f"\n📊 Final Statistics:")
print(f"   Rows: {len(df_clean):,}")
print(f"   Columns: {len(df_clean.columns)}")
print(f"   File size: {pd.read_csv(output_path).memory_usage(deep=True).sum() / 1024**2:.2f} MB")

print("\n" + "="*80)
print("🎉 PROJECT 1 COMPLETE!")
print("="*80)
print("\nNext steps:")
print("1. Review the visualizations in the visualizations/ folder")
print("2. Check the cleaned CSV file")
print("3. Move on to Project 2: MySQL Analysis")
print("\nYou can now explain:")
print("- What data quality issues you found")
print("- How you cleaned the data")
print("- Why each cleaning step was necessary")
print("- The impact of cleaning (before/after metrics)")
