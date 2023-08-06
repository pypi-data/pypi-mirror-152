# pyse

Pyse (**Py**thon **s**erver **E**2E testing) provides testing capabilities for
server-side web APIs via the unittest and requests libraries.

Simply subclass PyseTestCase:

```python
import requests

from pyse import PyseTestCase


class PyseTest(PyseTestCase):
    def test_my_api(self):
        response = requests.get("http://127.0.0.1:5000/text")
        self.assert_success(response)
        self.assert_content_equal(response, "Text")
```

## Requirements

This library requires Python >= 3.9.

## Installation

You can install pyse using the pip package manager:

```shell
pip install pye2e
```
