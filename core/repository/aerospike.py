from core.connection.aerospike_db import get_aerospike_client

def filter_games(query=None):
    client = get_aerospike_client()
    games = []

    def callback(record_tuple):
        key, meta, record = record_tuple
        if not query or query.lower() in record.get("name", "").lower() or query.lower() in record.get("category", "").lower():
            games.append(record)

    query_obj = client.query("test", "games")
    query_obj.foreach(callback)

    return games


def insert_game(game_id, name, category):
    client = get_aerospike_client()
    key = ("test", "games", game_id)
    record = {
        "name": name,
        "category": category
    }
    client.put(key, record)