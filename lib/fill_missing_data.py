import pandas as pd


class FillMissing:
    def __init__(self, pd_data):
        self.__data = pd_data

    def get_values(self):
        return self.__data

    def show(self):
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 10000)
        print(self.__data)

    def fill_missing_numeric_vals(self):
        columns_array = self.__data.select_dtypes(include=['float64']).columns
        self.__data[columns_array] = self.__data[columns_array].fillna(
            self.__data.groupby('weight_class')[columns_array].transform('mean'))
        self.__data[columns_array] = self.__data[columns_array].fillna(self.__data[columns_array].mean())
        # print(self.data)
