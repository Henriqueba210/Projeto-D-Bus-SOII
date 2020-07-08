import dbus


class spotifyDbus():
    def __init__(self):
        try:
            session_bus = dbus.SessionBus()

            spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
            propriedadesSpotify = dbus.Interface(spotify_bus, "org.freedesktop.DBus.Properties")
            metadados = propriedadesSpotify.Get("org.mpris.MediaPlayer2.Player", "Metadata")

            artista = metadados['xesam:artist']
            artista = str(artista[0])

            tituloMusica = str(metadados['xesam:title'])

            song_art = metadados['mpris:artUrl']
            song_art = str(song_art)

            print(tituloMusica)
            print(artista)
            print(song_art)

            song = {"song_artist": artista, "song_title": tituloMusica, "song_art": song_art}

        except Exception as e:
            print(e)
