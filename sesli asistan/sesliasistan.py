
        #ÖNEMLİ EKLENTİLER
import pyaudio
from playsound import playsound #SIKINTI CIKARSA TEKRAR YAP
from gtts import gTTS
import speech_recognition as sr
import os

kayit=sr.Recognizer()

def dinleme(a=False):
    with sr.Microphone() as kaynak:
        if a:
            print(a)
        mikrofon=kayit.listen(kaynak)    #BURAYA TEKRAR BAK(BİTTİ)
        ses = ""
        
        try:
            ses=kayit.recognize_google(mikrofon,language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım Efendim")
        except sr.RequestError:
            print("Asistan: Sistem Şuan Çalışmıyor")
            
        return ses
    
def konusma(metin):
    tts=gTTS(text=metin,lang="tr",slow=False)
    ses="konusma.mp3"
    tts.save(ses)  #HATA TEKRAR BAK(ÇÖZÜLDÜ)
    playsound("konusma.mp3")
    os.remove(ses)
    
        #YANITLAR KISMI 
def yanıt(ses):
    if "selam limonata" in ses:
        konusma("Selam Baran senin için ne yapabilirim")
    
    if "merhaba" in ses:
        konusma("Sanada Merhaba Baran")
        
    if "nasılsın" in ses:
        konusma("ben çok iyiyim seni sormalı")
        
    if "bende iyiyim" in ses:
        konusma("İyi olman beni mutlu etti")
        
    if "kötüyüm" in ses:
        konusma("neden kötü oldugunu bilmek isterim belki seni iyi yaparım")
        
    if "kapat" in ses:
        konusma("Çıkış yapılıyor")
        quit()
        
    if "dünya kupası" in ses:
        konusma("Arjantin Parçalayacak")
        
    if "messi" in ses:
        konusma("Messi cok cok cok iyi bir futbolcu")
        
        
        #İLK GİRİSDE İLK CÜMLE VE SES
konusma("Merhaba Barancım")
print("Başlatıldı...")

while True:
    
    
    #ÇALIŞMA KISMI
    ses=dinleme()
    if bool(ses)==True:
        print(ses)
        ses=ses.lower()
        yanıt(ses)
        
#BarCode Sunar :)