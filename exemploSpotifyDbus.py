import dbus
import re

def get_song_details():

    try:
        session_bus = dbus.SessionBus()

        spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                             "/org/mpris/MediaPlayer2")
        propriedadesSpotify = dbus.Interface(spotify_bus,
                                            "org.freedesktop.DBus.Properties")
        metadados = propriedadesSpotify.Get("org.mpris.MediaPlayer2.Player", "Metadata")

        artista = metadados['xesam:artist']
        artista = str(artista[0]).lower()
        artista = artista.replace(" ", "")

        tituloMusica = str(metadados['xesam:title']).lower()
        tituloMusica = tituloMusica.replace(" ", "")

        song_art = metadados['mpris:artUrl']
        song_art = str(song_art)

        tituloMusica = re.sub("[\(\[].*?[\)\]]", "", tituloMusica)
        tituloMusica = re.sub('[^A-Za-z0-9]+', '', tituloMusica)

        artista = re.sub("[\(\[].*?[\)\]]", "", artista)
        artista = re.sub('[^A-Za-z0-9]+', '', artista)

        print(tituloMusica)
        print(artista)
        print (song_art)

        song ={}
        song["song_artist"] = artista
        song["song_title"] = tituloMusica
        song["song_art"] = song_art

        return song

    except Exception as e:
        return 0

get_song_details()
