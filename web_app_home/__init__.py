import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    with open("html/home.html", "rb") as f:

            return func.HttpResponse(f.read(),
                                     status_code=200, mimetype="text/html"
                                     )
