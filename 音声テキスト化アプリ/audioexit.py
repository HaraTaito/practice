import moviepy.editor as mp
#インポート

clip=mp.VideoFileClip("D:\program Foles(x86)\動画ファイル/test.mp4")
#動画ファイルを参照

clip.audio.write_audiofile("D:\program Foles(x86)\動画ファイル/audiosample2.wav")
