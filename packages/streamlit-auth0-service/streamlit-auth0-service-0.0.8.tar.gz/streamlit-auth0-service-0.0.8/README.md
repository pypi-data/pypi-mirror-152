# streamlit-auth0-service
Service to authorize user by checking the `token` in the param variable of the streamlit page URL.

## Environment Variables
* AUTH0_CLAIM_KEY: JWT claim key that holds `user_metadata.org`.
* AUTH0_DOMAIN: Auth0 domain name that verifies the access token.
* ORG_ID: (Optional) organization ID. If provided, limits the access to the provided organization's users only.

## Usage

* install the dependency:
```shell
pip install streamlit-auth0-service==0.0.7
```

* Use it in streamlit python file

```python
from streamlit_auth0_service.auth0_service import StreamlitAuth0Service

auth_service = StreamlitAuth0Service()
is_authorized = auth_service.is_authorized()

if is_authorized:
    print("Authorized User.")
else:
    print("Unauthorized User!")
```