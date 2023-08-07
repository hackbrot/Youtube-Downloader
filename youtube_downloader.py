import os

from pytube import YouTube
from pathlib import Path

home = str(Path.home())
outputPath = os.path.join(home, "Downloads", "Youtube Downloader")



def download():

    print("\n----[Schizo Mettbrots Youtube Downloader Ver 1.0]-------------------------------------------\n")
    
    try:
        print("'Youtube Downloader' Ordner wird im Dowloads Ordner erstellt...\n")
        os.mkdir(outputPath)

    except:
        pass

    try:

        link = input("URL des Youtube Videos:")
        yt = YouTube(link)

        yt_choice = ""

        while yt_choice == "":

            print("\nWas möchtest du tun? [1) Höchste Qualität][2) Niedrigste Qualität][3) Qualität auswählen][4) Programm beenden]\n")
            yt_choice = input("[1/2/3]: ")
            
            if yt_choice == "":
                
                print("Du musst etwas eingebem.")

            elif yt_choice == "1":

                ys = yt.streams.get_highest_resolution()
                print("STATUS: Video wird möglicher Höchstauflösung heruntergeladen")
                ys.download(output_path = outputPath)
                print(f"STATUS: Download abgeschlossen. Datei liegt unter: {outputPath}")
            
            elif yt_choice == "2":

                ys = yt.streams.get_lowest_resolution()
                print("STATUS: Video wird in Mindestauflösung heruntergeladen")
                ys.download(output_path = outputPath)
                print(f"STATUS: Download abgeschlossen. Datei liegt unter: {outputPath}")
            
            elif yt_choice == "3":

                chosen_res = ""

                while chosen_res == "":

                    print("Wähle eine Auflösung aus [144p, 240p, 360p, 480p, 720p, ...]")
                    chosen_res = input("Auflösung: ")

                    if chosen_res == "exit":

                        print("STATUS: Vorgang abgebrochen!")
                        break

                    else:

                        try:

                            ys = yt.streams.get_by_resolution(resolution= chosen_res)
                            print(f"STATUS: Video wird in {chosen_res} heruntergeladen")
                            ys.download(output_path = outputPath)
                            print(f"STATUS: Download abgeschlossen. Datei liegt unter: {outputPath}")

                        except:

                            print("FEHLER: Wähle eine kompatible Auflösung!")
                            chosen_res = ""
            
            elif yt_choice == "4":

                print("Youtube Downloader wird beendet")
    except Exception as e:

        print("\n----[Es ist etwas schiefgelaufen]-----------------------------------------------------------\n")
        print(e)

download()