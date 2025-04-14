import requests

käynnistys = input("Paina enter niin saat Chuck Norris vitsin.")

def hae_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        vastaus = requests.get(url)

        if vastaus.status_code == 200:
            json_vastaus = vastaus.json()
            print(json_vastaus["value"])
        else:
            print("Vitsin hakeminen epäonnistui. Statuskoodi:", vastaus.status_code)

    except requests.exceptions.RequestException as e:
        print("Vitsin hakeminen epäonnistui:", e)

    except Exception as ex:
        print("Tapahtui odottamaton virhe:", ex)

hae_vitsi()
