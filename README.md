# Google drive to Wikimedia Commons

[![Build Status](https://travis-ci.com/tonythomas01/gdrive-to-commons.svg?branch=master)](https://travis-ci.com/tonythomas01/gdrive-to-commons)

This tool is developed to Upload images directly from Google drive to Wikimedia Commons and is currently deployed at [Toollabs](https://tools.wmflabs.org/google-drive-photos-to-commons/).

## Dependencies

We use `python 3.5.3` on production. Make sure you have this installed on
your machine, or use `pyenv` as described later in this documentation under steps for local development.

## Pre-requisites for local development 

The tool authenticates to the Wikimedia cluster using Wikimedia OAuth and to Google using Google OAuth. Hence, we need a couple of secret keys in your `local_settings.py` to start development. 
1. `SOCIAL_AUTH_MEDIAWIKI_KEY` & `SOCIAL_AUTH_MEDIAWIKI_SECRET`: You can request for an OAuth client using [Wikimedia:OAuth](https://www.mediawiki.org/wiki/OAuth/For_Developers). Once created, you will get both keys. Remember that you set the right Mediawiki OAuth callback URL. 
2. `GOOGLE_APP_ID`: We need an application running on Google cloud to authorize and access Google drive. You can create your application at [Google cloud console](https://console.cloud.google.com/). `GOOGLE_APP_ID` is your project id. 
3. `GOOGLE_CLIENT_ID`: You can create a new OAuth 2.0 Client at [Google cloud credentials](https://console.cloud.google.com/apis/credentials). 
4. `GOOGLE_API_DEV_KEY`: You need to enable the **Google Picker API** on Google cloud console. Once enabled, a dev key is generated, and you can find it on your [Google cloud credentials](https://console.cloud.google.com/apis/credentials).

For Wikimedia developers, you can find more information on development keys [here](https://phabricator.wikimedia.org/T235969)

And also, the Google Drive to Wikimedia Commons Developer credentials are provided at the following link:
https://phabricator.wikimedia.org/P10014 . <br/>
Developers need not create new secret keys and can use the credentials given in the above link as instructed later in this documentation under steps for local development.
## Steps for local development

1. Create a local fork of https://github.com/tonythomas01/gdrive_to_commons using your GitHub account by running the          following command in terminal:
   ```
   $  git clone https://github.com/username/gdrive-to-commons.git
   ```
   
2. If homebrew is not installed before, install homebrew package manager by following the instructions given in      the below link: <br/>
   https://docs.brew.sh/Homebrew-on-Linux   
   
3. Install pyenv and virtual manager by running the following commands in terminal: 
   ```
   $ brew install pyenv
   $ brew install pyenv-virtualenv
   $ export PATH="$HOME/.pyenv/bin:$PATH"   
   $ eval "$(pyenv init -)"
   $ eval "$(pyenv virtualenv-init -)"
   $ pyenv install 3.5.3
   $ eval "$(pyenv init -)"
   ```
   
4. navigate into the repository by running the following command in terminal: 
   ```
   $ cd gdrive_to_commons   
   ```
   Now you are in the `gdrive_to_commons` directory and all the following commands are run in this directory.
   
5. Create pyenv-virtualenv by running the following command in terminal:
   ```
   gdrive_to_commons/$ pyenv virtualenv 3.5.3 gdrive-env-3.5.3   
   ```
   This will create a pyenv-virtualenv for you and probably place it on your `~/home/<username>/.pyenv/versions/`.   
6. Activate the virtual environment manually by running the following command:   
   ```
   gdrive_to_commons/$ source ~/.pyenv/versions/gdrive-env-3.5.3/bin/activate
   ```
   or even better:
   ```
   gdrive_to_commons/$ pyenv activate gdrive-env-3.5.3
   ```
   or, <br/>
   there are better ways to do this if you follow https://github.com/pyenv/pyenv-virtualenv.
   
   Now you are in the right environment if your terminal shows:
   ```
   (gdrive-env-3.5.3) gdrive_to_commons/$
   ```
   All the following commands are run in this environment and in this directory only.
   
7. Install dependencies by running the following command:
   ```
   (gdrive-env-3.5.3) gdrive_to_commons/$ pip install -r requirements.txt
   ```
8. We use pre-commit hooks to format code. install precommit framework by running the following command:
   `(gdrive-env-3.5.3) gdrive_to_commons/$ pip install pre-commit`<br/>
   Now, install our pre-commit hooks using: 
   `(gdrive-env-3.5.3) gdrive_to_commons/$ pre-commit install`
   
9. There are some `localsettings` you need to have as part of running the server. You can copy a template using:
   `(gdrive-env-3.5.3) gdrive_to_commons/$ cp gdrive_to_commons/local_settings_sample.py        gdrive_to_commons/local_settings.py` <br/>
   Few credentials have to be modified in `local_setting.py` <br/>
   The credentials that are to be pasted in the `local_settings.py` are given in the following link:<br/>
   https://phabricator.wikimedia.org/P10014. <br/>
   Paste the Google Drive to Wikimedia Commons Dev credentials in `local_settings.py`

10. Run the Django standard runserver steps:
   ```
   (gdrive-env-3.5.3) gdrive_to_commons/$ python manage.py makemigrations
   (gdrive-env-3.5.3) gdrive_to_commons/$ python manage.py migrate
   (gdrive-env-3.5.3) gdrive_to_commons/$ python manage.py collectstatic
   (gdrive-env-3.5.3) gdrive_to_commons/$ python manage.py runserver localhost:8000
   ```
   or even better, run it from pyCharm using your debugger.
   
Note: Only paste the command after $ in terminal while setting up and do not paste the whole line which might cause error.    
