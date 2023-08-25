from flask import Flask
import json
app = Flask(__name__)

data = { "totalCount": 1, "pageSize": 50, "problems": [ { "title": "Http monitor local outage", "affectedEntities": [ { "entityId": { "id": "HTTP_CHECK-A2313049293E", "type": "HTTP_CHECK" }, "name": "ENTITY1_HEALTH_STATUS" } ] }, { "title": "Http monitor local outage", "affectedEntities": [ { "entityId": { "id": "HTTP_CHECK-B23213131A", "type": "HTTP_CHECK" }, "name": "ENTITY2_HEALTH_STATUS" } ] } ] }

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test_data', methods=["GET"])
def test_data():
    return json.dumps(data)

@app.route('/explicit', methods=["GET"])
def explicit():
    ret = []
    for problem in data['problems']:
        for entity in problem['affectedEntities']:
            ret.append(problem['title'] + ' (' + entity['name'] + ')')
    return json.dumps({ 'problems: ' + ', '.join(ret) })
