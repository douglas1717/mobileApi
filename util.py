#-*-coding:utf8-*-
import datetime
from random import randint

#call fileName('/path','jpg')
def fileName(_path,_extension):
    _now = datetime.datetime.now()
    _anyNumber = randint(0, 1000)
    _fileName = _now.strftime("%Y%m%d_%H%M") + "_" + str(_now.second) + "_" + str(_anyNumber)
    _fileName = _path + '/' + _fileName + '.' + _extension
    return _fileName

def help(_url_resource,_port_resource):
    _echo = 'http://' + _url_resource + ':' + _port_resource + '/echo/text_to_echo'
    _help = '<a href="' + _echo + '" target="_blank">' + _echo + '</a>'
    _help = _help + '<br>'
    
    _showphoto = 'http://' + _url_resource + ':' + _port_resource + '/showphoto'
    _help = _help + '<a href="' + _showphoto + '" target="_blank">' + _showphoto + '</a>'
    _help = _help + '<br>'
    
    _showphoto2 = 'http://' + _url_resource + ':' + _port_resource + '/showphoto2'
    _help = _help + '<a href="' + _showphoto2 + '" target="_blank">' + _showphoto2 + '</a>'
    _help = _help + '<br>'
    
    _soundRecord10 = 'http://' + _url_resource + ':' + _port_resource + '/soundRecord10'
    _help = _help + '<a href="' + _soundRecord10 + '" target="_blank">' + _soundRecord10 + '</a>'
    _help = _help + '<br>'
    
    _soundRecordStart = 'http://' + _url_resource + ':' + _port_resource + '/soundRecordStart'
    _help = _help + '<a href="' + _soundRecordStart + '" target="_blank">' + _soundRecordStart + '</a>'
    _help = _help + '<br>'
    
    _soundRecordStop = 'http://' + _url_resource + ':' + _port_resource + '/soundRecordStop'
    _help = _help + '<a href="' + _soundRecordStop + '" target="_blank">' + _soundRecordStop + '</a>'
    _help = _help + '<br>'
    
    _videoRecord10 = 'http://' + _url_resource + ':' + _port_resource + '/videoRecord10'
    _help = _help + '<a href="' + _videoRecord10 + '" target="_blank">' + _videoRecord10 + '</a>'
    _help = _help + '<br>'
    
    _videoRecordStart = 'http://' + _url_resource + ':' + _port_resource + '/videoRecordStart'
    _help = _help + '<a href="' + _videoRecordStart + '" target="_blank">' + _videoRecordStart + '</a>'
    _help = _help + '<br>'
    
    _videoRecordStop = 'http://' + _url_resource + ':' + _port_resource + '/videoRecordStop'
    _help = _help + '<a href="' + _videoRecordStop + '" target="_blank">' + _videoRecordStop + '</a>'
    _help = _help + '<br>'

    return _help