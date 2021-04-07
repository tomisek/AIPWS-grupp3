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


async def get_artists(artist):
    artist = "%" + artist + "%"
    return await get('SELECT * FROM dataset WHERE name LIKE :artist LIMIT 10', {"artist": artist})