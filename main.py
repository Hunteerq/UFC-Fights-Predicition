from lib.data_extractor import DataExtractor
from lib.fill_missing_data import FillMissing

if __name__ == '__main__':
    de = DataExtractor()
    raw_data = de.get_raw_data()
    fm = FillMissing(raw_data)
    fm.fill_missing_values()
    filled_data = fm.get_values()
    print(filled_data.isnull().any())