import uuid
from datetime import datetime, timedelta
from .activities_repository import ActivitiesRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

# @pytest.mark.skip(reason='This test is not implemented yet.')
def test_registry_activities():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activities_infos = {
        'id': str(uuid.uuid4()),
        'trip_id': trip_id,
        'title': 'Passeio de barco',
        'occurs_at': datetime.strptime('11-07-2024', '%d-%m-%Y')
    }

    activities_repository.registry_activities(activities_infos)

# @pytest.mark.skip(reason='This test is not implemented yet.')
def test_find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activities = activities_repository.find_activities_from_trip(trip_id)
    print(activities)
    return activities