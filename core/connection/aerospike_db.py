import aerospike

config = {
    'hosts': [('127.0.0.1', 3000)]
}

try:
    client = aerospike.client(config).connect()
except Exception as e:
    print("Aerospike connection error:", e)
    client = None

def get_aerospike_client():
    try:
        client = aerospike.client(config).connect()
        return client
    except Exception as e:
        print("Aerospike connection error:", e)
        return None

