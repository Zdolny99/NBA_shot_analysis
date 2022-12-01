# NBA_shot_analysis
This is the GitHub repository for NBA Basketball shot analysis project by group 9 of ECE 143 Fall 2022.
This repo consists of a jupyter notebook named `analysis.ipynb` 
This project also contains raw data under the folders 'Data' and 'yearwise data' that has been fetched using nba_api. The data fetching process is done using Fetch-nba-data.py.

## Objectives

Analyzing NBA shot data to see how basketball has changed over time, through where players take shots, where shots are most successful, and, and if players are getting “better” 
Demonstrate the trends behind the “3-point revolution”.

## Team Members
- Mayank Sharma -- musharma@ucsd.edu
- Tristan Philip -- tphilip@ucsd.edu
- Ken Zhou -- kzhou@ucsd.edu
- Neng Xiong -- nxiong@ucsd.edu
- Siddhant Jadhav -- sijadhav@ucsd.edu

## File description
1. shot-analysis.ipynb - The main jupyter notebook that contains all the shot-analysis done over the data. The notebook is divided into two parts - 1. Analysis of shots over time and 2. Analysis of shots over location on the field.
2. Fetch-nba-data.py - The python script to fetch, preprocess and clean all the data from nba_api. 

## How to use the code
1. Data Fetching and preprocessing  - Run the Fetch-nba-data.py as `python Fetch-nba-data.py` from root of the project to fetch, preprocess, and clean all the data from NBA API. This may take a few hours to run because the data is huge and we have to make multiple calls to the endpoint for each player and season, and also because the API is rate-limited and we can make only one request per second. Once this script runs, all the data is saved in `Data` folder. We use this data for analysis. Alternatively, you can just download the data that we have instead of going through the fetching process.
2. Run the notebook `shot-analysis.ipynb` cell by cell for the analysis.

## Packages

Jupyter Notebook, Pandas, Numpy, NBA API, Matplotlib

Install all requirements using the code below.
```bash
pip install jupyter-notebook
pip install pandas
pip install numpy
pip install matplotlib
pip install nba_api
```
## File Structure

``` bash
├── Data
│   ├── *.csv
│   └── ...
├── yearwise data
│   ├── season*.csv
│   └── ...
├── Fetch-nba-data.py
└── shot-analysis.ipynb
```


shot-analysis.ipynb
