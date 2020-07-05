# swagger_client.IdentityApi

All URIs are relative to *https://api.kroger.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profile_get**](IdentityApi.md#profile_get) | **GET** /identity/profile | User profile information

# **profile_get**
> IdentityProfileModel profile_get()

User profile information

Provides access to the profile `id` of an authenticated customer. <br><br> **Note**: the customer must be authenticated using the OAuth2 Authorization Code grant type.

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
api_instance = swagger_client.IdentityApi(swagger_client.ApiClient(configuration))

try:
    # User profile information
    api_response = api_instance.profile_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityApi->profile_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdentityProfileModel**](IdentityProfileModel.md)

### Authorization

[Customer Context](../README.md#Customer Context)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

