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

    def upload_file(self, file_name, file_stream, description="", license=""):
        if not description:
            description = file_name

        upload_result = self.mw_client.upload(
            file=file_stream,
            filename=file_name,
            description=get_initial_page_text(license, description),
            ignore=True,
            comment=description,
        )
        debug_information = "Uploaded: {0} to: {1}, more information: {2}".format(
            file_name, self.mw_client.host, upload_result
        )
        logging.debug(debug_information)
        upload_response = upload_result.get("result")
        print(upload_response)
        if not upload_response == "Success":
            return False, {}
        else:
            return True, upload_result["imageinfo"]


def get_initial_page_text(
    license="", summary="", category="", date_of_creation="", source="", author=""
):
    description = "|description=" + summary + "\n" if summary is not "" else ""
    date_of_creation = (
        "|date=" + date_of_creation + "\n" if date_of_creation is not "" else ""
    )
    source = "|source=" + source + "\n" if source is not "" else ""
    author = "|author=" + author + "\n" if author is not "" else ""
    category = "[[Category:{0}]] ".format(category) + "\n" if category is not "" else ""

    return """=={{{{int:filedesc}}}}==
{{{{Information
 {0}{1}{2}{3}
}}}}


=={{{{int:license-header}}}}==
{{{{{4}}}}}
{5}
""".format(
        description, date_of_creation, source, author, license, category,
    )
