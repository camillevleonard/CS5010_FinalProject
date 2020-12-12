# cs5010SP. Drug Awareness Response Tool (DART).

## Table of Contents.
* Intro
* Technologies used
* Functions
* Launch
* Status
* Sources

## Intro: Project Description.
* This project aims to develop knowledge and insight into the drug epidemic in the US between the years 2000-2017 using data accumulated by IHME through various governmental sources, including the CDC. The tool is intended to be flexible, allowing queries for all states, one state, all years in the time period, or even one year. The output is tabular in some cases and graphical in other cases. We intend the user to be at least familiar with python coding, data manipulation, and data visualization. The queries are robust, however, and do not require modifications for most basic queries.

## Technologies used:

* Python using pandas and plotly.

## Functions included:

* Function 1. topState. This function returns the top "n" states, default set to 5, for drug death rates. User can specify the time period between 2000-2017 and either M, F, or both for gender. Rates correspond to the following drug types: all, opioids, amphetamine, and cocaine. The output is either a pandas data frame tabulating the return data or a user option to download the data in a csv to their working directory.
* Function 2. bottomState. This function is similar to the first function except it is looking at the bottom states in terms of death rates. These states are the least afflicted states. User input and return is the same as in function 1 but for bottom states.
* Function 3. stateHeatMap. This function graphically displays the relative death rates across all fifty US states for a given time period. The user defines the time period within the years 2000-2017. 
* Function 4. This function provides graphical output for a given state over a user defined time period for the state's drug death rates. There are two outputs available including a bar chart (if one year is selected) and a line graph (if multiple years are selected). 

## Launch.

* To run this set-up, you will need to import the module and download the appropriate csv from IHME, shown below.
* You will also need to import the following libraries: pandas, plotly.

## Project status: 
* Complete as of 5 August 2020.

## Sources.
* The main data file came from IHME in a downloaded csv, see link here:

* http://ghdx.healthdata.org/gbd-results-tool.

