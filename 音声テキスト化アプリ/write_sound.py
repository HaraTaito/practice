import speech_recognition as sr
r=sr.Recognizer()

#↓音声ファイルを開き、音声データを抜き出す

with sr.AudioFile("D:\program Foles(x86)\動画ファイル/audiosample2.wav") as sourse:
    audio=r.record(sourse)

print('音声摘出中・・・')

try:
    result=r.recognize_google(audio, language='ja-jp')
    print('変換が完了しました')
    print('結果:')
    print("「" + result + "」")

    with open('file.txt', 'w') as f:
        print("「" + result + "」", file=f)


except sr.RequestError:
    print('リクエストエラーが発生しました。\n処理を終了します')

except sr.UnknownValueError:
    print('正しく読み込めませんでした。\n別の動画を試すか誤字脱字の確認')
    
