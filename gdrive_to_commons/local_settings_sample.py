# Fetch the following GOOGLE_* from https://console.developers.google.com
import os

from gdrive_to_commons.settings import BASE_DIR

GOOGLE_API_DEV_KEY = "<Google API Dev Key>"
GOOGLE_CLIENT_ID = "<Your Google app client id>"
GOOGLE_APP_ID = "<Your Google APP ID>"

# Generate a Mediawiki OAuth consumer using
# https://meta.wikimedia.org/wiki/Special:OAuthConsumerRegistration/propose
SOCIAL_AUTH_MEDIAWIKI_KEY = "<OAuth consumer client id>"
SOCIAL_AUTH_MEDIAWIKI_SECRET = "<OAuth consumer client secret>"
SOCIAL_AUTH_MEDIAWIKI_URL = "<Wiki to authenticate to>"
SOCIAL_AUTH_MEDIAWIKI_CALLBACK = "oob"

WIKI_URL = "https://test.wikipedia.org/w/api.php"
STATIC_URL_DEPLOYMENT = "/static/"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "%5r@$^)+$$#$%ˆˆ%ˆˆˆˆ%$%%$&ˆˆFFDFDSFSDF@$@#DSSFDZzzzSAe3n%fm_"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://<SENTRY_ID>@sentry.io/<SENTRY_PROJECT>",
    integrations=[DjangoIntegration()],
)
