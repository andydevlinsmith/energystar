# energystar

Command-line query tool for the EnergyStar database.

# Setup:

* Clone the repository.
* Set up the environment.
    * pipenv: `pipenv install`
    * virtualenv:
        * Create and activate virtual environment.
        * Install the requirements:
            `pip install -r requirements.txt`
* Optional: Set the SODAPY_APPTOKEN environment variable.

# Run a query

* get:
    python energystar.py get [ev|tv|ups] -b *brand* -m *model*

    `python energystar.py get tv -b NEC -m E437Q`

* search:
    python energystar.py search [ev|tv|ups] -t *search term*

    `python energystar.py search ev -t charge`

# Run the tests:
* python test/test.py

