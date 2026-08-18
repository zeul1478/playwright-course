import json
import requests

class BookingAPIClient:
    def __init__(self, session) -> None:
        self.session = session

    def create_booking(self, payload):
        return self.session.post("/booking", json=payload)

    def get_booking(self, booking_id):
        return self.session.get(f"/booking/{booking_id}")  # ← Changed to GET!

    def update_booking(self, booking_id, payload):
        return self.session.put(f"/booking/{booking_id}", json=payload)

    def delete_booking(self, booking_id):
        return self.session.delete(f"/booking/{booking_id}")