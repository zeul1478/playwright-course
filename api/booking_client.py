import json
import requests


class BookingAPIClient:

    def __init__(self, session) -> None:
        self.session = session

    def create_booking(self, payload):
        return self.session.post("/booking", json=payload)

    def get_booking(self, booking_id):
        return self.session.post(f"/booking/{booking_id}")