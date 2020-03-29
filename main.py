from lib.data_extractor import DataExtractor
from lib.fill_missing_data import FillMissing

if __name__ == '__main__':
    de = DataExtractor()
    raw_data = de.get_raw_data()
    filled_data = FillMissing(raw_data).get_values()
    print(filled_data)