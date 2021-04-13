from databases import Database
import urllib.parse

db = Database('sqlite:spotify_dataset.db')

async def get(query, values = {}):
  rows = await db.fetch_all(query=query, values=values)
  dicts = []
  for row in rows:
    dicts.append(dict(row))
  return dicts


async def get_artists(artist):
  artist = urllib.parse.unquote(artist)
  query = "SELECT DISTINCT * FROM data_by_artist WHERE artists LIKE  '%' || :artist || '%' LIMIT 5"
  return await get(query, {"artist": artist})

async def get_songs(artist):
  artist = urllib.parse.unquote(artist)  
  query = '''SELECT name, popularity FROM dataset WHERE artists = :artist1 or artists LIKE "%, " || :artist2 || ", %" or artists LIKE :artist3 || ",%" or artists LIKE "%, " || :artist4 ORDER BY popularity DESC LIMIT 10'''
  return await get(query, {"artist1": artist, "artist2": artist , "artist3": artist , "artist4": artist})
