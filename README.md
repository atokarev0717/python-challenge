# Python-Challenge

There are two folders [PyBank](PyBank) and [PyPoll](PyPoll) which are completely unrelated. 

## PyBank
Please note the raw data is not included in the repository but is available upon request. The raw date contains financial data which is composed of two columns: `Date` and `Profit/Losses`. 
[Python Script](PyBank\main.py) runs through the data to calculate the following:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* Average change of "Profit/Losses" over the entire period

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in losses (date and amount) over the entire period

The Python Script [prints results of the analysis to terminal](PyBank\Analysis\PyBank_Analysis_img.PNG) and [records the results to newely created CSV file](PyBank\Analysis\result.csv)

## PyPoll
Please note the raw data is not included in the repository but is available upon request. The raw date contains set of poll data for a small town. The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. [Python Script](PyPoll\main.py) runs through the data to calculate the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote

The Python Script [prints results of the analysis to terminal](PyPoll\Analysis\PyPoll_Analysis_img.PNG) and [records the results to newely created CSV file](PyPoll\Analysis\election_result.csv)

## Notes
If there are any questions please feel free to reach out to me 