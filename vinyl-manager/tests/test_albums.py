def test_create_album_unauthenticated(client):
    resp = client.post(
        "/albums",
        json={
            "title": "Abbey Road",
            "artist": "The Beatles",
            "genre": "Rock",
            "release_year": 1969,
        },
    )
    assert resp.status_code == 403


def test_create_and_list_albums(client, token, auth_header):
    client.post(
        "/albums",
        json={
            "title": "Abbey Road",
            "artist": "The Beatles",
            "genre": "Rock",
            "release_year": 1969,
        },
        headers=auth_header,
    )

    client.post(
        "/albums",
        json={
            "title": "Thriller",
            "artist": "Michael Jackson",
            "genre": "Pop",
            "release_year": 1982,
        },
        headers=auth_header,
    )

    resp = client.get("/albums")
    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] == 2
    assert len(data["items"]) == 2


def test_filter_albums_by_genre(client, token, auth_header):
    client.post(
        "/albums",
        json={
            "title": "Abbey Road",
            "artist": "The Beatles",
            "genre": "Rock",
            "release_year": 1969,
        },
        headers=auth_header,
    )

    client.post(
        "/albums",
        json={
            "title": "Thriller",
            "artist": "Michael Jackson",
            "genre": "Pop",
            "release_year": 1982,
        },
        headers=auth_header,
    )

    resp = client.get("/albums?genre=Rock")
    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] == 1
    assert data["items"][0]["title"] == "Abbey Road"


def test_update_album_owner_only(client, token, auth_header):
    create_resp = client.post(
        "/albums",
        json={
            "title": "Abbey Road",
            "artist": "The Beatles",
            "genre": "Rock",
            "release_year": 1969,
        },
        headers=auth_header,
    )
    album_id = create_resp.json()["id"]

    resp = client.put(
        f"/albums/{album_id}",
        json={"title": "Abbey Road (Remastered)"},
        headers=auth_header,
    )
    assert resp.status_code == 200
    assert resp.json()["title"] == "Abbey Road (Remastered)"


def test_delete_album_with_reviews_blocked(client, token, auth_header):
    create_resp = client.post(
        "/albums",
        json={
            "title": "Abbey Road",
            "artist": "The Beatles",
            "genre": "Rock",
            "release_year": 1969,
        },
        headers=auth_header,
    )
    album_id = create_resp.json()["id"]

    client.post(
        f"/albums/{album_id}/reviews",
        json={
            "text": "Classic!",
            "rating": 5,
        },
        headers=auth_header,
    )

    resp = client.delete(f"/albums/{album_id}", headers=auth_header)
    assert resp.status_code == 409
    assert "reviews" in resp.json()["detail"].lower()
