from databases import Database

db = Database('sqlite:spotify_dataset.db')

async def get(query, values = {}):
  rows = await db.fetch_all(query=query, values=values)
  dicts = []
  for row in rows:
    dicts.append(dict(row))
  return dicts

async def get_genres():
  return await get('SELECT * FROM data_by_genre ORDER BY popularity DESC LIMIT 10')


# async def get_artists(artist):
#   artist = artist.replace(' ', '')
#   query = "SELECT * FROM dataset WHERE REPLACE(name,' ','') LIKE :artist LIMIT 10"
#   return await get(query, {"artist": "%" + artist + "%"})

async def get_artists(artist):
  artist = artist.replace('%20', ' ')  
  query = "SELECT DISTINCT * FROM data_by_artist WHERE artists LIKE  '%' || :artist || '%' LIMIT 5"
  return await get(query, {"artist": artist})

async def get_songs(artist):
  artist = artist.replace('%20', ' ')  
  query = "SELECT name, popularity FROM dataset WHERE artists LIKE  '%' || :artist || '%' ORDER BY popularity DESC LIMIT 10"
  return await get(query, {"artist": artist})
