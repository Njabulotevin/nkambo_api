from flask import session
from decouple import config
from utils.token import gen_token
from middlewares.auth import protectedRoute
import bcrypt
from .eventDAO import EventDAO
from utils.token import decode_token
from .eventModel import EventGuestSchema, EventGuest
from ..guests.guestModel import Guest


class EventService:
    eventDAO = EventDAO()

    def create_event(self, data):
        if self.event_exist(data["name"]):
            return None
        event = self.eventDAO.save_event({**data, "cover_url": None, "guest_speaker": []})
        return event

    def event_exist(self, event_name):
        event = self.eventDAO.find_by_query({"name": event_name})
        if event:
            return True
        return False

    def add_guest(self, event_id: str, guest):
        return self.eventDAO.save_guest(event_id, guest)
