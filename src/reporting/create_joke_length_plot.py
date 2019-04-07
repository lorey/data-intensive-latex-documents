# -*- coding: utf-8 -*-
import logging
from os import path
from pathlib import Path

import click
import pandas as pd
from dotenv import find_dotenv, load_dotenv

import matplotlib.pyplot as plt


@click.command()
@click.option('-output', type=click.Path())
def main(output):
    """ Create jokes plot. """
    logger = logging.getLogger(__name__)
    logger.info('make jokes plot')

    df_input = pd.read_pickle(path.join(str(project_dir), 'data', 'processed', 'jokes.pkl'))  # type: pd.DataFrame
    df_input['length'] = df_input['value'].apply(lambda s: len(s))

    n, bins, patches = plt.hist(df_input['length'], 5, density=True, facecolor='g', alpha=0.75)
    plt.xlabel('Joke length in characters')
    plt.ylabel('Probability')
    plt.title('Histogram')
    plt.axis([0, 100, 0, 0.1])
    plt.grid(True)

    with open(path.join(str(project_dir), output), 'wb') as file:
        plt.savefig(file)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
