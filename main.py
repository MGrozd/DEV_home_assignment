import configparser
import logging
from pathlib import Path
from pandas import read_feather

from app.influence_category import calculate_influence_category
from app import influence_score

logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('app.log')
f_format = logging.Formatter('%(asctime)s [%(levelname)s] - %(name)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.setLevel(logging.INFO)

CONFIG_FILENAME = 'conf.ini'


def main():
    try:
        config = configparser.ConfigParser()
        config.read(CONFIG_FILENAME)
        calculation_strategies = config.sections()
        for calculation_strategy in calculation_strategies:
            input_files_paths_list = list(config[calculation_strategy].keys())
            chosen_calculation_strategy = config[calculation_strategy][input_files_paths_list[0]]
            input_files_paths = [input_files_path for input_files_path in input_files_paths_list[1:-1]]
            feather_data = [
                read_feather(config[calculation_strategy][input_files_path]) for input_files_path in input_files_paths
            ]
            output_filepath = config[calculation_strategy][input_files_paths_list[-1]]

            influence_category_dataframe = calculate_influence_category(
                getattr(influence_score, f'{chosen_calculation_strategy}')(feather_data)
            )
            print(influence_category_dataframe.head())
            output_filepath = Path(output_filepath)
            output_filepath.parent.mkdir(parents=True, exist_ok=True)
            influence_category_dataframe.to_feather(output_filepath)
            logger.info(f'Made file at path: {output_filepath}')
    except Exception as err:
        logger.exception("Exception occurred")


if __name__ == '__main__':
    main()
