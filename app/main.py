#!/usr/bin/env python

from app.DependencyContainer import DependencyContainer

app = DependencyContainer()

app_name = app.config().get('APP', 'name')

try:
    print(f'{app_name} has started')
except KeyError as ex:
    print(ex)

