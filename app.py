from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test_data', methods=["GET"])
def test_data():
    data = { "totalCount": 1, "pageSize": 50, "problems": [ { "title": "Http monitor local outage", "affectedEntities": [ { "entityId": { "id": "HTTP_CHECK-A2313049293E", "type": "HTTP_CHECK" }, "name": "ENTITY1_HEALTH_STATUS" } ] }, { "title": "Http monitor local outage", "affectedEntities": [ { "entityId": { "id": "HTTP_CHECK-B23213131A", "type": "HTTP_CHECK" }, "name": "ENTITY2_HEALTH_STATUS" } ] } ] }
    return json.dumps(data)
