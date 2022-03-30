## First-time Setup

1. Install pipenv: `pip3 install pipenv`
   > Pipenv is the `npm` of Python projects

## Deployment

1. Build docker container: `pipenv run docker_build`
2. Start docker container: `pipenv run docker_run`

## Development scripts

- Dev server: `pipenv run dev`
- Testing: `pipenv run test`
- Type checking: `pipenv run lint`

## Usage

For review counts (overall rating and breakdown by stars), head to:
http://localhost/counts?app={your_app_name} 

To get a list of reviews left by customers, including the messages, head to:
http://localhost/messages?app={your_app_name}&page=1 

E.g. http://localhost:5000/counts?app=aftersell for the app listing https://apps.shopify.com/aftersell

