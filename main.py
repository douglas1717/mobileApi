#-*-coding:utf8-*-
from flask import Flask, Response, render_template, request, url_for, send_file
import androidhelper
import os
import util
import time

app = Flask(__name__)
_droid = androidhelper.Android()
#_droid = sl4a.Android()

####################################
##Constants

_pathFilesMobileApi = '/sdcard/Pictures/mobileApi'
_pathSound = '/sdcard/AudioRecorder/my_sounds'
_URL_RESOURCE = '192.168.0.5'
_PORT_RESOURCE = 5005


####################################
#Routes

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/help')
def help():
    return util.help(_URL_RESOURCE,str(_PORT_RESOURCE))

@app.route('/echo/<_echo>', methods=['GET'])
def echo(_echo):
    return _echo

@app.route('/showphoto', methods=['GET'])
def showphoto():
    _extension = 'jpg'
    _file = util.fileName(_pathFilesMobileApi,_extension)
    _droid.cameraCapturePicture(_file)
    return send_file(_file, mimetype='image/jpg')

@app.route('/showphoto2', methods=['GET'])
def showphoto2():
    _extension = 'jpg'
    _file = util.fileName(_pathFilesMobileApi,_extension)
    _return = _droid.cameraStartPreview(10,100,_pathFilesMobileApi)
    _droid.cameraInteractiveCapturePicture(_file)
    _droid.cameraStopPreview()
    return 'Photo captured' #send_file(_file, mimetype='image/jpg')

@app.route('/soundRecord10', methods=['GET'])
def soundRecord10():
    _extension = 'mp3'
    _file = util.fileName(_pathFilesMobileApi,_extension)
    _droid.recorderStartMicrophone(_file)
    time.sleep(10)
    _droid.recorderStop()
    return "Recorded 10 last seconds"

@app.route('/soundRecordStart', methods=['GET'])
def soundRecordStart():
    _extension = 'mp3'
    _file = util.fileName(_pathFilesMobileApi,_extension)
    _droid.recorderStartMicrophone(_file)
    #time.sleep(5)
    #_droid.recorderStop()
    return "Recording...<br>Use /soundRecordStop to stop"

@app.route('/soundRecordStop', methods=['GET'])
def soundRecordStop():
    _droid.recorderStop()
    return "Record stoped"

@app.route('/videoRecord10', methods=['GET'])
def videoRecord10():
    _extension = 'mp4'
    _file = util.fileName(_pathFilesMobileApi,_extension)
    _duration = 10
    _videoSize = 4 #0=160x120, 1=320x240, 2=352x288, 3=640x480, 4=800x480
    _droid. recorderCaptureVideo(_file,_duration,True) #self,targetPath,duration=0,videoSize=1
    return "Video captured"

##update
@app.route('/videoRecordStart', methods=['GET'])
def videoRecordStart():
    _extension = 'mp4'
    _file = util.fileName(_pathFilesMobileApi,_extension)
    _duration = 10
    _videoSize = 4 #0=160x120, 1=320x240, 2=352x288, 3=640x480, 4=800x480
    _droid. recorderCaptureVideo(_file,_duration,True) #self,targetPath,duration=0,videoSize=1
    return "Recording...<br>Use /videoRecordStop to stop"

@app.route('/videoRecordStop', methods=['GET'])
def videoRecordStop():
    _droid.recorderStop()
    return "Video captured"

@app.route('/photo', methods=['GET'])
def photo():
    _extension = 'jpg'
    _file = util.fileName(_pathFilesMobileApi,_extension)
    _droid.cameraCapturePicture(_file)
    #res('200 OK',[('Content-type','image/jpeg')])
    #return [file(_pathFilesMobileApi).read()]
    #r = Response(response="TEST OK", status=200, mimetype="application/xml") 
    #r.headers["Content-Type"] = "image/jpg; charset=utf-8" 
    return "ok"

####################################
#App
if __name__ == '__main__':
    app.run(host=_URL_RESOURCE, port=_PORT_RESOURCE)
    #app.run(host='127.0.0.1', port=5002)
