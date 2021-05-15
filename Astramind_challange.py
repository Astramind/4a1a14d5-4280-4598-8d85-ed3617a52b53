import copy
import csv
import datetime as dt
import pandas as pd


class Stocks:
    def __init__(self):
        self.data = open("Stocks_Data_5_years.csv")
        self.data = self.data.read().splitlines()
        self.file = [val.strip().split(',') for val in self.data]
        self.column_map = {
            k: self.file[0].index(k)
            for k in self.file[0]
        }
        self.data = [self.file[i] for i in range(1, len(self.file))]

    def date_conversion(self, date1):
        """
        Take date as string and convert it into a date format
        :param: date1: string in yyyy-mm-dd format
        :return: return date in datetime format
        """
        date1 = date1.split('-')
        date1 = [int(val) for val in date1]
        date1 = dt.datetime(date1[0], date1[1], date1[2])
        return date1

    def filter_data(self, data, start_date, end_date):
        """
        Create a new filtered data list where date is between start_date and end_date
        :param data: stock data in list of list
        :param start_date: starting date as string in yyyy-mm-dd format
        :param end_date: ending date as string in yyyy-mm-dd format
        """
        filtered_data = []
        start_date = self.date_conversion(start_date)
        end_date = self.date_conversion(end_date)
        for val in data:
            date = self.date_conversion(val[self.column_map['date']])
            if start_date <= date <= end_date:
                filtered_data.append(val)
        return filtered_data

    def merge(self, sorted_list, left, mid, right_end, column_index):
        """
        Iterative function to merge sublists in ascending order
        :param sorted_list: list of list of stock data to be sorted
        :param left: Starting index of left sub-list
        :param mid: end index of left sub-list
        :param right_end: ending index of right sub-list
        :param column_index: index of column name 
        """
        # Calculating the size of left and right sub-list
        left_list_size = mid - left + 1
        right_list_size = right_end - mid
        # copying data to temporary left and right sub-list
        left_list = [sorted_list[left + i] for i in range(0, left_list_size)]
        right_list = [sorted_list[mid + 1 + i] for i in range(0, right_list_size)]
        # Merging the left and right sub-list to sorted_list
        left_list_index = 0
        right_list_index = 0
        sorted_list_index = left
        while left_list_index < left_list_size and right_list_index < right_list_size:
            # Comparing Company Name
            if left_list[left_list_index][column_index] <= right_list[right_list_index][column_index]:
                sorted_list[sorted_list_index] = left_list[left_list_index]
                left_list_index += 1
            else:
                sorted_list[sorted_list_index] = right_list[right_list_index]
                right_list_index += 1
            sorted_list_index += 1
        # Copy the remaining element of left_list if any
        while left_list_index < left_list_size:
            sorted_list[sorted_list_index] = left_list[left_list_index]
            left_list_index += 1
            sorted_list_index += 1
        # Copy the remaining element of right_list if any
        while right_list_index < right_list_size:
            sorted_list[sorted_list_index] = right_list[right_list_index]
            right_list_index += 1
            sorted_list_index += 1

    def default_sort(self, file_name='data_sorted_by_company_name.csv', column_name='Name', asc='0'):
        """
        Sort the data in ascending order by column name
        :param column_name: take default value as Name 
        :param file_name: file name to write output
        :param asc: determines the sorting order as ascending(0) or descending(1), by default its ascending
        """
        data_copy = copy.deepcopy(self.data)
        data_size = len(data_copy)
        # Size of sub-array to be merged
        size = 1
        while size < data_size:
            # Left is the start index index of left sub-lisst
            left = 0
            while left < data_size:
                # mid determine the end of left sub-list
                mid = min(left + size - 1, data_size - 1)
                # determine the end of right sub-list
                right_end = min(left + 2 * size - 1, data_size - 1)
                # merging left and right sub-list
                self.merge(data_copy, left, mid, right_end, self.column_map[column_name])
                left = left + 2 * size
            size = size * 2
        if asc == '1':
            data_copy = data_copy[::-1]
        # Writing in CSV file
        file = open(file_name, 'w+', newline='')
        with file:
            writing = csv.writer(file)
            writing.writerow(self.file[0])
            writing.writerows(data_copy)

    def modified_merge_on_company_name_or_date(self, sorted_list, left, mid, right_end):
        """
        This is a iterative function to sort the data based on the company name or date using merge sort technique
        :param sorted_list: list of list of stock data to be sorted
        :param left: Starting index of left sub-list
        :param mid: end index of left sub-list
        :param right_end: ending index of right sub-list
        """
        left_list_size = mid - left + 1
        right_list_size = right_end - mid
        # copying data to temporary left and right sub-list
        left_list = [sorted_list[left + i] for i in range(0, left_list_size)]
        right_list = [sorted_list[mid + 1 + i] for i in range(0, right_list_size)]
        # Merging the left and right sub-list to sorted_list
        left_list_index = 0
        right_list_index = 0
        sorted_list_index = left
        while left_list_index < left_list_size and right_list_index < right_list_size:
            # Converting date for comparison
            date1 = self.date_conversion(left_list[left_list_index][self.column_map['date']])
            date2 = self.date_conversion(right_list[right_list_index][self.column_map['date']])
            # Comparing dates
            if date1 <= date2:
                sorted_list[sorted_list_index] = left_list[left_list_index]
                left_list_index += 1
            else:
                sorted_list[sorted_list_index] = right_list[right_list_index]
                right_list_index += 1
            sorted_list_index += 1
        # Copy the remaining element of left_list if any
        while left_list_index < left_list_size:
            sorted_list[sorted_list_index] = left_list[left_list_index]
            left_list_index += 1
            sorted_list_index += 1
        # Copy the remaining element of right_list if any
        while right_list_index < right_list_size:
            sorted_list[sorted_list_index] = right_list[right_list_index]
            right_list_index += 1
            sorted_list_index += 1

    def sort_on_company_name_or_date_range(self, start_date='', end_date='', asc='0'):
        """
         Sort the stock data by company name as default or by date range using merge sort
        :param start_date: starting date as string in yyyy-mm-dd format by default take None
        :param end_date: ending date as string in yyyy-mm-dd format by default take Node
        :param asc: determines the sorting order as ascending(0) or descending(1), by default its ascending
        """
        if start_date == '' or end_date == '':
            self.default_sort(file_name='data_sorted_by_company_name_OR_date.csv', asc=asc)
        else:
            data_copy = copy.deepcopy(self.data)
            filtered_data = self.filter_data(data_copy, start_date, end_date)
            data_size = len(filtered_data)
            size = 1
            while size < data_size:
                # Left is the start index index of left sub-list
                left = 0
                while left < data_size:
                    # mid determine the end of left sub-list
                    mid = min(left + size - 1, data_size - 1)
                    # determine the end of right sub-list
                    right_end = min(left + 2 * size - 1, data_size - 1)
                    # merging left and right sub-list
                    self.modified_merge_on_company_name_or_date(data_copy, left, mid, right_end)
                    left = left + 2 * size
                size = size * 2
                if asc == '1':
                    filtered_data = filtered_data[::-1]

            # Writing in CSV file
            file = open("data_sorted_by_company_name_OR_date.csv", 'w+', newline='')

            with file:
                writing = csv.writer(file)
                writing.writerow(self.file[0])
                writing.writerows(filtered_data)
            file.close()

    def retrieves_the_highest_close_value(self, company_name, start_date, end_date):
        """
        retrieves the highest close value. Take company name and date range as input and return the
        highest close value in particular date range of the company
        :param company_name: name of the company
        :param start_date: starting date as string in yyyy-mm-dd format
        :param end_date: ending date as string in yyyy-mm-dd format
        """
        start_date = self.date_conversion(start_date)
        end_date = self.date_conversion(end_date)
        highest_close_value = -99999
        for data in self.data:
            if data[self.column_map['Name']] == company_name and float(highest_close_value) < float(
                    data[self.column_map['close']]):
                date = self.date_conversion(data[self.column_map['date']])
                if start_date <= date <= end_date:
                    highest_close_value = data[self.column_map['close']]
        print(highest_close_value)

    def volatile_company_stock_on_a_given_date(self, given_date):
        """
        Find the most volatile company stock on a given date
        (Volatile stocks are those which have huge differences between 'open' and 'close' value)
        :param given_date: date given by user
        """
        given_date = self.date_conversion(given_date)
        volatile_stock = -9999
        company_name = ''
        for data in self.data:
            date = self.date_conversion(data[self.column_map['date']])
            diff = -9999
            if data[self.column_map['open']] and data[self.column_map['close']]:
                diff = float(data[self.column_map['open']]) - float(data[self.column_map['close']])
            if date == given_date and volatile_stock < diff:
                volatile_stock = diff
                company_name = data[self.column_map['Name']]
        if volatile_stock == -9999:
            print("No date found")
        else:
            print("volatile_stock: ", volatile_stock, "\ncompany name: ", company_name)


def main():
    while True:
        try:
            input_function = int(input("Press 0 to exit\n"
                                       "press 1 to retrieve stocks data sorted by company name by default\n"
                                       "Press 2 to sort the stock data in ascending/descending order of company "
                                       "name or date range\n"
                                       "Press 3 to retrieves the highest close value. \n"
                                       "press 4  to find most volatile company stock on a given date\n"))
        except Exception:
            raise print("wrong input format")

        stock = Stocks()
        if input_function == 1:
            stock.default_sort()
        if input_function == 2:
            print("Start and End date fields can be left empty to sort with company name")
            start_date = str(input(" Enter start_date as string separated by '-': "))
            end_date = str(input(" Enter end_date as string separated by '-': "))
            asc = str(input("Enter 1 for descending else default is ascending: "))
            stock.sort_on_company_name_or_date_range(start_date, end_date, asc)
        if input_function == 3:
            company_name = input("Enter company name: ")
            start_date = input(" Enter start_date as string separated by '-': ")
            end_date = input(" Enter end_date as string separated by '-': ")
            stock.retrieves_the_highest_close_value(company_name, start_date, end_date)

        if input_function == 4:
            date = input("Enter Date: ")
            stock.volatile_company_stock_on_a_given_date(date)
        if input_function == 0:
            break


if __name__ == "__main__":
    main()
