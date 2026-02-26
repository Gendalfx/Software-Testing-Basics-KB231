import pytest
from httpx import AsyncClient, ASGITransport
from app.main import server

@pytest.mark.asyncio
async def test_root_endpoint():

    transport = ASGITransport(app=server)
    
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/")
    
    data = response.json()
    
    assert response.status_code == 200
    assert isinstance(data, list)  
    assert "text" in data[0]     