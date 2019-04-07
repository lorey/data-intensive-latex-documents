Python framework for a data-intensive LaTeX documents
==============================

A project structure for a data-intensive, latex-based documents with the ability to generate LaTeX from data 
automatically.

Features:
* structured and repeatable data analysis process via a solid framework.
* easy collaboration and repeatability through version control and GNU make.
* automated (re-)generation of LaTeX files based on DataFrames and JSON data (via pandas and Jinja2 templates).

Background:

For my masters' thesis I had to analyse a lot of data and plot a lot of correlations.
Like many others, I did this with Python ([pandas](https://pandas.pydata.org/), 
[scikit-learn](https://scikit-learn.org/), [matplotlib](https://matplotlib.org/), etc.) and LaTeX.
I then created many scripts with a lot of dependencies, ran them, and copied all files into the right place afterwards.
This soon became a cumbersome task and made it hard to update the data.
Not to speak of the inability to work with my supervisor.

There had to be a better way.
So I used [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science),
a framework for reproducible data analysis (via [GNU make](https://www.gnu.org/software/make/)),
and integrated LaTeX generation for my thesis.

This framework has since been used by many of my friends, colleagues, and bachelor/master students for academic and 
corporate work (at my startup [First Momentum](https://firstmomentum.vc)).


Usage
------------
As an example, this project generates a document with Chuck Norris jokes.
To get started, you have to install the the requirements with
```
make requirements
```

Then, to generate our example document:
```
make reports/document.pdf
```
to find an auto-created document including Chuck Norris jokes.

### How it works:
Make deducts which steps are necessary to create the pdf file.
This is done via all rules defined in the Makefile.
To generate the example, the following steps are executed:

1. Fetching jokes from [an API](https://api.chucknorris.io/) in [`src/data/fetch_jokes.py`](src/data/fetch_jokes.py) 
and storing them as JSON.
2. Generating an interim DataFrame from the JSON file.
3. Making a processed DataFrame (currently only copies, usually includes feature deduction).
4. Generate jokes table in tex from the processed jokes DataFrame (in data/processed).
5. Generate jokes list in tex via the jinja template and the processed jokes DataFrame.
6. Generate PDF with the document.tex file that includes two generated tex files.

As you can see, the whole process is executed automatically which saves you many steps when your data changes.


Installation with Docker
------------
Be aware that using docker will result in large containers as the LaTeX installation will grow quite big.
So if you have LaTeX installed anyway, just install it locally.

To run the container with [docker-compose](https://docs.docker.com/compose/install/):

```
docker-compose build
docker-compose up -d
```

To use docker, enter a bash inside the newly created container:
```
docker exec -ti (container name) bash
```


Local installation
------------
If you don't want to use docker, e.g. to save disk-space, just install LaTeX or use your existing installation.
To run python, create and activate a virtual environment:
```
pip install virtualenv
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
```


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
