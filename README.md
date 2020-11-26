# cf_scraping

This is a [ClowdFlows 3.0](https://github.com/xflows/clowdflows-backend) package which contains widgets for collecting data from the web and extracting boilerplate code.

## Installation
Install this package by running: `pip install cf_scraping`.
To enable it in the ClowdFlows Backend, edit the `local_settings.py` file like shown below:
```
PACKAGE_TREE = [
    {
        "name": "Web Scraping",
        "packages": ['cf_scraping'],
        "order": 1
    }
]
```
Then run ` ./manage.py import_package cf_scraping` from the ClowdFlows Backend directory to import widgets into the platform.

