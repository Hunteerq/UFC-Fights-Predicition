from lib.data_extractor import DataExtractor
from lib.fill_missing_data import FillMissing
from lib.data_encoder import DataEncoder
from lib.data_normalizer import DataNormalizer
from lib.data_analyzer import DataAnalyzer

LIB_DIR = "./data/ufcdata/"

if __name__ == '__main__':
    de = DataExtractor()
    raw_data = de.get_raw_data()

    DataAnalyzer(raw_data, 'raw_data')

    fm = FillMissing(raw_data)
    fm.fill_missing_values()
    filled_data = fm.get_values()

    filled_data.to_csv(LIB_DIR + 'data_after_filling.csv', index=False)

    DataAnalyzer(filled_data, 'filled_data')

    dn = DataNormalizer(filled_data)
    normalized_data = dn.get_normalized_data()

    normalized_data.to_csv(LIB_DIR + 'data_after_normalisation.csv', index=False)

    print(normalized_data)

    enc = DataEncoder(normalized_data)
    enc.encode_data()
    enc_data = enc.get_encoded_data()
    print(enc_data)

    enc_data.drop(columns=['R_fighter', 'B_fighter', 'Referee', 'date', 'location'])

    enc_data.to_csv(LIB_DIR + 'data_after_encoding.csv', index=False)
