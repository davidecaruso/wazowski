<p align="center">
    <img src="https://github.com/davidecaruso/wazowski/raw/master/logo.jpg" />
</p>

> *Python+GraphQL* microservice to check **ports availability** in a host.

## Install
```shell script
git clone git@github.com:davidecaruso/wazowski.git
cd wazowski && cp .env.example .env && vi .env
```

## Usage
#### With Docker
```shell script
docker-compose up --build -d
```
#### With Python3
```shell script
pip3 install --no-cache-dir -r requirements.txt
python3 main.py
```

## Getting started
Many of the following *GraphQL* queries accept these parameters:
- `start`: is the starting port value of the range. Default value is **1024**
- `end`: is the ending port value of the range. Default value is **65535**
- `host`: is the host where the search will be performed. Default value is **"127.0.0.1"**

#### Check if a port is free
> **POST** /graphql

```graphql
query Query {
  check(port: 3000, host: "127.0.0.1")
}
```
> **200**
```json
{
  "data": {
    "check": true
  }
}
```

#### Get the list of free ports in a range
> **POST** /graphql

```graphql
query Query {
  list(start: 3000, end: 3010, host: "127.0.0.1")
}
```
> **200**
```json
{
  "data": {
    "list": [
      3000,
      3002,
      3010
    ]
  }
}
```

#### Get the next free port to a given one in a range
> **POST** /graphql

```graphql
query Query {
  next(port: 3007, start: 3000, end: 3010, host: "127.0.0.1")
}
```
> **200**
```json
{
  "data": {
    "next": 3008
  }
}
```

#### Get the previous free port to a given one in a range
> **POST** /graphql

```graphql
query Query {
  previous(port: 3007, start: 3000, end: 3010, host: "127.0.0.1")
}
```
> **200**
```json
{
  "data": {
    "previous": 3006
  }
}
```

#### Get a random free port in a range
> **POST** /graphql

```graphql
query Query {
  random(start: 3000, end: 4000, host: "127.0.0.1")
}
```
> **200**
```json
{
  "data": {
    "random": 3265
  }
}
```

## Author
[Davide Caruso](https://about.me/davidecaruso)

## License
Licensed under [MIT](LICENSE).
