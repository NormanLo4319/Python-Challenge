# Python Challenge
## PyBank
* In this challenge, we are tasked with creating a Python script for analyzing the financial records of a company. A set of financial data called [budget_data.csv](PyBank/budget_data.csv) is provided. The dataset is composed of two columns: `Date` and `Profit/Losses`.
* Our task is to create a Python script that analyzes the records to calculate each of the following:
  * The total number of months included in the dataset
  * The net total amount of "Profit/Losses" over the entire period
  * The average of the changes in "Profit/Losses" over the entire period
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period

* As an example, the analysis should look similar to the one below:

```text
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
```


## PyPoll 
* In this challenge, we are tasked with helping a small, rural town modernize its vote-counting process. 
* We are given a set of poll data called [election_data.csv](PyPoll/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Our task is to create a Python script that analyzes the votes and calculates each of the following:
  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

```text
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
```

