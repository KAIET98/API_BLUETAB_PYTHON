from types import MethodDescriptorType
#from flask import Flask, json, jsonify

from flask import Flask

from fastapi import FastAPI
import pandas as pd
from starlette.responses import StreamingResponse
from PIL import Image
import io



app = FastAPI()


#app = Flask(__name__)

#1. Si ponemos http://127.0.0.1:8000/nombre: 

@app.get("/nombre")

def hello(name = None):

    if name is None:
        text = 'Hello!'

    else:
        text = 'Hello ' + name + '!'

    return text


# 2. Podemos obtener los datos tal cual en bruto


@app.get("/get-iris")

def get_iris():

    import pandas as pd
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    return iris


# 3. Inclulso podemos obtener una gráfica


@app.get("/plot-iris")

def plot_iris():

  import pandas as pd
  import matplotlib.pyplot as plt

  url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
  iris = pd.read_csv(url)

  plt.scatter(iris['sepal_length'], iris['sepal_width'])

  plt.show()

  '''
  plt.savefig('iris.png')
  file = open('iris.png', mode="rb")

  return StreamingResponse(file, media_type="image/png")
  '''

# 3. Opcion de hacer incluso llamada a nuestra api 


'''
if __name__ == '__main__':
    app.run(debug=True, port=8000)
    
'''