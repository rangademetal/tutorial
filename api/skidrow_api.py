from fastapi import FastAPI


import json
app = FastAPI()


@app.get("/skidrow/")
async def item():
    with open('/home/sad/PycharmProject/rest/files/skidow.json', 'r') as file:
        return json.load(file)

@app.get("/skidrow/id/{id}")
async def item_id(id: str):
    with open('/home/sad/PycharmProject/rest/files/skidow.json', 'r') as file:
        games = json.load(file)
        for game in games:
            if game['id'] == id:
                return {
                    'result': game
                }

@app.get('/skidrow/name/{name}')
async def name(name:str):
    with open('/home/sad/PycharmProject/rest/files/skidow.json', 'r') as file:
        games = json.load(file)
        res = []
        for game in games:
            if name in game['name'] :
                res.append(game)
        return {
            'result': res
        }