import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)


class FillMissing:
    def __init__(self, pd_data):
        self.__data = pd_data

    def get_values(self):
        return self.__data

    def fill_missing_values(self):
        self._fill_missing_numeric_values()
        self._fill_missing_categorical_values()

    def _fill_missing_numeric_values(self):
        columns_array = self.__data.select_dtypes(include=['number']).columns
        self.__data[columns_array] = self.__data[columns_array].fillna(
            self.__data.groupby('weight_class')[columns_array].transform('median'))
        self.__data[columns_array] = self.__data[columns_array].fillna(self.__data[columns_array].mean())

    def _fill_missing_categorical_values(self):
        columns_array = self.__data.select_dtypes(include=['object']).columns
        self.__data[columns_array] = self.__data[columns_array].fillna(self.__data[columns_array].mode().iloc[0])

    @staticmethod
    def check_for_missing_values(data):
        data.isnull().any()
