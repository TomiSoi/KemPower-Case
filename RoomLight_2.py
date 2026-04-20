class LightingScene:
    def __init__(self, id, name, brightness, color_temp, description):
        self.id = id
        self.name = name
        self.brightness = brightness      # 0-100
        self.color_temp = color_temp      # warm / neutral / cool (sisäinen)
        self.description = description


class Room:
    def __init__(self, id, floor, status):
        self.id = id
        self.floor = floor
        self.status = status              # "varattu" / "Vapaa"
        self.current_scene = None         # skenen nimi tai None



COLOR_MAP = {
    "warm": "lämmin",
    "neutral": "neutraali",
    "cool": "viileä"
}


def make_hotel():
    """Luo alkuperäiset huoneet ja skenet"""
    rooms = [
        Room("101", 1, "Vapaa"),
        Room("102", 1, "varattu"),
        Room("103", 1, "Vapaa"),
        Room("104", 1, "varattu"),
        Room("201", 2, "Vapaa"),
        Room("202", 2, "Vapaa"),
        Room("203", 2, "varattu"),
        Room("301", 3, "Vapaa"),
        Room("302", 3, "varattu"),
        Room("Sviitti", 3, "Vapaa"),
    ]

    scenes = [
        LightingScene(1, "Tervetuloa!", 85, "warm", "Lämmin vastaanotto"),
        LightingScene(2, "Yö", 10, "warm", "Hämärä nukkumistila"),
        LightingScene(3, "Uni", 0, "warm", "Valot kokonaan pois"),
        LightingScene(4, "Työ mode", 100, "cool", "Kirkas työntekoa varten"),
        LightingScene(5, "Juhlat", 100, "warm", "Kirkas ja lämmin"),
    ]

    return rooms, scenes


def show_rooms(rooms, selected=None):
    """Näytä huonelista"""
    if selected is None:
        selected = set()

    print("\n--- Huoneet ---")
    print(f"{'ID':<10} {'Kerros':<6} {'Tila':<10} {'Nykyinen skene':<20}")
    print("-" * 50)

    for room in rooms:
        sel = "✔" if room.id in selected else " "
        scene = room.current_scene if room.current_scene else "(ei mitään)"
        status = room.status
        print(f"{room.id:<10} {room.floor:<6} {status:<10} {scene:<20} {sel}")

    print("-" * 50)


def show_scenes(scenes):
    """Näytä kaikki valaistusskenet"""
    print("\n--- Valaistusskenet ---")
    for scene in scenes:
        bar = "█" * (scene.brightness // 10) + "░" * (10 - scene.brightness // 10)
        color_fi = COLOR_MAP.get(scene.color_temp, scene.color_temp)
        print(f"{scene.id}. {scene.name:<22} {scene.brightness:>3}% [{bar}] {color_fi}")
        print(f"   {scene.description}")
    print("-" * 40)


def create_scene(scenes):
    """Luo uusi valaistusskene"""
    print("\n--- Luo uusi skene ---")
    
    name = input("Skene nimi: ").strip()
    if not name:
        print("Virhe: Nimi ei voi olla tyhjä.")
        return

    while True:
        try:
            brightness = int(input("Kirkkaus (0-100): "))
            if 0 <= brightness <= 100:
                break
            else:
                print("Anna numero väliltä 0–100.")
        except ValueError:
            print("Anna kelvollinen numero.")

    print("Värilämpötila: 1) Lämmin  2) Neutraali  3) Viileä")
    ct_choice = input("Valitse (1/2/3): ").strip()
    ct_map = {"1": "warm", "2": "neutral", "3": "cool"}
    color_temp = ct_map.get(ct_choice, "neutral")

    description = input("Lyhyt kuvaus: ").strip()

    # uusi ID
    new_id = max(s.id for s in scenes) + 1
    scenes.append(LightingScene(new_id, name, brightness, color_temp, description))
    print(f"Onnistui! Skene '{name}' luotu.\n")


def sync_scene(rooms, scenes):
    """Synkronoi skene valittuihin huoneisiin"""
    print("\n--- Synkronoi skene huoneisiin ---")

    show_scenes(scenes)
    try:
        scene_id = int(input("Syötä skenen numero: "))
        scene = next((s for s in scenes if s.id == scene_id), None)
        if not scene:
            print("Virhe: Skeneä ei löytynyt.")
            return
    except ValueError:
        print("Virhe: Anna numero.")
        return

    print(f"\nValittu skene: {scene.name}")

    show_rooms(rooms)
    print("\nHuoneiden valintaohjeet:")
    print("  - Kirjoita huoneiden ID:t pilkulla eroteltuna (esim. 101,102,201)")
    print("  - Kirjoita 'kaikki' kaikille huoneille")
    print("  - Kirjoita 'kerros:2' kaikille kerroksen 2 huoneille")

    selection = input("\nValintasi: ").strip().lower()

    selected_ids = set()

    if selection == "kaikki":
        selected_ids = {room.id for room in rooms}
    elif selection.startswith("kerros:"):
        try:
            floor_num = int(selection.split(":")[1])
            selected_ids = {room.id for room in rooms if room.floor == floor_num}
            if not selected_ids:
                print(f"Kerrokselta {floor_num} ei löytynyt huoneita.")
                return
        except:
            print("Virheellinen kerrosformaatti. Käytä: kerros:2")
            return
    else:
        tokens = [t.strip() for t in selection.split(",")]
        all_room_ids = {room.id for room in rooms}
        for t in tokens:
            if t in all_room_ids:
                selected_ids.add(t)
            else:
                print(f"Huonetta '{t}' ei löytynyt.")

    if not selected_ids:
        print("Ei kelvollisia huoneita valittu.")
        return

    print(f"\nValitsit {len(selected_ids)} huonetta:")
    show_rooms(rooms, selected=selected_ids)

    confirm = input(f"\nSynkronoidaanko '{scene.name}' näihin huoneisiin? (k/e): ").strip().lower()
    if confirm != "k":
        print("Synkronointi peruutettu.")
        return

    # Synkronoi 
    for room_id in selected_ids:
        for room in rooms:
            if room.id == room_id:
                room.current_scene = scene.name
                print(f"✓ Synkronoitiin huone {room_id} → {scene.name}")
                break

    print(f"\nOnnistui! {len(selected_ids)} huone(tta) päivitetty skeneen '{scene.name}'.\n")


def main():
    rooms, scenes = make_hotel()

    print("=== RoomLight ===")

    while True:
        print("\nPÄÄVALIKKO")
        print("1. Näytä kaikki huoneet")
        print("2. Näytä valaistusskenet")
        print("3. Luo uusi skene")
        print("4. Synkronoi skene huoneisiin")
        print("0. poistu")

        choice = input("\nValitse toiminto: ").strip()

        if choice == "1":
            show_rooms(rooms)
            input("\nPaina Enter jatkaaksesi...")
        elif choice == "2":
            show_scenes(scenes)
            input("\nPaina Enter jatkaaksesi...")
        elif choice == "3":
            create_scene(scenes)
            input("\nPaina Enter jatkaaksesi...")
        elif choice == "4":
            sync_scene(rooms, scenes)
            input("\nPaina Enter jatkaaksesi...")
        elif choice == "0":
            print("\nNäkemiin!")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")


if __name__ == "__main__":
    main()