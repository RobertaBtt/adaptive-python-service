#!/usr/bin/env python

from app.DependencyContainer import DependencyContainer

app = DependencyContainer()

app_name = app.config().get('APP', 'name')

artist_id = 90
album_id = 162

try:
    print(f'{app_name} has started')
    print(f' Getting the Artist with id {artist_id}')
    print(app.service().get_artist_by_id(artist_id).get_name()[0])

    print(f' Getting the Album with id {album_id}')
    print(app.service().get_album_by_id(album_id).get_title()[0])

except KeyError as ex:
    print(ex)

