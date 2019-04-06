# -*- coding: utf-8 -*-
import json
from os import path

import click
import logging
from pathlib import Path

import requests
from dotenv import find_dotenv, load_dotenv


@click.command()
def main():
    """ Downloads jokes. """
    logger = logging.getLogger(__name__)
    logger.info('fetching jokes')

    jokes = []
    for i in range(10):
        response = requests.get('https://api.chucknorris.io/jokes/random')
        jokes.append(response.json())

    with open(path.join(str(project_dir), 'data', 'external', 'jokes.json'), 'w') as file:
        json.dump(jokes, file)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()