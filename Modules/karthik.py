from threading import Thread
def srmk():
    import speech_recognition as sr

    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        str = (r.recognize_google(audio))
        arr = str.lower()
        arr1 = arr.split()
        try:
            for x in range(100):
                if (arr1[x] == "name"):
                    return arr1[x+2]
                    break
        except:
            return "rgv"

