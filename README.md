# Swindon Real Estate Analysis

A comprehensive Python-based analysis tool for real estate data in the Swindon area, focusing on property prices, market trends, and postcode-based analysis.

## Overview

This project provides tools for scraping, analyzing, and visualizing real estate data from Rightmove for the Swindon area. It includes functionality for data collection, analysis, visualization, and change tracking across different time periods.

## Features

- **Data Collection**: Automated scraping of property listings from Rightmove
- **Data Analysis**: Statistical analysis of property prices by postcode and property type
- **Visualization**: Interactive plots and charts using Plotly and Matplotlib
- **Change Tracking**: Comparison of data across different time periods
- **Postcode Mapping**: Integration with Swindon area postcode data

## Project Structure

```
Swindon-RealEstate-Analysis/
├── analysis.py              # Basic price analysis and box plots
├── plots.py                 # Advanced visualization with Plotly
├── changelog.py            # CSV file comparison tool
├── rightmove-get.py        # Data scraping from Rightmove
├── requirements.txt         # Python dependencies
├── swindon/                # Data storage directory
└── *.csv                   # Property data files
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Swindon-RealEstate-Analysis
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

- `pandas>=1.5.0` - Data manipulation and analysis
- `matplotlib>=3.5.0` - Basic plotting
- `seaborn>=0.11.0` - Statistical data visualization
- `plotly>=5.0.0` - Interactive plotting
- `rightmove-webscraper>=1.0.0` - Web scraping from Rightmove

## Usage

### 1. Data Collection (`rightmove-get.py`)

Scrapes property data from Rightmove for Swindon area postcodes:

```bash
python rightmove-get.py
```

**Features:**
- Collects data for postcodes SN1-SN99
- Filters for 3+ bedroom properties
- Price range: £200,000 - £1,000,000
- Includes properties with garden and parking
- Saves data with current date prefix

### 2. Basic Analysis (`analysis.py`)

Performs basic statistical analysis and creates box plots:

```bash
python analysis.py
```

**Features:**
- Reads the most recent CSV file (dated format)
- Calculates median prices by postcode
- Creates box plots with scatter overlay
- Sorts data by median price
- Generates price vs postcode visualization

### 3. Advanced Visualization (`plots.py`)

Creates interactive plots and comprehensive visualizations:

```bash
python plots.py
```

**Features:**
- Processes all CSV files in the directory
- Creates price distribution histograms for 4-bedroom properties
- Generates box plots by property type
- Interactive Plotly visualizations
- Automatic file naming and saving

### 4. Change Tracking (`changelog.py`)

Compares CSV files to track changes over time:

```bash
python changelog.py
```

**Features:**
- Compares two CSV files
- Identifies added/removed rows
- Useful for tracking market changes
- Configurable file comparison

## Data Files

The project works with CSV files containing property data with the following columns:
- `price` - Property price in GBP
- `PostCode` - UK postcode
- `type` - Property type
- `number_bedrooms` - Number of bedrooms
- `Town` - Town name

## Configuration

### File Paths
- Update `FOLDER_PATH` in `plots.py` to match your project directory
- Ensure postcode mapping JSON file is in the correct location

### Data Collection Parameters
In `rightmove-get.py`, you can modify:
- `outcode_min` and `outcode_max` for different postcode ranges
- URL parameters for different property criteria
- Price ranges and property types

## Output

The scripts generate various outputs:
- **CSV files**: Dated property data files
- **PNG images**: Histograms and plots saved automatically
- **Interactive plots**: Plotly visualizations displayed in browser
- **Console output**: Processing status and change summaries

## Data Sources

- **Rightmove**: Primary data source for property listings
- **Postcode Data**: Swindon area postcode mappings

## Notes

- The project focuses on the Swindon area (SN postcodes)
- Data is collected with specific filters (3+ bedrooms, garden, parking)
- Visualizations are optimized for 4-bedroom property analysis
- Change tracking helps monitor market dynamics over time

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with sample data
5. Submit a pull request

## License

This project is for personal educational and research purposes. Please respect Rightmove's terms of service when using the web scraping functionality.

## Author

Created by Eshwar - Real Estate Data Analysis Project 