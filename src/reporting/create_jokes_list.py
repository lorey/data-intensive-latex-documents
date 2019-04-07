# -*- coding: utf-8 -*-
import logging
from os import path
from pathlib import Path

import click
import pandas as pd
from dotenv import find_dotenv, load_dotenv

from src import latex


@click.command()
@click.option('-output', required=True)
def main(output):
    """ Make jokes list. """
    logger = logging.getLogger(__name__)
    logger.info('make jokes list')

    environment = latex.create_jinja_env()

    with open(path.join(str(project_dir), 'reports', 'templates', 'jokes-list.tex')) as file:
        template_content = file.read()
    template = environment.from_string(template_content)

    df = pd.read_pickle(path.join(str(project_dir), 'data', 'processed', 'jokes.pkl'))
    jokes = df.to_dict('records')
    template_rendered = template.render(jokes=jokes)

    with open(path.join(str(project_dir), output), 'w') as file:
        file.write(template_rendered)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
