from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

def test_insert_event():
    event = {
        "uuid": "meu-uuid",
        "title": "meu-title",
        "slug": "meu-slug-aqui",
        "maximum_attendees": 20       
    }
    
    
    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)
    
    