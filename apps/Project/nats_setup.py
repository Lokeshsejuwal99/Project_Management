from nats import NATS 

nats = NATS()

def start_nats():
 nats.connect(url="nats://localhost:4222") 

def close_nats():
 nats.close()