# RoomLight

Komentorivipohjainen hotellihuoneiden valaistuksen hallintajärjestelmä, jonka avulla voit luoda valaistuskohtauksia ja synkronoida niitä useisiin huoneisiin.

---

# Demo video
[YouTube](https://youtu.be/shFfA8TOVLo)

### Huoneiden hallinta

* Näytä kaikki huoneet (kerros, tila, nykyinen scene)
* Mahdollisuus suodattaa kerroksen mukaan tai valita kaikki huoneet

### Valaistus scenet

* Esiasetetut kohtaukset
* Mukautettujen valaistuskohtauksien luonti
* Kirkkauden ja värilämpötilan määrittäminen

### scenejen synkronointi

* Aseta scene useisiin huoneisiin
* Joustavat valintavaihtoehdot:

  * Yksittäiset huoneet (esim. 101,102)
  * Koko kerros (floor:2)
  * Kaikki huoneet (all)


### Vaatimukset

* Python 3.10+

### Ohjelman suoritus

```bash
python RoomLight_2.py
```

---


### Päävalikon vaihtoehdot

```
1. Näytä kaikki huoneet
2. Näytä valaistuscenet
3. Luo uusi scene
4. Synkronoi kohtaus huoneisiin
0. Poistu
```

---

### Esimerkkikäyttö

1. Valitse valaistus
2. Valitse huoneet:

   * 101,102
   * floor:2
   * all
3. Vahvista synkronointi


---


## Rajoitukset

* Data ei tallennu (nollautuu käynnistyksen yhteydessä)
* Kohtausten muokkaus ja poisto puuttuvat
* Ei rinnakkaisuutta tai oikeaa laitteistointegraatiota

---


