import pytest
from RoomLight_2 import LightingScene, Room, make_hotel, sync_scene


def test_lighting_scene_creation():
    scene = LightingScene(1, "Testi", 50, "warm", "kuvaus")
    assert scene.id == 1
    assert scene.name == "Testi"
    assert scene.brightness == 50
    assert scene.color_temp == "warm"
    assert scene.description == "kuvaus"


def test_room_creation():
    room = Room("101", 1, "Vapaa")
    assert room.id == "101"
    assert room.floor == 1
    assert room.status == "Vapaa"
    assert room.current_scene is None


def test_make_hotel():
    rooms, scenes = make_hotel()

    assert len(rooms) == 10
    assert len(scenes) == 5

    assert rooms[0].id == "101"
    assert rooms[0].status == "Vapaa"

    assert scenes[0].name == "Tervetuloa!"
    assert scenes[1].name == "Yö"


def test_sync_scene_all_rooms(monkeypatch):
    rooms, scenes = make_hotel()

    inputs = iter(["1", "kaikki", "k"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    sync_scene(rooms, scenes)

    for room in rooms:
        assert room.current_scene == "Tervetuloa!"


def test_sync_scene_specific_rooms(monkeypatch):
    rooms, scenes = make_hotel()

    inputs = iter(["2", "101,102", "k"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    sync_scene(rooms, scenes)

    for room in rooms:
        if room.id in {"101", "102"}:
            assert room.current_scene == "Yö"
        else:
            assert room.current_scene is None


def test_sync_scene_floor(monkeypatch):
    rooms, scenes = make_hotel()


    inputs = iter(["1", "kerros:2", "k"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    sync_scene(rooms, scenes)

    for room in rooms:
        if room.floor == 2:
            assert room.current_scene == "Tervetuloa!"
        else:
            assert room.current_scene is None


def test_sync_scene_cancel(monkeypatch):
    rooms, scenes = make_hotel()

    inputs = iter(["1", "kaikki", "e"]) 
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    sync_scene(rooms, scenes)

    for room in rooms:
        assert room.current_scene is None