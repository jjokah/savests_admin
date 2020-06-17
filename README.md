# SAVESTS ADMIN

A customized Admin dashboard - SaVests Interview Project

## Table of Contents

- [Example](#example)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Features](#features)
- [Deployment](#deployment)
- [License](#license)

## Example

```python
xxx
```

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

## Prerequisites

What you need to setup the project

- Python 3
- Pip install packages
- pipenv

## Installation

__To get a development environment running:__

> clone this repo to your local machine

```
git clone https://github.com/JohnJohnsonOkah/savests_admin.git
```

> Install Requirements

```shell
$ pipenv install
```

> Activate virtual environment
```shell
$ pipenv shell
```

> Setup Database and Create Superuser

```
not required! db.sqlite3 available..
```

> Run Development Server

```shell
$ python manage.py runserver
```

... 👯 Now development server is up and running...

## Features

- Light-weight admin dashboard page
- Dashboard displays user metrics
- Login to django-admin is redirected to custom admin
- Allow staff set a user to active or inactive (via button click)
- Allow staff send email to all existing users (console.EmailBackend)

## Deployment

Additional notes about how to deploy this on a live system
- Not yet available

## License

[MIT](LICENSE)