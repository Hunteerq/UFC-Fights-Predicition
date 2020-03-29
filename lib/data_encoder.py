FIGHTERS = ['B', 'R']


class DataEncoder:
    def __init__(self, data):
        self.__data = data

    def get_encoded_data(self):
        return self.__data

    def encode_data(self):
        self.__encode_boolean()
        self.__encode_names()
        self.__encode_categorical_strings()
        self.__encode_categorical_ints()

    def __encode_boolean(self):
        columns_array = self.__data.select_dtypes(include=['boolean']).columns
        self.__data[columns_array] = self.__data[columns_array].astype(int)

    # TODO Here values that needs to be normalized
    # def __encode_numerical(self):
    #     numerical_columns = []
    #     for fighter in FIGHTERS:
    #         numerical_columns = numerical_columns + [f'{fighter}_avg_BODY_att', f'{fighter}_avg_BODY_landed',
    #                                                  f'{fighter}_avg_CLINCH_att', f'{fighter}_avg_CLINCH_landed',
    #                                                  f'{fighter}_avg_DISTANCE_att', f'{fighter}_avg_DISTANCE_landed',
    #                                                  f'{fighter}_avg_GROUND_att', f'{fighter}_avg_GROUND_landed',
    #                                                  f'{fighter}_avg_HEAD_att', f'{fighter}_avg_HEAD_landed',
    #                                                  f'{fighter}_avg_KD', f'{fighter}_avg_LEG_att',
    #                                                  f'{fighter}_avg_LEG_landed',
    #                                                  f'{fighter}_avg_PASS', f'{fighter}_avg_REV',
    #                                                  f'{fighter}_avg_SIG_STR_att', f'{fighter}_avg_SIG_STR_landed',
    #                                                  f'{fighter}_avg_SIG_STR_pct', f'{fighter}_avg_SUB_ATT',
    #                                                  f'{fighter}_avg_TD_att',
    #                                                  f'{fighter}_avg_TD_landed', f'{fighter}_avg_TD_pct',
    #                                                  f'{fighter}_avg_TOTAL_STR_att', f'{fighter}_avg_TOTAL_STR_landed',
    #                                                  f'{fighter}_avg_opp_BODY_att', f'{fighter}_avg_opp_BODY_landed',
    #                                                  f'{fighter}_avg_opp_CLINCH_att',
    #                                                  f'{fighter}_avg_opp_CLINCH_landed',
    #                                                  f'{fighter}_avg_opp_DISTANCE_att',
    #                                                  f'{fighter}_avg_opp_DISTANCE_landed',
    #                                                  f'{fighter}_avg_opp_GROUND_att',
    #                                                  f'{fighter}_avg_opp_GROUND_landed', f'{fighter}_avg_opp_HEAD_att',
    #                                                  f'{fighter}_avg_opp_HEAD_landed', f'{fighter}_avg_opp_KD',
    #                                                  f'{fighter}_avg_opp_LEG_att', f'{fighter}_avg_opp_LEG_landed',
    #                                                  f'{fighter}_avg_opp_PASS', f'{fighter}_avg_opp_REV',
    #                                                  f'{fighter}_avg_opp_SIG_STR_att',
    #                                                  f'{fighter}_avg_opp_SIG_STR_landed',
    #                                                  f'{fighter}_avg_opp_SIG_STR_pct', f'{fighter}_avg_opp_SUB_ATT',
    #                                                  f'{fighter}_avg_opp_TD_att', f'{fighter}_avg_opp_TD_landed',
    #                                                  f'{fighter}_avg_opp_TD_pct', f'{fighter}_avg_opp_TOTAL_STR_att',
    #                                                  f'{fighter}_avg_opp_TOTAL_STR_landed',
    #                                                  f'{fighter}_total_time_fought(seconds)', f'{fighter}_Height_cms',
    #                                                  f'{fighter}_Reach_cms', f'{fighter}_Weight_lbs'
    #                                                  ]
    #

    def __encode_categorical_strings(self):
        categorical_string_columns = ['Referee', 'Winner', 'location', 'weight_class']
        for col in categorical_string_columns:
            self.__data[col] = self.__data[col].astype('category').cat.codes.apply(lambda x: self.decimal_to_binary(x))
        for fighter in FIGHTERS:
            self.__data[f'{fighter}_Stance'] = self.__data[f'{fighter}_Stance'].astype('category').cat.codes.apply(
                lambda x: self.decimal_to_binary(x))

    def __encode_names(self):
        self.__data[['R_fighter', 'B_fighter']] = self.__data[['R_fighter', 'B_fighter']].stack().rank(
            method='dense').unstack().astype(int)
        self.__data['R_fighter'] = self.__data['R_fighter'].apply(lambda x: self.decimal_to_binary(x))
        self.__data['B_fighter'] = self.__data['B_fighter'].apply(lambda x: self.decimal_to_binary(x))

    def __encode_categorical_ints(self):
        self.__data['no_of_rounds'] = self.__data['no_of_rounds'].astype('category').cat.codes.apply(
            lambda x: self.decimal_to_binary(x))
        columns = ['_current_lose_streak', '_current_win_streak',
                   '_draw', '_longest_win_streak', '_losses',
                   '_total_rounds_fought', '_total_title_bouts',
                   '_win_by_Decision_Majority', '_win_by_Decision_Split',
                   '_win_by_Decision_Unanimous', '_win_by_KO/TKO',
                   '_win_by_Submission', '_win_by_TKO_Doctor_Stoppage',
                   '_wins', '_age']
        for col_name in columns:
            self.__data[[f'R{col_name}', f'B{col_name}']] = self.__data[[f'R{col_name}', f'B{col_name}']].stack().rank(
                method='dense').unstack().astype(int)

            self.__data[f'R{col_name}'] = self.__data[f'R{col_name}'].apply(lambda x: self.decimal_to_binary(x))
            self.__data[f'B{col_name}'] = self.__data[f'B{col_name}'].apply(lambda x: self.decimal_to_binary(x))

    @staticmethod
    def decimal_to_binary(decimal_number):
        return str(bin(decimal_number))[2:]
