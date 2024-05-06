from fastapi import FastAPI
import uvicorn 
from DineMServer import DineMServer

app = FastAPI()

server = DineMServer(lambda x: print(x))


@app.get("/")
async def root():
    return {"/": "api information", 
            "/v1/start": "Start the dineM server", 
            "/v1/stop": "stop the dineM server", 
            "/v1/status": "Get the status of the dineM server"}

@app.get("/v1/start")
async def start(): 
    server.run()
    return {"status": server.status()}

@app.get("/v1/stop")
async def stop(): 
    server.stop()
    return {"status": server.status()}

@app.get("/v1/status")
async def status(): 
    return {"status": server.status()}


if __name__ == "__main__":
    try:
        uvicorn.run(app, host="127.0.0.1", port=8000)
    except KeyboardInterrupt:
        print("Shutting down gracefully")
        # Handle other cleanup here