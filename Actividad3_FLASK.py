from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/cine",methods=["GET"])
def cine():
    return render_template("cinepolis.html")

@app.route("/ResultadoCine",methods=["POST"])
def ResultadoCine():
    nBoletos = int(request.form.get("txtCantidadB"))
    nombre = request.form.get("txtNumbre")
    nCantidad = request.form.get("txtCantidadB")
    
    

    opc = request.form.get("drone")
    res = ""

    if nBoletos > 7:
        res = "No puede comprar mas boletos"
    
    elif nBoletos > 5 and nBoletos <= 6:

        if opc == "1":
             des2 = ((nBoletos*12)*.85)
             des = des2 * .85
             res = "$" + str(des)
        else:
             des2 = ((nBoletos*12)*.85)
             res = "$" + str(des2)

    elif nBoletos >= 3 and nBoletos <= 5:
        
            if opc == "1":
                des2 = ((nBoletos*12)*.90)
                des = des2 * .90
                res = "$" + str(des)
            else:
                 des2 = ((nBoletos*12)*.90)
                 res = "$" + str(des2)
    
    else:
             if opc == "1":
                des = ((nBoletos*12)) * .90
                res = "$" + str(des)
             else:
                res = "$" + str((nBoletos*12))
    
    return render_template("ResultadoCine.html",res=res,nombre=nombre,nCantidad=nCantidad)


    

if __name__ =="__main__":
    app.run(debug=True, port=3000)