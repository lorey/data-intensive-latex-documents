# -*- coding: utf-8 -*-
import logging
from os import path
from pathlib import Path

import click
import pandas as pd
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.option('-output', type=click.Path())
def main(output):
    """ Make jokes tables. """
    logger = logging.getLogger(__name__)
    logger.info('make jokes')

    # use full width in output
    pd.set_option('display.max_colwidth', -1)

    df_input = pd.read_pickle(path.join(str(project_dir), 'data', 'processed', 'jokes.pkl'))  # type: pd.DataFrame
    df = pd.DataFrame(df_input, columns=['value'])
    df = df.rename({'id': 'ID', 'value': 'Joke'}, axis=1)
    with open(path.join(str(project_dir), output), 'w') as output_file:
        df.to_latex(output_file, index=False, col_space=100)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
