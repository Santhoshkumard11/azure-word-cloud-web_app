import logging

import azure.functions as func

from save_user_data.save_user_date import save_user_data


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    user_name = req.params.get('name')
    associate_id = req.params.get('associate_id')
    
    if not user_name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            user_name = req_body.get('user_name')
            associate_id = req_body.get("associate_id")
            associate_level = req_body.get("associate_level")

        save_result, error_message = save_user_data(user_name, associate_id, associate_level)

        return func.JSONResponse(
            save_result, error_message)
