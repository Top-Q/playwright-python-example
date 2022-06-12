# Playwright Python Example

Example project for different features of the **Playwright** Python technology.

Many of the examples are working with the **OpenProject** site, so you should install it on your local 
machine before running them

Installation instruction for **OpenProject** can be found in [this](https://www.openproject.org/docs/installation-and-operations/installation/docker/#quick-start-1) link

## Prerequisite

Other than the **Open Project** site, you should have the following installed:

* Python 3.9 and up
* Pipenv
* Pytest

You will also need the Playwright installed.
While it is part of the projects dependencies and will be installed by Pipenv, it is best that you will follow the 
following command for installation of the different browsers rendering engines. 

```
> pip install playwright
> playwright install
```

## Running the project

You can run the tests using your favourite IDE or from the command line. For example:

```
> pytest .\tests\openproject\test_open_project_site_with_po.py
```


