from httpx import AsyncClient
from app.main import app
import pytest

@pytest.mark.asyncio
async def test_notify():
    async with AsyncClient(app=app, base_url="http://t") as ac:
        r = await ac.post("/notify", json={"channel":"email","to":"a@b.com","message":"hi"})
        assert r.status_code==202
