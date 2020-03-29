from lib.data_extractor import DataExtractor
from lib.fill_missing_data import FillMissing
from lib.data_encoder import DataEncoder
from lib.data_normalizer import DataNormalizer

if __name__ == '__main__':
    de = DataExtractor()
    raw_data = de.get_raw_data()

    fm = FillMissing(raw_data)
    fm.fill_missing_values()
    filled_data = fm.get_values()

    print(raw_data)

    dn = DataNormalizer(filled_data)
    normalized_data = dn.get_normalized_data()

    print(normalized_data)

    enc = DataEncoder(normalized_data)
    enc.encode_data()
    enc_data = enc.get_encoded_data()
    print(enc_data)

    enc_data.drop(columns=['Referee', 'date', 'location'])
