import requests
import schemathesis
from schemathesis.checks import not_a_server_error
from schemathesis.specs.openapi.checks import (
    content_type_conformance,
    response_headers_conformance,
    response_schema_conformance,
    status_code_conformance,
)


# loading schema from uri
schema = schemathesis.from_uri("http://localhost:5252/swagger/v1/swagger.json")

#schema = schemathesis.from_uri("https://testytgrapp.azurewebsites.net/swagger/v1/swagger.json")

# loading schema from path
#schema = schemathesis.from_path("./swagger.json")

# get user token

#url = "https://testytgrapp.azurewebsites.net/api/users"
url = "http://localhost:5252/api/users"

user = {"Username": "test", "Password": "test"}
token = requests.post(url, json=user).json()["token"]


@schema.parametrize()
def test_api(case):
    # run default checks
    #case.call_and_validate(headers={"Authorization": f"Bearer {token}"})

    #or customize checks which need to be chosen/excluded
     response = case.call(headers={"Authorization": f"Bearer {token}"})
     case.validate_response(
        response,
        checks=(
            #not_a_server_error,
            response_schema_conformance,
            #response_headers_conformance,
            #content_type_conformance,
            #status_code_conformance
        ),
        #additional_checks=(content_type_conformance,),
        #excluded_checks=(status_code_conformance,),
    )
