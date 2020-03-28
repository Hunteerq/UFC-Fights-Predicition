import pandas as pd
import matplotlib.pyplot as plt

LIB_DIR = "./data/ufcdata/"


class DataExtractor:

    def __init__(self):
        self.__read_all_data()
        self.__show_data()

    def __read_all_data(self):
        self.__data_df = pd.read_csv(LIB_DIR + "data.csv")
        self.__preprocessed_df = pd.read_csv(LIB_DIR + "preprocessed_data.csv")
        self.__raw_fighter_details_df = pd.read_csv(LIB_DIR + "raw_fighter_details.csv")
        self.__raw_total_fight_df = pd.read_csv(LIB_DIR + "raw_total_fight_data.csv")

