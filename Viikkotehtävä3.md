# Viikkotehtävä III – RoomLight

## 3a) Product Requirements

### Product Overview
RoomLight on hotellin valaistuksen hallintajärjestelmä, joka mahdollistaa valaistuksen suunnittelun ja synkronoinnin kaikkiin hotellin kaikkiin huoneisiin

Tavoitteena on:
- Yhtenäinen asiakaskokemus
- Manuaalisen työn vähentäminen
- Skaalautuva valaistuksen hallinta

---

### Target Users
- Hotellien johto
- Maintenance / tekninen henkilöstö

---

### Problem
Nykyään valaistusta hallitaan huonekohtaisesti manuaalisesti, mikä:
- vie paljon aikaa  
- aiheuttaa epäyhtenäisyyttä  
- ei skaalaudu suuriin hotelleihin  

---

### Key Features
- **Keskitetty** Yksi näkymä kaikkien huoneiden hallintaan  
- **Huone muokkaaja:** Valaistusskenaarioiden luonti (esim. Welcome, Sleep)  
- **Huoneen valinta:** Huoneiden valinta yksittäin tai ryhmissä  
- **yhden napin synkkaaminen:** Skenaarion jakaminen useisiin huoneisiin yhdellä toiminnolla  
- **vieraan override:** Vieraat voivat silti säätää valoja huoneessa  
- **Skaalautuvuus:** Toimii pienistä hotelleista yli 1000 huoneen kohteisiin  

---

### Functional Requirements
- Käyttäjä voi luoda, muokata ja poistaa skenaarioita  
- Käyttäjä voi valita huoneita/ryhmiä  
- Käyttäjä voi synkronoida skenaarion valittuihin huoneisiin  
- Järjestelmä päivittää tilan nopeasti ja tallentaa asetukset  

---

### Non-Functional Requirements
- Helppokäyttöisyys (ei vaadi teknistä osaamista )  
- Nopea suorituskyky
- Luotettavuus
- Tietoturva (valtuutetut käyttäjät)  
- Yhteensopivuus yleisten valaistusratkaisujen kanssa  

---

## 3b) Prototype Scope

### Prototype Goal
Demonstroida keskeinen arvolupaus:  
**"suunnittele kerran, synkronoi kaikkialle"**

---

### Included in Prototype (MVP)
- Yksinkertainen UI:
  - Lista huoneista  
  - Lista skenaarioista  
- Skenaarion luonti (kirkkaus + väri preset)  
- Useiden huoneiden valinta  
- “Sync” painike  
- Visuaalinen palaute onnistuneista päivityksistä  

---

### Excluded from Prototype
- Oikea laiteintegraatio  
- Käyttäjähallinta (login/roolit)  
- Monimutkaiset valaistusasetukset  
- IoT / reaaliaikainen backend  
- Guest override -logiikka  

---

### Assumptions
- Valaistus simuloidaan käyttöliittymässä  
- Käytössä yksi hotelli  
- Huoneita rajallinen määrä (demo)  

---

### Success Criteria
- Käyttäjä ymmärtää toiminnan nopeasti  
- Scene → Select Rooms → Sync -flow toimii loogisesti  
- Demo on esitettävissä lyhyesti (1–2 min)  