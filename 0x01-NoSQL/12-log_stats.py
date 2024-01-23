#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient, database, collection

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')

    db: database = client.logs
    nginx: collection = db.nginx

    print(f'{nginx.count_documents({})} logs')

    print('Methods:')
    print(f'\tmethod GET: {nginx.count_documents({ "method": "GET" })}')
    print(f'\tmethod POST: {nginx.count_documents({ "method": "POST" })}')
    print(f'\tmethod PUT: {nginx.count_documents({ "method": "PUT" })}')
    print(f'\tmethod PATCH: {nginx.count_documents({ "method": "PATCH" })}')
    print(f'\tmethod DELETE: {nginx.count_documents({ "method": "DELETE" })}')

    print(f'{nginx.count_documents({ "method": "GET", "path": "/status" })} status check')
