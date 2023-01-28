from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/operasBas",methods = ["GET","POST"])
def operasBas():
    if request.method == "POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        opc = request.form.get("drone")
        if opc == "1":
            return "<h2> La suma es: {}".format(str(int(num1) + int(num2)))
        elif opc == "2":
            return "<h2> La resta es: {}".format(str(int(num1) - int(num2)))
        elif opc == "3":
            return "<h2> La multi es: {}".format(str(int(num1) * int(num2)))
        elif opc == "4":
            return "<h2> La division es: {}".format(str(int(num1) / int(num2)))
        
    else:
        return '''
        <form action="operasBas" method="POST">
            <label>N1: </label>
            <input type="text" name="num1"/></br></br>
            <label>N2: </label>
            <input type="text" name="num2"/></br></br>
            <input type="submit" value="calcular"/></br></br>
            <div>
                    <input type="radio" id="suma" name="drone" value="1"
                            checked>
                    <label for="suma">Suma</label>
                    </div>

                    <div>
                    <input type="radio" id="resta" name="drone" value="2">
                    <label for="resta">Resta</label>
                    </div>

                    <div>
                    <input type="radio" id="multi" name="drone" value="3">
                    <label for="multi">Multi</label>
                    </div>

                    <div>
                    <input type="radio" id="div" name="drone" value="4">
                    <label for="div">Division</label>
            </div>
        </form>
        '''

if __name__ =="__main__":
    app.run(debug=True, port=3000)