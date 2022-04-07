from types import MethodDescriptorType
#from flask import Flask, json, jsonify

from flask import Flask

from fastapi import FastAPI
import pandas as pd
from starlette.responses import StreamingResponse

app = FastAPI()


#app = Flask(__name__)


@app.get("/nombre")

def hello(name: str):
  
  return {'Hello ' + name + '!'}







if __name__ == '__main__':
    app.run(debug=True, port=8000)