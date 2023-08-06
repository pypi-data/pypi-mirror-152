[![Tests](https://github.com/trafire/promail/workflows/Tests/badge.svg)](https://github.com/trafire/promail/actions?workflow=Tests)
[![Codecov](https://codecov.io/gh/trafire/promail/branch/master/graph/badge.svg)](https://codecov.io/gh/trafire/promail)
[![PyPI](https://img.shields.io/pypi/v/promail.svg)](https://pypi.org/project/promail/)
# Promail

Promail along with its sister library Promail-Templates aims 
to close the email gap between what you as an individual can make your
email do with little effort and what enterprise users do

- Automated Professional Rich content HTML emails
- Allow you to write your own pluggins that do arbitrary things depending on the content of the email.

## Installation
```
pip install promail
```
## Simple Usage

```python

client = GmailClient("your-gmail@gmail.com")
# The first time you do this it will open a web browser allowing you to sign into your google account directly
client.send_email()

```
