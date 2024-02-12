import pytest
from httpx import AsyncClient
from unittest.mock import patch
from main import app, database

# Test: Successful Database Fetch
@pytest.mark.asyncio
async def test_read_first_chunk_success():
    # Arrange 
    with patch.object(database, "fetch_all", return_value=[{"id": 1, "name": "Test Item"}]):
        # Act
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/read/first-chunck")
        # Assert
        assert response.status_code == 200
        assert len(response.json()) > 0

# Test: Database Fetch Error
@pytest.mark.asyncio
async def test_read_first_chunk_db_error():
    # Arrange
    with patch.object(database, "fetch_all", side_effect=Exception("Database fetch error")):
        # Act
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/read/first-chunck")
        # Assert
        assert response.status_code == 500
        assert response.json() == {"detail": "Internal Server Error"}

# Test: Empty Result Set
@pytest.mark.asyncio
async def test_read_first_chunk_empty_result():
    # Arrange
    with patch.object(database, "fetch_all", return_value=[]):
        # Act
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/read/first-chunck")
        # Assert
        assert response.status_code == 200
        assert response.json() == []  # Expecting an empty list