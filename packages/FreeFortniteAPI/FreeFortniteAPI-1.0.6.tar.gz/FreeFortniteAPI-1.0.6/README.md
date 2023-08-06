# FreeFortniteAPI
![PyPI Python Version](https://img.shields.io/pypi/pyversions/fortnite-api?label=python%20version&logo=python&logoColor=yellow)
[![discord server invite](https://discordapp.com/api/guilds/881251978951397396/embed.png)](https://discord.com/invite/pFUTyqqcUx)
Easy to use FreeFortniteAPI module.

## Installing

Python 3.5 or higher is required

```
pip install FreeFortniteAPI
```

## Documentation

To get started we first need to import the api and initialize the client.

```
import FreeFortniteAPI

api = FreeFortniteAPI.FortniteAPI
```

## Aes

```
api.aes("build", "main key", "updated")
```

## News
```
api.news("image gif", "date", "hash")
```

## Creator Code
```
api.creator_code(code="", type="code", "status")
```

## Creative Mode
```
api.creative_mode_island(code="", type="title", "description", "published date", "image", "creator")
```

## Cosmetics By ID
```
api.cosmetics_by_id(idc="", type="id", "name", "description", "type", "rarity", "image", "introduction", "file")
```