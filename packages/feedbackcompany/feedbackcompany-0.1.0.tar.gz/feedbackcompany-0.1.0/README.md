# Python client for the Feedback Company API

https://intercom.help/feedbackcompany/nl/collections/2424875-api-review-research-portal


### Usage

First obtain a `client_id` and `client_secret`. Example to create an order and automatically send a review invite:

```python
from feedbackcompany import FeedbackCompanyAPI
client_id = 'AAA'
client_secret = 'BBB'
api = FeedbackCompanyAPI(client_id, client_secret)
response = api.post(
    'orders',
    {
        'external_id': 'Order 123', 
        'customer': {
            'email': 'info@example.com', 
            'fullname': 'John Doe' 
        },
        'invitation': {
            'delay': {'unit': 'days', 'amount': 0},
            'reminder': {'unit': 'days', 'amount': 7}
        },
    }
)
```

### Persistent access token

If you construct the client using `FeedbackCompanyAPI(client_id, client_secret)`, it will automatically request an access token. Since an access token is usually valid for 60 days, it is useful to store it for reuse in future sessions, for example in a database or cache. The user is responsible for this. To reuse an existing access token, simply pass it to the constructor. If the access token has expired, the client will automatically request a new one.

Example:
```python
from feedbackcompany import FeedbackCompanyAPI
client_id = 'AAA'
client_secret = 'BBB'
access_token = cache.get('feedbackcompany_access_token') # Replace with some storage backend
api = FeedbackCompanyAPI(client_id, client_secret, access_token=access_token)
response = api.get(...)
if api.access_token != access_token:
    # Store new access token
    cache.set('feedbackcompany_access_token', api.access_token, 60*24*60*60)
```
