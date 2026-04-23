def test_root_redirects_to_static_index(client):
    """Test that GET / redirects to /static/index.html"""
    # Arrange: client fixture is already prepared

    # Act: make a GET request to root
    response = client.get("/", follow_redirects=False)

    # Assert: verify redirect response
    assert response.status_code in [307, 308]
    assert "/static/index.html" in response.headers.get("location", "")
