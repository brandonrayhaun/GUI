import websockets
import asyncio

def hello(websocket,path):
	while True:
		result = yield from websocket.recv()
		if result is None:
			break
		if result == "0":
			print("Received 0...")
			print("Sending message back...")
			yield from websocket.send("Hello, world!")
		if result == "1":
			print("Receiver 1...")
			print("Sending message back...")
			yield from websocket.send("Goodbye, world!")

start_server = websockets.serve(hello,'localhost',8275)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
