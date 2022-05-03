from threading import Thread
def lsm():
    import speech_recognition as sr
    import mj
    mj.stt("Hey! welcome to this interview,Tell me about yourself")

    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        str = (r.recognize_google(audio))
        print(str)
        arr = str.split()
    l = len(arr)
    for i in range(0, l):
        if (arr[i] == "name" or arr[i]=="I"):
            name = arr[i + 2]


    mj.stt("hello"+name)

t12 = Thread(target=lsm)
t12.start()




