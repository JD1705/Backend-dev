<!-- markdownlint-disable MD024 -->
# Documentation of Endpoints

## Endpoints app/main.py

### **GET /**

#### Description

Root path that returns a JSON response with the message hello world

#### Parameters

- **No parameters required**

#### Response

```json
{
  "message":"Hello Wold!"
}
```

#### Example request

```http
GET / HTTP/1.1
Host: api.example.com
```

#### Errors

- **No possible errors (yet)**

### **POST /sum/

#### Description

Receive two numbers and return the sum of both

#### Parameters (Query)

| Name   | Type  | Required | Default | Description          |  
|--------|-------|----------|---------|----------------------|  
| `num_1`| int   | Yes      | None    | First sum number.    |  
| `num_2`| int   | Yes      | None    | Second sum number.   |

#### Response

```json
{
    "result": int,
    "status_code": 200
}
```

#### Example request

```http
POST /sum/?num_1=4&num_2=3 HTTP/1.1
Host: api.example.com
```

#### Errors

| Status code  |           Description                     |
|--------------|-------------------------------------------|
| `400`        | all parameters must be passed to          |
