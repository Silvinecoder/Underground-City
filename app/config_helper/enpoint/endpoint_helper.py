import re
from config_helper.log import log_config

log = log_config("Endpoint")


class Endpoint(object):
    """
    Creating a class inside your `endpoints` folder that inherits from Endpoint will generate a new endpoint.

    Typically, an endpoint will serve both "global" (`/resource/`) and "single" (`/resource/{uuid}`) requests.

    To implement the endpoint behaviour, you must override:
    - `get_global` for `GET` requests to `/resource/`
    - `get_single` for `GET` requests to `/resource/{uuid}`
    - `post_global` for `POST` requests to `/resource/`
    - `post_single` for `POST` requests to `/resource/{uuid}`
    - `put_global` for `PUT` requests to `/resource/`
    - `put_single` for `PUT` requests to `/resource/{uuid}`
    - `delete_global` for `DELETE` requests to `/resource/`
    - `delete_single` for `DELETE` requests to `/resource/{uuid}`

    All the above are optional, but you must implement at least one of them.
    These methods must return a tuple of `(status_code, body)`, where body is a dict.

    Error handling is done automatically when an exception is raised.
    """

    DEFAULT_ENDPOINTS_DATA = {
        "default": {  # The HTTP method. In __custom_endpoints_data__ this should be replaced with GET/PUT/POST/DELETE
            "integration_type": "aws_proxy",  # The integration type between the APIGW and the Lambda function
            "response_content_type": "application/json",
            # The content type expected by the requester. Only use when integration_type is not aws_proxy
            "request_content_type": "application/json",
            # The content type expected by the APIGW. Only use when integration_type is not aws_proxy
            "response_mapping_template": "",
            # The template that maps outgoing data from JSON to the content type expected by the requester. Only use when integration_type is not aws_proxy
            "request_mapping_template": "",
            # The template that maps incoming data to JSON for the lambda function. Only use when integration_type is not aws_proxy
            "response_mapping_regex": "default"
            # The rule that matches the outgoing lambda HTTP response to the outgoing APIGW response
        }
    }

    __custom_endpoints_data__ = {
        "GET": {},
        "PUT": {},
        "POST": {},
        "DELETE": {}
    }

    __deprecated__ = False  #: Flag this endpoint as deprecated
    __body_schema_name__ = None  #: Override the name of the schema to use for the body
    __return_schema_name__ = None  #: Override the name of the schema to use for the responsew