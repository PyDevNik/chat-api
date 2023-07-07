# RESTful API for chat
## FastAPI
## Docs - /docs

## Install
```git clone https://github.com/PyDevNik/chat-api.git
cd chat-api
```

## Setup
```sh
pip install -r requirements.txt
```

## Run
```sh
cd fast_api
uvicorn api:app
```

## Example
```py
import requests
response = requests.get("example.com/chat")
print(response.json)
```
