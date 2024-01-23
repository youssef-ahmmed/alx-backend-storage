#!/usr/bin/env python3
"""Log stats - new version"""

from pymongo import MongoClient


def print_nginx_ips(nginx_collection):
    """Prints the Ips and total requests"""
    print('IPs:')
    request_logs = nginx_collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for request_log in request_logs:
        ip = request_log['_id']
        ip_requests_count = request_log['totalRequests']
        print('\t{}: {}'.format(ip, ip_requests_count))


def print_nginx_request_logs(nginx_collection):
    """Prints stats about Nginx request logs"""
    print(f'{nginx_collection.count_documents({})} logs')

    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        print(f"""\tmethod {method}: {nginx_collection.count_documents(
            {"method": method})}""")

    print_nginx_ips(nginx_collection)

    print(f"""{nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})} status check""")


def run():
    """Provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
