# election-analysis

## Overview of Election Audit

The purpose of the audit was to determine the winner of a local election. This included determining how many votes each candidate got along with their percentage of the total vote. In addition, we were tasked with determining how many votes each county had along with relevant percentage data.

Pesudocode for project:

1. The total number of votes cast
2. A complete list oc candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote

## Software Utilized

- Python 3.7.6
- Visual Stuido Code 1.64.2
- Git Bash 2.35.1.windows.2

## Election Audit Results

Total votes cast in the election: 367,711
- County Votes:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)

- Largest County Turnout:
  - Winning County: Denver
  - Winning Vote Count: 306,055
  - Winning Percentage: 82.8%

- Candidate Votes:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
 
- Winning Candidate:
  - Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%
 
![Screenshot](https://github.com/gonzalesbarrett/election-analysis/blob/main/Election-Analysis%20Output.png)

## Election Audit Summary

The code utilized to calculate and format the complete vote data is easily customizable for similar projects. If data is provided in the same file format, with similar file structure (columns with relevant data), this code could be utilized to calculate similar results with only minor edits. The functions for determining county and candidate winners & percentage of votes can easily be adapted to additional vote related statistics such as ethnicity/race, gender, income etc as long as the data is provided in a similar format. If further voter/county data was added in additional columns the same functions already created could be modified to look at the new rows and then export similar data that we have already provided but for different demographics. Also, many aspects of the code could be easily reversed and the focus of the outputs could be on areas of opportunities. This could provided election/party officials with target areas where voter turn out was low or focus on specific demographics that did not vote. This code is also extremely scalable and would have no issues handling a much larger dataset.
