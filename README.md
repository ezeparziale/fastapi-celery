# :octopus: API with Fastapi and celery

Simple api with Fastapi using celery.

## :pushpin: Features

- fastapi
- celery
- flower

## :floppy_disk: Installation

```bash
python -m venv env
```

```bash
. env/scripts/activate
```

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

## :wrench: Config

Create `.env` file. Check the example `.env.example`

:construction: Before first run:

Run `docker-compose` :whale: to start the redis server

```bash
docker compose -f "docker-compose.yml" up -d --build
```

## :runner: Run

Run `docker-compose.yml` with:

```bash
docker compose -f "docker-compose.yml" up -d --build
```
