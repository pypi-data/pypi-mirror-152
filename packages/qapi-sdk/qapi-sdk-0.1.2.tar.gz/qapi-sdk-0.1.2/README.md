# QAPI SDK

QAPI SDK provides a library of classes for working with Query API in your Python code.

## Requirements

    * Python 3.6+
    * [python-dotenv](https://pypi.org/project/python-dotenv/)

## Installation

```bash
pip install qapi-sdk 
```

## Environment Variables

- `QAPI_URL`: QAPI API URL
- `EMAIL`: Your email

## Examples

### Query

- `FEED ID`: The table must exist in Athena.
- `QUERY ID`: The query id is used as an identifier for the query. Query id must be unique. Once you have retrieved your
  data from S3 it is advised to delete the query.
- `SQL`: The SQL query to be executed.

```python
import time

from dotenv import load_dotenv

from qapi_sdk import Query

load_dotenv()

# Step 1: Assign your FEED ID, QUERY ID, and SQL QUERY
feed_id = "[FEED/TABLE NAME]"
query_id = "[QUERY NAME]"
query = f"SELECT * FROM {feed_id}"

# Step 2: Create a Query object
my_query = Query(
    feed_id=feed_id,
    query_id=query_id
)

# Step 3: Execute the query push
my_query.push_query(sql=query)

# Step 4: Wait for the query to complete
while my_query.query_status():
    print("Waiting for query to complete...")
    time.sleep(10)

# Step 5 (Optional): Delete the query
my_query.delete_query()
```



