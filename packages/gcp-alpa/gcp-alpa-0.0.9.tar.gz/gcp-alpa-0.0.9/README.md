# gcp

Various wrappers over Google Cloud Platform API



## Installation

```
pip install gcp-alpa
```

## geocoding


```
from gcp.geocoding import GCPGeocoding

geocoding = GCPGeocoding(api_key='<API_KEY>')

result = geocoding.reverse(78.2232, 15.6267)

print(result.country)
print(result.locality)
print(result.neighborhood)
```

Output
```
Svalbard and Jan Mayen
Longyearbyen
None
```