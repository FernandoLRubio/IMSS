from flask import Flask, request
from datetime import datetime
import cfe_scrapper as cfe_scrap
import multas_scrapper as placas_scrap
app = Flask(__name__)

@app.route('/')
def index():
    return 'Server Works!'

@app.route('/cfe',methods = ['GET'])
def fetch_cfe():
    if request.args.get("month"):
        month = int(request.args.get("month"))
        return cfe_scrap.obtener_tarifa(month).toJSON()
    else:
        return "API ERROR: UNEXPECTED ARGUMENTS"

@app.route('/cfe_now',methods = ['GET'])
def current_cfe():
    return cfe_scrap.obtener_tarifa(datetime.now().month).toJSON()


@app.route('/multas',methods = ['GET'])
def fetch_multas():
    if request.args.get("placas") and request.args.get("numeroSerie"):
        return placas_scrap.obtener_multas(request.args.get("placas"),request.args.get("numeroSerie"))
    else:
        return "API ERROR: UNEXPECTED ARGUMENTS"

if __name__ == '__main__':
    app.run(host='XXXXX', port=XXXX, debug=False, threaded=False)