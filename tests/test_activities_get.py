def test_get_activities_returns_all_activities(client):
    """Test that GET /activities returns all activities with correct structure"""
    # Arrange: client fixture is ready

    # Act: fetch all activities
    response = client.get("/activities")
    data = response.json()

    # Assert: verify response and data structure
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert "Gym Class" in data
    # Verify structure of one activity
    assert "description" in data["Chess Club"]
    assert "schedule" in data["Chess Club"]
    assert "max_participants" in data["Chess Club"]
    assert "participants" in data["Chess Club"]
    assert isinstance(data["Chess Club"]["participants"], list)
