## mixpanel-client-3

Data export api of Mixpanel.
Work with python3.

https://mixpanel.com/site_media/api/v2/mixpanel.py

https://mixpanel.com/help/reference/data-export-api

## Requirements

Require `requests` (https://github.com/requests/requests)

Add `requests` to your requirements.txt or just run `pip install requests`


## Usage

```python
def sample():
    api = Mixpanel(api_secret)
    params = {
        'event': ['pages'],
        'unit': 'hour',
        'interval': 24,
        'type': 'general',
    }
    methods = ['events']
    response = {}
    response['data'] = api.request(methods, params)
    print(response)
```
