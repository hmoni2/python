from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World"

@app.route("/led")
def led_on():
    state = request.values.get("state", "error")
    if state == "on":
        print("GPIO.HIGH")
    elif state == "off":
            print("GPIO.LOW")
    elif state == "error":
        return "쿼리스트링 state가 전달되지 않았습니다."
    else:
        return "잘못된 쿼리스트링이 전달되었습니다."
    return "LED "+ state

@app.route("/gpio/cleanup")
def gpio_cleanup():    
    return "GPIO CLEANUP" 

if __name__ == "__main__":
    app.run(debug = True)