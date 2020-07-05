# swagger_client.CartApi

All URIs are relative to *https://api.kroger.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**put_carts**](CartApi.md#put_carts) | **PUT** /cart/add | Add to cart

# **put_carts**
> APIErrorCartOk put_carts(body=body)

Add to cart

Provides access to add items to an authenticated customer's cart.  <br><br> **Note**: the customer must be authenticated using the OAuth2 Authorization Code grant type. 

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
api_instance = swagger_client.CartApi(swagger_client.ApiClient(configuration))
body = swagger_client.CartCartItemRequestModel() # CartCartItemRequestModel | A list of items that you are adding to the cart. (optional)

try:
    # Add to cart
    api_response = api_instance.put_carts(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->put_carts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CartCartItemRequestModel**](CartCartItemRequestModel.md)| A list of items that you are adding to the cart. | [optional] 

### Return type

[**APIErrorCartOk**](APIErrorCartOk.md)

### Authorization

[Customer Context](../README.md#Customer Context)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

