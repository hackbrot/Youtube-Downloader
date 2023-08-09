# Imports

import os

from pathlib import Path
from pytube import YouTube
from pytube import innertube


# Globale Variablen

home = str(Path.home())
outputPath = os.path.join(home, "Downloads", "Youtube Downloader")
restricted_name_symbols = ["\\", "/", ":", "*", "?", "<", ">", "|", "#", "$", "+", "%", '"']

innertube._cache_dir = os.path.join(os.getcwd(), "cache")
innertube._token_file = os.path.join(innertube._cache_dir, 'tokens.json')

# Funktion für Downloads

def download():

    try: # Erstellt einen Ordner für heruntergeladene Videos falls er noch nicht existiert
        
        os.mkdir(outputPath)
        print("'Youtube Downloader' Ordner wird im Dowloads Ordner erstellt...\n")

    except: # Ansonsten fährt der Code fort

        pass

    try:

        link = input("URL des Youtube Videos: ") # Eingeben der URL des Youtube Videos

        # Link in Youtube Funktion einreichen

        yt = YouTube(link, 
                    use_oauth = True,           # use_oauth nutzt die Authentifikation des Youtube Nutzers um Altersbegrenzte Videos herunterzuladen
                    allow_oauth_cache = True    # allow_oauth_cache legt den Zugangstoken im Cache ab, sodass die Abfrage nur einmal getätigt werden muss
                    )   
        
        # Video Details     
        
        print("\n[Ausgewähltes Video]")
        print(f"\nVideo: {yt.title}")   # Videotitel
        print(f"Länge: {yt.length}")    # Videolänge
        print(f"Aufrufe: {yt.views}\n") # Videoaufrufe

        # Namensvergebung

        file_name = " "

        while file_name == " ":

            file_name = input("Name für die Datei (Leer lassen um Videotitel zu nutzen): ") # Dateinamen vergeben
            file_name.strip() # Leerzeichen werden entfernt, sodass es nicht zu Fehlern in der Namensgebung kommt

            if file_name in restricted_name_symbols : # Falls ungültige Zeichen im Dateinamen sind

                print("\nFehler: Name enthält ungültiges Zeichen.")
                print("Folgende Zeichen dürfen nicht verwendet werden: \\, /, :, *, ?, <, >, |, #, $, +, %," + '"\n')
                file_name = " "
            
            elif file_name == "": # Falls leer

                download_name = yt.streams.get_highest_resolution().default_filename.strip(".mp4")
                
            else: # Ansonsten Dateinamen nutzen, der eingegeben wird

                download_name = file_name
                
        print(f"Dateiname: {download_name}.mp4")

        yt_choice = ""

        while yt_choice == "":

            print("\nWas möchtest du tun? [1) Höchste Qualität][2) Niedrigste Qualität][3) Qualität auswählen][4) Programm beenden]\n") # Auflösungsoptionen / Verlassen
            yt_choice = input("[1/2/3/4]: ")
            
            if yt_choice == "":
                
                print("INFO: Du musst etwas eingeben.")

            elif yt_choice == "1":  # Höchste Qualität

                ys = yt.streams.get_highest_resolution()
                print("\nSTATUS: Video wird möglicher Höchstauflösung heruntergeladen")
                
                if os.path.exists(f"{outputPath}/{download_name}.mp4"): # Falls die MP4 schon existiert
                    
                    print("Fehler. Dieses Video existiert bereits\n")

                else:

                    ys.download(output_path = outputPath, filename = download_name)
                    print(f"STATUS: Download abgeschlossen. Datei liegt unter: {outputPath}\n")
                    download() # Programmablauf wiederholen

            elif yt_choice == "2":  # Niedrigste Qualität

                ys = yt.streams.get_lowest_resolution()
                print("\nSTATUS: Video wird in Mindestauflösung heruntergeladen")

                if os.path.exists(f"{outputPath}/{download_name}.mp4"): # Falls die MP4 schon existiert
                    
                    print("Fehler. Dieses Video existiert bereits\n")
                
                else:

                    ys.download(output_path = outputPath, filename = download_name)
                    print(f"Download abgeschlossen. Datei liegt unter: {outputPath}\n")
                    download() # Programmablauf wiederholen
                
            elif yt_choice == "3":  # Qualität auswählen

                chosen_res = ""

                while chosen_res == "":

                    print("\nWähle eine Auflösung aus [144p, 240p, 360p, 480p, 720p]") # Gewünschte Auflösung eingeben
                    chosen_res = input("[Auflösung]: ")

                    if chosen_res == "exit":

                        print("\nSTATUS: Vorgang abgebrochen!") # Mit exit abbrechen
                        break

                    else:

                        try:
                            
                            ys = yt.streams.get_by_resolution(resolution= chosen_res)
                            print(f"\nSTATUS: Video wird in {chosen_res} heruntergeladen")

                            if os.path.exists(f"{outputPath}/{download_name}.mp4"): # Falls die MP4 schon existiert
                    
                                print("Fehler. Dieses Video existiert bereits\n")
                            
                            else:

                                ys.download(output_path = outputPath, filename = download_name)
                                print(f"STATUS: Download abgeschlossen. Datei liegt unter: {outputPath}\n")
                                download() # Programmablauf wiederholen

                        except:

                            print("Fehler. Wähle eine kompatible Auflösung!\n")
                            chosen_res = ""
            
            elif yt_choice == "4": # Programm beenden

                print("Youtube Downloader wird beendet...")

    except Exception as e:

        print("\n----[Es ist etwas schiefgelaufen]-----------------------------------------------------------\n") # Für kritische Fehler
        print(f"Fehler: {e}")
        download()

print("\n----[Schizo Mettbrots Youtube Downloader Ver 1.1]-------------------------------------------\n") # Überschrift

download()