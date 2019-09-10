import requests
import json

def create_project(pro_name):
    url = "http://localhost:3080/v2/projects"
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    payload = {"name": pro_name}
    response = requests.post(url, data= json.dumps(payload), headers=headers)
    print(response.text)
    response = response.json()
    return response["project_id"]

def create_node(pro_id, node_type, node_name):
    url = "http://localhost:3080/v2/projects/" + pro_id + "/nodes"
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    payload = {"name": node_name, "node_type": node_type, "compute_id": "local"}
    response = requests.post(url, data= json.dumps(payload), headers=headers)
    print(response.text)
    response = response.json()
    return response["node_id"]

def link_nodes(pro_id, node_1_id, node_1_adapter, node_1_port, node_2_id, node_2_adapter, node_2_port):
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    url = "http://localhost:3080/v2/projects/"+ pro_id + "/links"
    payload = {
    'nodes': [
            {'adapter_number': node_1_adapter, 'node_id': node_1_id, 'port_number': node_1_port},
            {'adapter_number': node_2_adapter, 'node_id': node_2_id, 'port_number': node_2_port}
        ]
    }
    payload = json.dumps(payload)
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)

def start_nodes(pro_id, node_id):
    url = "http://localhost:3080/v2/projects/" + pro_id + "/nodes/" + node_id +"/start"
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    payload = {}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)

pro_id = create_project("python_gns3_api2")
node_1_id = create_node(pro_id, "vpcs", "node-1")
node_2_id = create_node(pro_id, "vpcs", "node-2")
link_nodes(pro_id, node_1_id, 0, 0, node_2_id, 0,0)
start_nodes(pro_id, node_1_id)
start_nodes(pro_id, node_2_id)
