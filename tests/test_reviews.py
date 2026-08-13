def test_create_review_on_nonexistent_album(client, auth_header):
    resp = client.post(
        "/albums/9999/reviews",
        json={
            "text": "Great album!",
            "rating": 5,
        },
        headers=auth_header,
    )
    assert resp.status_code == 404


def test_create_and_list_reviews(client, token, auth_header):
    create_resp = client.post(
        "/albums",
        json={
            "title": "Kind of Blue",
            "artist": "Miles Davis",
            "genre": "Jazz",
            "release_year": 1959,
        },
        headers=auth_header,
    )
    album_id = create_resp.json()["id"]

    client.post(
        f"/albums/{album_id}/reviews",
        json={
            "text": "Masterpiece",
            "rating": 5,
        },
        headers=auth_header,
    )

    resp = client.get(f"/albums/{album_id}/reviews")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 1
    assert data[0]["text"] == "Masterpiece"
    assert data[0]["rating"] == 5


def test_delete_review(client, token, auth_header):
    create_resp = client.post(
        "/albums",
        json={
            "title": "Kind of Blue",
            "artist": "Miles Davis",
            "genre": "Jazz",
            "release_year": 1959,
        },
        headers=auth_header,
    )
    album_id = create_resp.json()["id"]

    review_resp = client.post(
        f"/albums/{album_id}/reviews",
        json={
            "text": "Masterpiece",
            "rating": 5,
        },
        headers=auth_header,
    )
    review_id = review_resp.json()["id"]

    resp = client.delete(f"/reviews/{review_id}", headers=auth_header)
    assert resp.status_code == 200
    assert resp.json()["message"] == "Review deleted successfully"

    list_resp = client.get(f"/albums/{album_id}/reviews")
    assert len(list_resp.json()) == 0
