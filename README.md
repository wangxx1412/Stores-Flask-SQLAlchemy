# Stores Flask RestAPI with SQLAlchemy

## Installation

```
pip install Flask
pip install flask-restful
pip install flask-jwt
pip install flask-sqlalchemy
python app.py
```

Use Postman to test (For testing auth, 'JWT your_accesstoken' format is used in Authorization Headers)

## Description

User registeration will return an jwt token

Some resources is protected with authentication(need jwt)

An Item is CRUD with 'name' in endpoint and 'price' in request body(json)

A Store has many Items(Foreign key: store_id)

Sqlite is set with sqlalchemy

## Usage

Register Users with Username and Password

Create, Read, Update and Delete Item

Create, Read, Delete Store and Retrive data from Store
