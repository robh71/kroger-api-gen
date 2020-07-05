# swagger_client.LocationsApi

All URIs are relative to *https://api.kroger.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chain_exists**](LocationsApi.md#chain_exists) | **HEAD** /chains/{name} | Chain query
[**department_exists**](LocationsApi.md#department_exists) | **HEAD** /departments/{id} | Department query
[**get_chain**](LocationsApi.md#get_chain) | **GET** /chains/{name} | Chain details
[**get_department**](LocationsApi.md#get_department) | **GET** /departments/{id} | Department details
[**list_chains**](LocationsApi.md#list_chains) | **GET** /chains | Chain list
[**list_departments**](LocationsApi.md#list_departments) | **GET** /departments | Department list
[**locations_exists_by_id**](LocationsApi.md#locations_exists_by_id) | **HEAD** /locations/{locationId} | Location query
[**locations_get_by_id**](LocationsApi.md#locations_get_by_id) | **GET** /locations/{locationId} | Location details
[**search_locations**](LocationsApi.md#search_locations) | **GET** /locations | Location list

# **chain_exists**
> APIErrorNoContent chain_exists(name)

Chain query

Determine if a specific chain exists by using the chain `name`.

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

# create an instance of the API class
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The name of a chain owned by The Kroger Co. <br><br> **Note**: the chain `name` is returned from the [/chains](/#operation/ListChains) endpoint as `name` and from the [/locations](/#operation/SearchLocations) endpoint as `chain`.

try:
    # Chain query
    api_response = api_instance.chain_exists(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->chain_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of a chain owned by The Kroger Co. &lt;br&gt;&lt;br&gt; **Note**: the chain &#x60;name&#x60; is returned from the [/chains](/#operation/ListChains) endpoint as &#x60;name&#x60; and from the [/locations](/#operation/SearchLocations) endpoint as &#x60;chain&#x60;. | 

### Return type

[**APIErrorNoContent**](APIErrorNoContent.md)

### Authorization

[Client Context](../README.md#Client Context)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **department_exists**
> APIErrorNoContent department_exists(id)

Department query

Determine if a specific department exists by using the `departmentId`. 

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

# create an instance of the API class
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The departmentId of the department to return.

try:
    # Department query
    api_response = api_instance.department_exists(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->department_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The departmentId of the department to return. | 

### Return type

[**APIErrorNoContent**](APIErrorNoContent.md)

### Authorization

[Client Context](../README.md#Client Context)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chain**
> LocationsChainResponse get_chain(name)

Chain details

Provides access to the details of a specific chian by using the chain `name`.

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

# create an instance of the API class
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The name of a chain owned by The Kroger Co. <br><br> **Note**: the chain `name` is returned from the [/chains](/#operation/ListChains) endpoint as `name` and from the [/locations](/#operation/SearchLocations) endpoint as `chain`.

try:
    # Chain details
    api_response = api_instance.get_chain(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of a chain owned by The Kroger Co. &lt;br&gt;&lt;br&gt; **Note**: the chain &#x60;name&#x60; is returned from the [/chains](/#operation/ListChains) endpoint as &#x60;name&#x60; and from the [/locations](/#operation/SearchLocations) endpoint as &#x60;chain&#x60;. | 

### Return type

[**LocationsChainResponse**](LocationsChainResponse.md)

### Authorization

[Client Context](../README.md#Client Context)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_department**
> LocationsDepartmentResponse get_department(id)

Department details

Provides access to the details of a specific department by using the `departmentId`. 

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

# create an instance of the API class
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The departmentId of the department to return.

try:
    # Department details
    api_response = api_instance.get_department(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_department: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The departmentId of the department to return. | 

### Return type

[**LocationsDepartmentResponse**](LocationsDepartmentResponse.md)

### Authorization

[Client Context](../README.md#Client Context)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_chains**
> LocationsChainsResponse list_chains()

Chain list

Provides access to a list of all chains owned by The Kroger Co.

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

# create an instance of the API class
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))

try:
    # Chain list
    api_response = api_instance.list_chains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->list_chains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LocationsChainsResponse**](LocationsChainsResponse.md)

### Authorization

[Client Context](../README.md#Client Context)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_departments**
> LocationsDepartmentsResponse list_departments()

Department list

Provides access to a list of all departments, including departments of chains owned by The Kroger Co.

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

# create an instance of the API class
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))

try:
    # Department list
    api_response = api_instance.list_departments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->list_departments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LocationsDepartmentsResponse**](LocationsDepartmentsResponse.md)

### Authorization

[Client Context](../README.md#Client Context)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_exists_by_id**
> APIErrorNoContent locations_exists_by_id(location_id)

Location query

Determines if a specific location exists by using the `locationId`.

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

# create an instance of the API class
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))
location_id = 'location_id_example' # str | The locationId of the store.

try:
    # Location query
    api_response = api_instance.locations_exists_by_id(location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->locations_exists_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| The locationId of the store. | 

### Return type

[**APIErrorNoContent**](APIErrorNoContent.md)

### Authorization

[Client Context](../README.md#Client Context)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_get_by_id**
> LocationsLocationResponse locations_get_by_id(location_id)

Location details

Provides access to the details of a specific location by using the `locationId`.

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

# create an instance of the API class
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))
location_id = 'location_id_example' # str | The locationId of the store.

try:
    # Location details
    api_response = api_instance.locations_get_by_id(location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->locations_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| The locationId of the store. | 

### Return type

[**LocationsLocationResponse**](LocationsLocationResponse.md)

### Authorization

[Client Context](../README.md#Client Context)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_locations**
> LocationsLocationSearchResponse search_locations(filter_zip_code_near=filter_zip_code_near, filter_lat_long_near=filter_lat_long_near, filter_lat_near=filter_lat_near, filter_lon_near=filter_lon_near, filter_radius_in_miles=filter_radius_in_miles, filter_limit=filter_limit, filter_chain=filter_chain, filter_department=filter_department)

Location list

Provides access to a list of locations matching a given criteria. If the parameter `filter.chain` is not provided, the results include all locations and chains owned by The Kroger Co.<br> <h3>Starting Point Required</h3> You must include one of the following parameters as a starting point to narrow search results:<br><br> <ul> <li> <code>filter.zipCode.near</code></li> <li> <code>filter.latLong.near</code></li> <li> <code>filter.lat.near</code> and <code>filter.lon.near</code></li> </ul><br> If you do not provide a starting point or provide more than one starting point, an error is returned. By default, the results are limited to 10 locations within a 10-mile radius of the provided starting point. If you would like to extend the search results, you can use the parameter `filter.radiusInMiles` to set a new mile radius or `filter.limit` to set the number of results returned.

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

# create an instance of the API class
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))
filter_zip_code_near = 'filter_zip_code_near_example' # str | The zip code to use as a starting point for results. (optional)
filter_lat_long_near = 'filter_lat_long_near_example' # str | The latitude and longitude to use as a starting point for results. (optional)
filter_lat_near = 'filter_lat_near_example' # str | The latitude to use as a starting point for results. (optional)
filter_lon_near = 'filter_lon_near_example' # str | The longitude to use as a starting point for results. (optional)
filter_radius_in_miles = 10 # int | The mile radius of results. (optional) (default to 10)
filter_limit = 10 # int | The number of results to return. (optional) (default to 10)
filter_chain = 'filter_chain_example' # str | The chain name of the chain. When using this filter, only stores matching the provided chain name are returned. (optional)
filter_department = 'filter_department_example' # str | The departmentId of the department. Lists must be comma-separated. When using this filter, only stores that have all of the departments provided are returned. (optional)

try:
    # Location list
    api_response = api_instance.search_locations(filter_zip_code_near=filter_zip_code_near, filter_lat_long_near=filter_lat_long_near, filter_lat_near=filter_lat_near, filter_lon_near=filter_lon_near, filter_radius_in_miles=filter_radius_in_miles, filter_limit=filter_limit, filter_chain=filter_chain, filter_department=filter_department)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->search_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_zip_code_near** | **str**| The zip code to use as a starting point for results. | [optional] 
 **filter_lat_long_near** | **str**| The latitude and longitude to use as a starting point for results. | [optional] 
 **filter_lat_near** | **str**| The latitude to use as a starting point for results. | [optional] 
 **filter_lon_near** | **str**| The longitude to use as a starting point for results. | [optional] 
 **filter_radius_in_miles** | **int**| The mile radius of results. | [optional] [default to 10]
 **filter_limit** | **int**| The number of results to return. | [optional] [default to 10]
 **filter_chain** | **str**| The chain name of the chain. When using this filter, only stores matching the provided chain name are returned. | [optional] 
 **filter_department** | **str**| The departmentId of the department. Lists must be comma-separated. When using this filter, only stores that have all of the departments provided are returned. | [optional] 

### Return type

[**LocationsLocationSearchResponse**](LocationsLocationSearchResponse.md)

### Authorization

[Client Context](../README.md#Client Context)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

