#!/bin/bash

gunicorn -c ./apps/api/gconfig.py apps.api.application:app
