import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

LIB_DIR = "./data/ufcdata/"


class DataExtractor:

    def __init__(self):
        self.__read_all_data()
        self.__analyze_all_data()

    def __read_all_data(self):
        self.__data_df = pd.read_csv(LIB_DIR + "data.csv")
        self.__preprocessed_df = pd.read_csv(LIB_DIR + "preprocessed_data.csv")
        self.__raw_fighter_details_df = pd.read_csv(LIB_DIR + "raw_fighter_details.csv")
        self.__raw_total_fight_df = pd.read_csv(LIB_DIR + "raw_total_fight_data.csv")

    def __analyze_all_data(self):
        self.__analyze_boxplot_data(self.__preprocessed_df, 'preprocessed_data/')
        self.__analyze_statistics(self.__preprocessed_df)

    @staticmethod
    def __analyze_boxplot_data(df, folder):
        for column in df.select_dtypes(include=('int', 'float')):
            plt.figure()
            df.boxplot([column])
            plt.savefig('./analysis/boxplot/' + folder + column.replace('/', '_') + '.png')
            plt.close()

    def __analyze_statistics(self, df):
        for column in df.select_dtypes(include=('int', 'float')):
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


