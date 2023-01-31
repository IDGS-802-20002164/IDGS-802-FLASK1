from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/operasbasss",methods=["GET"])
def operasbas():
    return render_template("operasbas.html")

@app.route("/resultado",methods=["POST"])
def resultado():
    n1 = request.form.get("txtNum1")
    n2 = request.form.get("txtNum2")
    res = int(n1) * int(n2)
    contador = 1
    res2 = ""
    while contador <= int(n2):
       
        if contador == int(n2):
            res2 = res2 + n1
           
        else:
            res2 = n1 + "+" + res2
        
        contador = contador + 1
    
    return render_template("resultado.html",res2=res2,res=res)

if __name__ =="__main__":
    app.run(debug=True, port=3000)