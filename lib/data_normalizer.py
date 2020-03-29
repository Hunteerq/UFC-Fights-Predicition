FIGHTERS = ['B', 'R']


class DataNormalizer:

    def __init__(self, not_normalized_data):
        self.__not_normalized_data = not_normalized_data
        self.__normalized_data = not_normalized_data
        self.__normalize_data()

    def get_normalized_data(self):
        return self.__normalized_data

    def __normalize_data(self):
        cols_to_normalize = []
        print("BBBBBBBBBBBBBBBBBBBBBBBBBBB")
        for fighter in FIGHTERS:
            cols_to_normalize = cols_to_normalize + [f'{fighter}_avg_BODY_att', f'{fighter}_avg_BODY_landed',
                                                     f'{fighter}_avg_CLINCH_att', f'{fighter}_avg_CLINCH_landed',
                                                     f'{fighter}_avg_DISTANCE_att', f'{fighter}_avg_DISTANCE_landed',
                                                     f'{fighter}_avg_GROUND_att', f'{fighter}_avg_GROUND_landed',
                                                     f'{fighter}_avg_HEAD_att', f'{fighter}_avg_HEAD_landed',
                                                     f'{fighter}_avg_KD', f'{fighter}_avg_LEG_att',
                                                     f'{fighter}_avg_LEG_landed',
                                                     f'{fighter}_avg_PASS', f'{fighter}_avg_REV',
                                                     f'{fighter}_avg_SIG_STR_att', f'{fighter}_avg_SIG_STR_landed',
                                                     f'{fighter}_avg_SIG_STR_pct', f'{fighter}_avg_SUB_ATT',
                                                     f'{fighter}_avg_TD_att',
                                                     f'{fighter}_avg_TD_landed', f'{fighter}_avg_TD_pct',
                                                     f'{fighter}_avg_TOTAL_STR_att', f'{fighter}_avg_TOTAL_STR_landed',
                                                     f'{fighter}_avg_opp_BODY_att', f'{fighter}_avg_opp_BODY_landed',
                                                     f'{fighter}_avg_opp_CLINCH_att',
                                                     f'{fighter}_avg_opp_CLINCH_landed',
                                                     f'{fighter}_avg_opp_DISTANCE_att',
                                                     f'{fighter}_avg_opp_DISTANCE_landed',
                                                     f'{fighter}_avg_opp_GROUND_att',
                                                     f'{fighter}_avg_opp_GROUND_landed', f'{fighter}_avg_opp_HEAD_att',
                                                     f'{fighter}_avg_opp_HEAD_landed', f'{fighter}_avg_opp_KD',
                                                     f'{fighter}_avg_opp_LEG_att', f'{fighter}_avg_opp_LEG_landed',
                                                     f'{fighter}_avg_opp_PASS', f'{fighter}_avg_opp_REV',
                                                     f'{fighter}_avg_opp_SIG_STR_att',
                                                     f'{fighter}_avg_opp_SIG_STR_landed',
                                                     f'{fighter}_avg_opp_SIG_STR_pct', f'{fighter}_avg_opp_SUB_ATT',
                                                     f'{fighter}_avg_opp_TD_att', f'{fighter}_avg_opp_TD_landed',
                                                     f'{fighter}_avg_opp_TD_pct', f'{fighter}_avg_opp_TOTAL_STR_att',
                                                     f'{fighter}_avg_opp_TOTAL_STR_landed',
                                                     f'{fighter}_total_time_fought(seconds)', f'{fighter}_Height_cms',
                                                     f'{fighter}_Reach_cms', f'{fighter}_Weight_lbs']
        for column in cols_to_normalize:
            self.__normalized_data[column] = self.__normalize_column(self.__normalized_data[column])

    @staticmethod
    def __normalize_column(df):
        max_el = df.max()
        if max_el != 0:
            return df.map(lambda x: x / max_el)
        else:
            return df
