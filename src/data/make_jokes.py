# -*- coding: utf-8 -*-
import json
import logging
from os import path
from pathlib import Path

import click
from dotenv import find_dotenv, load_dotenv
from pandas.io.json import json_normalize


@click.command()
def main():
    """ Make jokes. """
    logger = logging.getLogger(__name__)
    logger.info('make jokes')
    with open(path.join(str(project_dir), 'data', 'external', 'jokes.json')) as file:
        df = json_normalize(json.load(file))

    df['length'] = df['value'].apply(lambda s: len(s))

    df.to_pickle(path.join(str(project_dir), 'data', 'interim', 'jokes.pkl'))


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
