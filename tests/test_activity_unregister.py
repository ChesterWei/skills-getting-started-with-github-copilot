def test_unregister_removes_participant_from_activity(client):
    """Test that DELETE /activities/{name}/participants successfully removes a participant"""
    # Arrange: use an existing participant
    activity_name = "Chess Club"
    existing_participant = "michael@mergington.edu"

    # Verify participant exists before removal
    activities_before = client.get("/activities").json()
    assert existing_participant in activities_before[activity_name]["participants"]

    # Act: unregister the participant
    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": existing_participant}
    )

    # Assert: verify unregister was successful
    assert response.status_code == 200
    result = response.json()
    assert "message" in result
    assert existing_participant in result["message"]

    # Verify participant is no longer in activity list
    activities_after = client.get("/activities").json()
    assert existing_participant not in activities_after[activity_name]["participants"]
