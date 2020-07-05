# swagger_client.OAuth2Api

All URIs are relative to *https://api.kroger.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**access_token**](OAuth2Api.md#access_token) | **POST** /connect/oauth2/token | Access Token
[**authorization_code**](OAuth2Api.md#authorization_code) | **GET** /connect/oauth2/authorize | Authorization Code

# **access_token**
> InlineResponse200 access_token(authorization)

Access Token

The OAuth2 endpoint that provides access tokens.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Client Context
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: Customer Context
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.OAuth2Api(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | Your `client_id:client_secret` base64 encoded.

try:
    # Access Token
    api_response = api_instance.access_token(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuth2Api->access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Your &#x60;client_id:client_secret&#x60; base64 encoded. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Client Context](../README.md#Client Context), [Customer Context](../README.md#Customer Context)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorization_code**
> authorization_code(scope, client_id, redirect_uri, response_type, state=state)

Authorization Code

The redirect URL to authenticate a customer and receive an authorization code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Customer Context
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.OAuth2Api(swagger_client.ApiClient(configuration))
scope = 'scope_example' # str | The level of access your application is requesting.
client_id = 'client_id_example' # str | Your application's client ID.
redirect_uri = 'redirect_uri_example' # str | Your registered redirect URL. The redirect URL is used by the server to redirect the web browser with the authorization code once the customer has given consent.
response_type = 'response_type_example' # str | Is always `code`.
state = 'state_example' # str | A random string to verify that the response belongs to the initiated request. The server should always return the same state as the one specified in the request to protect against forgery attacks. (optional)

try:
    # Authorization Code
    api_instance.authorization_code(scope, client_id, redirect_uri, response_type, state=state)
except ApiException as e:
    print("Exception when calling OAuth2Api->authorization_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The level of access your application is requesting. | 
 **client_id** | **str**| Your application&#x27;s client ID. | 
 **redirect_uri** | **str**| Your registered redirect URL. The redirect URL is used by the server to redirect the web browser with the authorization code once the customer has given consent. | 
 **response_type** | **str**| Is always &#x60;code&#x60;. | 
 **state** | **str**| A random string to verify that the response belongs to the initiated request. The server should always return the same state as the one specified in the request to protect against forgery attacks. | [optional] 

### Return type

void (empty response body)

### Authorization

[Customer Context](../README.md#Customer Context)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

