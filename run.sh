#!/usr/bin/env bash

if [ $1 ]; then
  if [ $1 == "dev" ]; then
    PYTHON_ENV=development python demo/main.py
  elif [ $1 == "demo" ]; then
    PYTHON_ENV=production forever --uid fa-muse -c python -a -l forever.log demo/main.py
  fi
else
    PYTHON_ENV=development python demomain.py
fi
