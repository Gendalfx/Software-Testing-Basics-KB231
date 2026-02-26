import pytest
from httpx import AsyncClient
from app.main import server
import os

@pytest.mark.asyncio
async def test_root_endpoint():
    async with AsyncClient(app=server, base_url="http://test") as ac:
        response = await ac.get("/")
    
    assert response.status_code == 200
    
    data = response.json()
    assert "greetings" in data
    assert isinstance(data["greetings"], list)