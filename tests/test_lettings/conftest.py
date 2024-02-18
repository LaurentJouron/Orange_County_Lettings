import pytest
from lettings.models import Address, Letting


@pytest.fixture
def fake_address_fixture():
    return [
        Address(
            id="1",
            number="7217",
            street="Bedford Street",
            city="Brunswick",
            state="GA",
            zip_code="31525",
            country_iso_code="USA",
        ),
        Address(
            id="2",
            number="4",
            street="Military Street",
            city="Willoughby",
            state="OH",
            zip_code="44094",
            country_iso_code="USA",
        ),
        Address(
            id="3",
            number="340",
            street="Wintergreen Avenue",
            city="Newport News",
            state="VA",
            zip_code="23601",
            country_iso_code="USA",
        ),
    ]


@pytest.fixture
def fake_letting_fixture():
    return [
        Letting(
            id="1",
            title="Joshua Tree Green Haus /w Hot Tub",
            address_id="1",
        ),
        Letting(
            id="2",
            title="Oceanview Retreat",
            address_id="2",
        ),
        Letting(
            id="3",
            title="'Silo Studio' Cottage",
            address_id="3",
        ),
    ]


@pytest.fixture
def address_fixture(monkeypatch, fake_address_fixture):
    monkeypatch.setattr(
        "lettings.models.Address",
        lambda: fake_address_fixture,
    )
    return {"address": fake_address_fixture}


@pytest.fixture
def lettings_fixture(monkeypatch, fake_letting_fixture):
    monkeypatch.setattr(
        "lettings.models.Letting",
        lambda: fake_letting_fixture,
    )
    return {"lettings": fake_letting_fixture}
