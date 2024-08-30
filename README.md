# Minimal project for Celery and chdb

Launch query with celery task manager

## Installation

```
pip install "celery[redis]" chdb==2.0.2
```

```
docker run --rm -p 6379:6379 valkey/valkey
```

## Description

The application is splitted into 2 parts.

`task.py`

The celery application.

`consummer.py`

The celery consummer application

## Launch

First the celery application.

`celery -A task worker -l debug`

Then you can started `consummer.py` with

`python consummer.py`