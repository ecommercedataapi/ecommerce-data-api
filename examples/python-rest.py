"""Call the REST API directly: product details, sales estimate and reviews for one ASIN.

    pip install requests
    export ECOMMERCE_DATA_API_KEY="your_api_key"
    python python-rest.py B08CK5Z5Q1

This makes three billable calls. Create a key at
https://ecommercedataapi.com/en/settings/apikeys/create
"""

import json
import os
import sys

import requests

BASE_URL = "https://ecommercedataapi.com"


def call(path, payload):
    response = requests.post(
        f"{BASE_URL}{path}",
        headers={"X-API-Key": os.environ["ECOMMERCE_DATA_API_KEY"]},
        json=payload,
        timeout=60,
    )
    body = response.json()
    if not response.ok:
        error = body.get("error", {})
        raise RuntimeError(f"{response.status_code} {error.get('code')}: {error.get('message')}")
    return body["data"]


def main():
    asin = sys.argv[1] if len(sys.argv) > 1 else "B08CK5Z5Q1"
    marketplace = "US"

    detail = call("/v1/amazon/asin/detail", {"marketplace": marketplace, "asin": asin})
    sales = call("/v1/amazon/sales/prediction/asin", {"marketplace": marketplace, "asin": asin})
    reviews = call(
        "/v1/amazon/review",
        {"marketplace": marketplace, "asin": asin, "page": 1, "size": 20, "stars": [1, 2]},
    )

    print(json.dumps({"detail": detail, "sales_estimate": sales, "critical_reviews": reviews}, indent=2))


if __name__ == "__main__":
    main()
