import logging
import uuid

import mwclient


class WikiUploader(object):
    mw_client = None

    def __init__(
        self,
        host=None,
        consumer_secret=None,
        consumer_token=None,
        access_token=None,
        access_secret=None,
    ):
        self.mw_client = mwclient.Site(
            host=host,
            consumer_secret=consumer_secret,
            consumer_token=consumer_token,
            access_token=access_token,
            access_secret=access_secret,
        )

    def upload_file(self, file_name, file_stream, description=""):
        if not description:
            description = file_name
        unique_filename = "{0}-{1}".format(str(uuid.uuid4()), file_name)
        upload_result = self.mw_client.upload(
            file=file_stream,
            filename=unique_filename,
            description=description,
            ignore=False,
            comment="Uploaded with Google drive to commons.",
        )
        debug_information = "Uploaded: {0} to: {1}, more information: {2}".format(
            unique_filename, self.mw_client.host, upload_result
        )
        print(debug_information)
        logging.debug(debug_information)
        return True
