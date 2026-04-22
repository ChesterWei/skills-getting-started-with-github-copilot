def test_signup_adds_participant_to_activity(client):
    """Test that POST /activities/{name}/signup successfully adds a participant"""
    # Arrange: prepare test data
    activity_name = "Chess Club"
    test_email = "newstudent@mergington.edu"

    # Act: sign up the participant
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": test_email}
    )

    # Assert: verify signup was successful
    assert response.status_code == 200
    result = response.json()
    assert "message" in result
    assert test_email in result["message"]
    assert activity_name in result["message"]

    # Verify that participant is now in the activity list
    activities = client.get("/activities").json()
    assert test_email in activities[activity_name]["participants"]
