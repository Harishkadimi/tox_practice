import requests

ENDPOINT = "https://todo.pixegami.io/"
response = requests.get(ENDPOINT)
def test_check_endPoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_crete_item():
    payload = {
        "content": "string",
        "user_id": "string",
        "is_done": False
        }
    response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert response.status_code == 200
    data = response.json()
    task_id = data['task']['task_id']
    get_task_response = requests.get(ENDPOINT + f'/get-task/{task_id}')
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data['content'] == payload['content']
    assert get_task_data['user_id'] == payload['user_id']