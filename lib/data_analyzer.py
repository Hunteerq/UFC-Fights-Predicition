import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BOXPLOT_DIR = "./analysis/boxplot/"


class DataAnalyzer:
    def __init__(self, data, dir):
        self.__NUMERIC_TYPES = (int, float)
        self._boxplot_dir = dir
        self.__data_df = data
        self.__create_boxplots()
        self.__analyze_all_data()

    def __analyze_all_data(self):
        self.__analyze_statistics(self.__data_df)

    def __create_boxplots(self):
        self.__analyze_boxplot_data(self.__data_df, f'{BOXPLOT_DIR}{self._boxplot_dir}/')

    @staticmethod
    def __analyze_boxplot_data(df, folder):
        for column in df.select_dtypes(include=('int', 'float')):
            plt.figure()
            df.boxplot([column])
            plt.savefig(folder + column.replace('/', '_') + '.png')
            plt.close()

    def __analyze_statistics(self, df):
        for column in df.select_dtypes(include=self.__NUMERIC_TYPES):
            self.__analyze_single_row(df[column], column)

    def __analyze_single_row(self, df, column):
        print(f'{column}')
        print(f'Range {self.__get_range(df)}')
        print(f'Empty data rows {self.__get_empty_rows(df)}')
        print(f'Data amount in classes {self.__get_classes_amount(df)}')
        print(f'Mean = {df.mean()}, Median = {df.median()}')
        print('')

    @staticmethod
    def __get_range(df):
        return df.min(), df.max()

    @staticmethod
    def __get_empty_rows(df):
        return np.where(pd.isnull(df))

    @staticmethod
    def __get_classes_amount(df):
        return df.nunique()
