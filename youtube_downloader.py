# Imports

import os

from pytube import YouTube
from pathlib import Path

# Globale Variablen

home = str(Path.home())
outputPath = os.path.join(home, "Downloads", "Youtube Downloader")

# Funktion für Downloads

def download():

    print("\n----[Schizo Mettbrots Youtube Downloader Ver 1.0]-------------------------------------------\n")
    
    try: # Erstellt einen Ordner für heruntergeladene Videos falls er noch nicht existiert
        
        os.mkdir(outputPath)
        print("'Youtube Downloader' Ordner wird im Dowloads Ordner erstellt...\n")

    except: # Ansonsten fährt der Code fort

        pass

    try:

        link = input("URL des Youtube Videos:") # Eingeben der URL des Youtube Videos
        yt = YouTube(link)

        yt_choice = ""

        while yt_choice == "":

            print("\nWas möchtest du tun? [1) Höchste Qualität][2) Niedrigste Qualität][3) Qualität auswählen][4) Programm beenden]\n") # Auflösungsoptionen / Verlassen
            yt_choice = input("[1/2/3/4]: ")
            
            if yt_choice == "":
                
                print("Du musst etwas eingeben.")

            elif yt_choice == "1":  # Höchste Qualität

                ys = yt.streams.get_highest_resolution()
                print("STATUS: Video wird möglicher Höchstauflösung heruntergeladen")
                ys.download(output_path = outputPath)
                print(f"STATUS: Download abgeschlossen. Datei liegt unter: {outputPath}")
            
            elif yt_choice == "2":  # Niedrigste Qualität

                ys = yt.streams.get_lowest_resolution()
                print("STATUS: Video wird in Mindestauflösung heruntergeladen")
                ys.download(output_path = outputPath)
                print(f"STATUS: Download abgeschlossen. Datei liegt unter: {outputPath}")
            
            elif yt_choice == "3":  # Qualität auswählen

                chosen_res = ""

                while chosen_res == "":

                    print("Wähle eine Auflösung aus [144p, 240p, 360p, 480p, 720p, ...]") # Gewünschte Auflösung eingeben
                    chosen_res = input("Auflösung: ")

                    if chosen_res == "exit":

                        print("STATUS: Vorgang abgebrochen!") # Mit exit abbrechen

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
            
            elif yt_choice == "4": # Programm beenden

                print("Youtube Downloader wird beendet")

    except Exception as e:

        print("\n----[Es ist etwas schiefgelaufen]-----------------------------------------------------------\n")
        print(e)

download()