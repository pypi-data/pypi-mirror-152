[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# Description

Python client library for interacting with Freshworks products.

# Installation

`pip install freshworks`

This will install all available packages for working with those Freshworks products.

* `freshdesk`
* `freshcaller`

# Usage

## Basic

``` python
from freshdesk import Client


fd = Client(domain='mydomain', api_key='MY_API_KEY')
```

## Different Plan

``` python
from freshdesk import Client
from freshdesk import Plan


fd = Client(
    domain='mydomain',
    api_key='MY_API_KEY',
    plan=Plan.ESTATE,
)
```
