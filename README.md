# Google drive to Wikimedia Commons

[![Build Status](https://travis-ci.com/tonythomas01/gdrive_to_commons.svg?branch=master)](https://travis-ci.com/tonythomas01/gdrive_to_commons)

Upload your files directly from Google drive to Wikimedia Commons. Currently
deployed at [Toollabs](https://tools.wmflabs
.org/google-drive-photos-to-commons/).

## Dependencies

We use `python 3.5.3` on production. Make sure you have this installed on
your machine, or use `pyenv` as described later in this documentation.

## Steps for local development

1. Install pyenv and its virtualenv manager using
   ```
   $ brew install pyenv
   $ brew install pyenv-virtualenv
   $ pyenv install 3.5.3
   $ eval "$(pyenv init -)"
   gdrive_to_commons/$ pyenv virtualenv 3.5.3 gdrive-env-3.5.3
   ```
   This will create a pyenv-virtualenv for you and probably place it on your
   `~/home/<username>/.pyenv/versions/`. You can activate that manually using
   ```
   gdrive_to_commons/$ source ~/.pyenv/versions/gdrive-env-3.5.3/bin/activate
   ```
   or even better:
   ```
   gdrive_to_commons/$ pyenv activate gdrive-env-3.5.3
   ```
   or, there are better ways to do this if you follow https://github
   .com/pyenv/pyenv-virtualenv
2. Now you are in the right environment, install dependencies using:
   ```
   (gdrive-env-3.5.3) gdrive_to_commons/$ pip install -r requirements.txt
   ```
3. We use `pre-commit` hooks to format code. See that you install it using
   https://pre-commit.com/. Later, install our pre-commit hooks using
   `(gdrive-env-3.5.3) gdrive_to_commons/$ pre-commit install`
4. There are some `localsettings` you need to have as part of running the
   server. You can copy a template using:
   `(gdrive-env-3.5.3) gdrive_to_commons/$ cp gdrive_to_commons/local_settings_sample.py gdrive_to_commons/local_settings.py`
   You need to modify the values there to use the applicaiton in full.
5. Run the Django standard runserver steps:
   ```
   (gdrive-env-3.5.3) gdrive_to_commons/$ python manage.py migrate
   (gdrive-env-3.5.3) gdrive_to_commons/$ python manage.py collectstatic
   (gdrive-env-3.5.3) gdrive_to_commons/$ python manage.py runserver
   ```
   or even better, run it from pyCharm using your debugger.
