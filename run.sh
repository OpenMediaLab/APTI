#!/usr/bin/env bash

cd demo

if [ $1 ]; then
  if [ $1 == "dev" ]; then
    PYTHON_ENV=development python main.py
  elif [ $1 == "demo" ]; then
    PYTHON_ENV=production forever --uid fa-muse -c python -a -l forever.log main.py
  fi
else
    PYTHON_ENV=development python main.py
fi
