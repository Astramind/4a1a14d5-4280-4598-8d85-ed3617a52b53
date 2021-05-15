# 4a1a14d5-4280-4598-8d85-ed3617a52b53

Overview
---------

Develop a Python application with core features which perform the operations as described in the 'Requirements' section

Input File
----------

https://bit.ly/3h8pQRG

Problem Statement
------------------

1. Read the data from the CSV input file
2. Write function 1 to retrieve stocks data sorted by company name by default
3. Write the second function which accepts input parameters to sort the stock data in ascending/descending order of company name or date range
4. Write a third function which retrieves the highest close value. Take company name and date range as input & return the highest close value in particular date range of the company
5. Find the most volatile company stock on a given date (Volatile stocks are those which have huge differences between 'open' & 'close' value)
6. Output the results from the function into a CSV

Implementation
--------------

`main()` gives user following options to choose from:
____________________________________________________
0. To `exit()`
1. Retrieve stocks data sorted by company name by default and store in csv file named as `data_sorted_by_company_name.csv`
2. Accepts input parameters to sort the stock data in ascending/descending order of company name or date range and store the sorted data in csv file named as `data_sorted_by_company_name_OR_date.csv`
3. Retrieves the highest close value. Take company name and date range as input & return the highest close value in particular date range of the company and prints it
4. Find the most volatile company stock on a given date (Volatile stocks are those which have huge differences between 'open' & 'close' value) and prints it

Created a class `Stacks` which have following important methods:
________________________________________________________________
1. `default_sort()` Sort the data in ascending order by column name
2. `sort_on_company_name_or_date_range()` Sort the stock data by company name as default or by date range using merge sort
3. `retrieves_the_highest_close_value()` retrieves the highest close value. Take company name and date range as input and return the highest close value in particular date range of the company
4. `volatile_company_stock_on_a_given_date()` Find the most volatile company stock on a given date (Volatile stocks are those which have huge differences between 'open' and 'close' value)
