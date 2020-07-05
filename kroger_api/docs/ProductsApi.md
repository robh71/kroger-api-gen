# swagger_client.ProductsApi

All URIs are relative to *https://api.kroger.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_get**](ProductsApi.md#product_get) | **GET** /products | Product search
[**product_get_id**](ProductsApi.md#product_get_id) | **GET** /products/{id} | Product details

# **product_get**
> ProductsProductsPayloadModel product_get(filter_term=filter_term, filter_location_id=filter_location_id, filter_product_id=filter_product_id, filter_brand=filter_brand, filter_fulfillment=filter_fulfillment, filter_start=filter_start, filter_limit=filter_limit)

Product search

Allows you to find products by passing in either a search term or product Id.  ### Initial Search Value Required  An initial search value is requred for all requests. You can use either of the following parameters as an initial search value:   `filter.term` - When using the term parameter, the API performs a fuzzy search based on the term provided in the string. Search results are based on how relevant the term is to the product description.  `filter.productId` - When using the productId parameter, the API performs a query to find an exact match.   

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
filter_term = 'filter_term_example' # str | A search term to filter product results. As an example, you could input _milk_, _bread_, or _salt_. (optional)
filter_location_id = 'filter_location_id_example' # str | The locationId of the store. When using this filter, only products available at that location are returned. (optional)
filter_product_id = 'filter_product_id_example' # str | The productId of the products(s) to return. For more than one item, the list must be comma-separated. When used, all other query parameters are ignored. (optional)
filter_brand = 'filter_brand_example' # str | The brand name of the products to return. When using this filter, only products by that brand are returned. Brand names are case-sensitive, and lists must be pipe-separated. (optional)
filter_fulfillment = 'filter_fulfillment_example' # str | The available fulfillment types of the product(s) to return. Fulfillment types are case-sensitive, and lists must be comma-separated. Must be one or more of the follow types: <ul> <li> `ais` - Available In Store</li> <li> `csp` - Curbside Pickup</li> <li> `dth` - Delivery To Home</li> <li> `sth` - Ship To Home</li> </ui> (optional)
filter_start = 56 # int | The number of products to skip. (optional)
filter_limit = 56 # int | The number of products to return. (optional)

try:
    # Product search
    api_response = api_instance.product_get(filter_term=filter_term, filter_location_id=filter_location_id, filter_product_id=filter_product_id, filter_brand=filter_brand, filter_fulfillment=filter_fulfillment, filter_start=filter_start, filter_limit=filter_limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->product_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_term** | **str**| A search term to filter product results. As an example, you could input _milk_, _bread_, or _salt_. | [optional] 
 **filter_location_id** | **str**| The locationId of the store. When using this filter, only products available at that location are returned. | [optional] 
 **filter_product_id** | **str**| The productId of the products(s) to return. For more than one item, the list must be comma-separated. When used, all other query parameters are ignored. | [optional] 
 **filter_brand** | **str**| The brand name of the products to return. When using this filter, only products by that brand are returned. Brand names are case-sensitive, and lists must be pipe-separated. | [optional] 
 **filter_fulfillment** | **str**| The available fulfillment types of the product(s) to return. Fulfillment types are case-sensitive, and lists must be comma-separated. Must be one or more of the follow types: &lt;ul&gt; &lt;li&gt; &#x60;ais&#x60; - Available In Store&lt;/li&gt; &lt;li&gt; &#x60;csp&#x60; - Curbside Pickup&lt;/li&gt; &lt;li&gt; &#x60;dth&#x60; - Delivery To Home&lt;/li&gt; &lt;li&gt; &#x60;sth&#x60; - Ship To Home&lt;/li&gt; &lt;/ui&gt; | [optional] 
 **filter_start** | **int**| The number of products to skip. | [optional] 
 **filter_limit** | **int**| The number of products to return. | [optional] 

### Return type

[**ProductsProductsPayloadModel**](ProductsProductsPayloadModel.md)

### Authorization

[Client Context](../README.md#Client Context), [Customer Context](../README.md#Customer Context)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_id**
> ProductsProductPayloadModel product_get_id(id, filter_location_id=filter_location_id)

Product details

Provides access to the details of a specific product by either using the `productId` or `UPC`.

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
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = swagger_client.Id() # Id | 
filter_location_id = 'filter_location_id_example' # str | The locationId of the store. When using this filter, only products available at that location are returned. (optional)

try:
    # Product details
    api_response = api_instance.product_get_id(id, filter_location_id=filter_location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->product_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id**](.md)|  | 
 **filter_location_id** | **str**| The locationId of the store. When using this filter, only products available at that location are returned. | [optional] 

### Return type

[**ProductsProductPayloadModel**](ProductsProductPayloadModel.md)

### Authorization

[Client Context](../README.md#Client Context), [Customer Context](../README.md#Customer Context)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

