from lib import aux_keys
import http.client, urllib.parse, json
from xml.etree import ElementTree
import sys
sys.dont_write_bytecode=True
import wave


# Write a .wav file based on the text input string and the file name string


def converttowav(filename, text):
    key = aux_keys.BING_KEY
    params = ""
    headers = {"Ocp-Apim-Subscription-Key": key}
    AccessTokenHost = "api.cognitive.microsoft.com"
    path = "/sts/v1.0/issueToken"
    conn = http.client.HTTPSConnection(AccessTokenHost)
    conn.request("POST", path, params, headers)
    response = conn.getresponse()

    data = response.read()
    conn.close()
    accesstoken = data.decode("UTF-8")

    body = ElementTree.Element('speak', version='1.0')
    body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
    voice = ElementTree.SubElement(body, 'voice')
    voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
    voice.set('{http://www.w3.org/XML/1998/namespace}gender', 'Female')
    voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)')
    voice.text = text

    headers = {"Content-type": "application/ssml+xml",
                "X-Microsoft-OutputFormat": "riff-16khz-16bit-mono-pcm",
                "Authorization": "Bearer " + accesstoken,
                "X-Search-AppId": "07D3234E49CE426DAA29772419F436CA",
                "X-Search-ClientID": "1ECFAE91408841A480F00935DC390960",
                "User-Agent": "TTSForPython"}

    conn = http.client.HTTPSConnection("speech.platform.bing.com")
    conn.request("POST", "/synthesize", ElementTree.tostring(body), headers)
    response = conn.getresponse()

    data = response.read()
    conn.close()

    wavfile = wave.open('app/static/audios/'+filename+'.wav', 'wb')
    wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
    wavfile.writeframes(data)
    wavfile.close()

    return
