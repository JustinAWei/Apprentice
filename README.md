# Apprentice: Machine Learning made Accessible

Apprentice is an ambitious project which allows users to easily adapt and apply Machine Learning models to their various data sets. To run the frontend and backend for Apprentice, you will need the following tools: [scikit_learn(0.19.0)](http://scikit-learn.org/stable/), [numpy (1.11.0)](http://www.numpy.org/), [scipy](http://www.scipy.org/), [pymongo (3.5.1)](https://api.mongodb.com/python/current/), [Flask (0.12)](http://flask.pocoo.org/docs/0.12/), [Werzeug (0.12.1)](http://werkzeug.pocoo.org/docs/0.12/) and [pickle](https://docs.python.org/2/library/pickle.html).
## Table of Contents

  1. [Frontend](#Frontend)
  2. [Backend](#Backend)
  3. [API](#API)
  4. [Features under development](#Features-under-development)
## Frontend

## Backend

## API

POST /upload
```python
  {
    "files":[(X, ...), (y, ...)],
    "predict": <id if uploading predict dataset>/null
  }
```

POST /example
```python
{
  "example": "iris"
}
```

POST /fit
```python
  {
    "data": {
      "id": <id>,
      "learner":["svm", {<params>}]
    }
  }
```

POST /predict
```python
  {
    "id":<id of orig dataset>
  }
```
## Features under development:

* Allow users to add their own input to pre-made models 
