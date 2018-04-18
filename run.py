from flask import Flask, Blueprint, send_from_directory, render_template
import time, datetime

app = Flask(__name__, static_folder='static')

@app.route("/")
def hello():
    start = datetime.datetime.now()
    print("start time for html file - " + str(start))
    r= render_template("hello.html")
    end = datetime.datetime.now()
    print("end time for html file - " + str(end))
    return r

@app.route("/img/")
def showImage():
    start = datetime.datetime.now()
    print("start time for image - " + str(start))
    s = send_from_directory(app.static_folder, 'img-w.jpg')
    end = datetime.datetime.now()
    print("end time for image - " + str(end))
    return s

@app.route("/slow/img/")
def slowImage():
    start = datetime.datetime.now()
    print("start time for slow image - " + str(start))
    time.sleep(20)
    s = send_from_directory(app.static_folder, 'img-w.jpg')
    end = datetime.datetime.now()
    print("end time for slow image - " + str(end))
    return s

@app.route("/gif/")
def showGif():
    start = datetime.datetime.now()
    print("star time for gif - " + str(start))
    s = send_from_directory(app.static_folder, 'gif.gif')
    end = datetime.datetime.now()
    print("end time for gif - " + str(end))
    return s

@app.route("/video/")
def showVideo():
    start = datetime.datetime.now()
    print("start time for video - " + str(start))
    s= send_from_directory(app.static_folder, 'vid-1.mp4')
    end = datetime.datetime.now()
    print("end time for video - " + str(end))
    return s

@app.route("/music")
def playMusic():
    start = datetime.datetime.now()
    print("start time for music - " + str(start))
    s= send_from_directory(app.static_folder, 'kd.mp3')
    end = datetime.datetime.now()
    print("end time for music - " + str(end))
    return s


def main():
    app.run(host="0.0.0.0", port=7777, debug=False,threaded=True)

if __name__ == "__main__":
    main()
