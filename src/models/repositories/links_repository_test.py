import pytest # type: ignore
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())

@pytest.mark.skip(reason='This test is not implemented yet.')
def test_registry_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    link_trips_infos = {
        'id': link_id,
        'trip_id': trip_id,
        'link': 'welloworld.com.br',
        'title': 'Hello'
    }

    links_repository.registry_link(link_trips_infos)

@pytest.mark.skip(reason='This test is not implemented yet.')
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    response = link_repository.find_links_from_trip(trip_id)
    print(response)

    assert isinstance(response, list)
    assert isinstance(response[0], tuple)