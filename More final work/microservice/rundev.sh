#!/usr/bin/env bash
export FLASK_APP=microapp.py
export FLASK_ENV=development

flask run --host=0.0.0.0 --port=$@
