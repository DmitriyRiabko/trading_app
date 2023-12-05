from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Trading App"
)

fake_users = [
    {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com"
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 35,
        "email": "bob@example.com"
    },
    {
        "id": 3,
        "name": "Carol",
        "age": 28,
        "email": "carol@example.com"
    },
    {
        "id": 4,
        "name": "Dave",
        "age": 40,
        "email": "dave@example.com"
    },
    {
        "id": 5,
        "name": "Eve",
        "age": 25,
        "email": "eve@example.com"
    }
]

fake_trades = [
    {'id':1,'user_id':1, 'currency':'BTC','side':'buy','price':123,'amount':2.12},
    {'id':2,'user_id':1, 'currency':'BTC','side':'buy','price':125,'amount':2.12}

]




@app.get('/user/{userId}')
def get_user(userId :int):
    return [user  for user in fake_users if user.get('id') == userId ]


class Trade(BaseModel):
    id: int
    user_id:int
    currency: str
    side: str
    price: float
    amount : float


@app.post('/trades')
def add_trades(trades: list[Trade]):
    fake_trades.extend(trades)
    return {'status':200,"data": fake_trades}