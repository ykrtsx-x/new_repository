def test_create_project_positive(api):
    response = api.create_project("My Project")

    assert response.status_code == 201
    assert response.json()["title"] == "My Project"


def test_create_project_negative(api):
    response = api.create_project("")  # пустое название

    assert response.status_code in [400, 422]


def test_get_project_positive(api, created_project):
    response = api.get_project(created_project)

    assert response.status_code == 200
    assert response.json()["id"] == created_project


def test_get_project_negative(api):
    response = api.get_project("wrong-id")

    assert response.status_code == 404


def test_update_project_positive(api, created_project):
    response = api.update_project(created_project, "Updated Project")

    assert response.status_code == 200
    assert response.json()["title"] == "Updated Project"


def test_update_project_negative(api):
    response = api.update_project("wrong-id", "Test")

    assert response.status_code in [400, 404]
