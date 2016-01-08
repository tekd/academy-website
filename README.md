[![Build Status](https://travis-ci.org/GovLab/academy-website.svg?branch=master)](https://travis-ci.org/GovLab/academy-website)

This is the **new** GovLab Academy website.

The old site was at [govlabacademy/govlabacademy.github.io](https://github.com/govlabacademy/govlabacademy.github.io).

## Requirements

* Python 2.7
* [pip and virtualenv](http://stackoverflow.com/q/4324558)
* [SASS](http://sass-lang.com/install) (Optional)

## Quick Start

```
virtualenv venv

# On Windows, replace the following line with 'venv\Scripts\activate'.
source venv/bin/activate

pip install -r requirements.txt
```

To develop the site, run `python build.py runserver` and visit
http://localhost:7000/. All static assets will be rebuilt as
you change them. However, if `sass` isn't on your command-line,
your SASS files won't be rebuilt.

The `site` directory will contain the generated website files.

## Deployment

To deploy the site, run `python build.py deploy`.
