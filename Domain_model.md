# RoomLight Domain Model

## Yleisesti
RoomLight on hotelleille keskitetty valaistuksenhallintajärjestelmä.  
Sen pääajatus on **"Suunnittele kerran, synkronoi kaikkialle"** – eli siis luodaan valaistusskenaario kerran ja levitetään se useisiin huoneisiin yhdellä napsautuksella.

## Pää osa-alueet

### Hotelli
- **Kuvaus**: Edustaa yhtä hotellia (prototyypissä käytetään vain yhtä hotellia).
- **Attribuutit**:
  - id
  - nimi
  - huoneidenLukumäärä

### Huone
- **Kuvaus**: Yksittäinen hotellihuone.
- **Attribuutit**:
  - id (esim. 101, 205, "Sviitti")
  - huoneenNumero
  - tila (Varattu / Vapaa)
  - nykyinenSkenaario (viittaus aktiiviseen valaistusskenaarioon)


### ValaistusSkenaario

- **Kuvaus**: Valaistuksen esiasetus tai tunnelma (esim. Tervetuloa, Uni, Onnittelut).
- **Attribuutit**:
  - id
  - nimi (esim. "Tervetuloa", "Hyvää yötä", "Deep Sleep")
  - kirkkaus (0–100 %)
  - värilämpötila (esim. 2700K–6500K) tai väri (RGB)
  - kuvaus
  - luotu
  - muokattu
- **Suhde**:
  - voidaan synkronoida useisiin Huoneisiin


### Synkronointi
- **Tapahtuma** joka tallentaa skenaarion synkronoinnin huoneisiin
- **Attribuutit**:
  - id
  - skenaarioId
  - kohdeHuoneet (lista huoneiden id:itä tai ryhmä)
  - synkronointiAika
  - tila (Onnistunut / Epäonnistunut)

## Keskeiset suhteet

- **Yksi-moneen**: Hotelli → Huoneet
- **Moneen-moneen**: ValaistusSkenaario ↔ Huone (yksi skenaario voidaan synkronoida moniin huoneisiin)
- **Yksi-moneen**: HuoneRyhmä → Huoneet
- **Yksi-moneen**: ValaistusSkenaario → Synkronointi (historia)

## Pääkäsitteet prototyypissä (MVP)

- Käyttäjä luo ja muokkaa **ValaistusSkenaario**ita (kirkkaus + väripreset)
- Käyttäjä valitsee yhden tai useampia **Huone**ita tai **HuoneRyhmän**
- Käyttäjä painaa **Synkronoi**-painiketta → luodaan Synkronointi-tapahtuma ja huoneiden nykyinenSkenaario päivittyy

