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
