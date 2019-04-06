from flask import Flask,request
app = Flask(__name__)
import assembly,os

@app.route('/')
def hello_world():
   return app.send_static_file('index.html')

@app.route('/generate',methods=['POST'])
def generator():
    print("posted here")
    data=request.form.to_dict()
    print(str(data['msg']))
    try:
        os.remove("./static/letter.jpeg")
        print("in remove")
    except Exception as e:
        print(str(e))
    assembly.main(str(data['msg']))
    return "1" 

app.run(debug=True)
