** Events **

Create Event: POST http://localhost:5000/events with JSON payload 
{ "name": "Music Festival", "date": "2024-08-15", "location": "Central Park" }

Get All Events: GET http://localhost:5000/events

Update Event: PUT http://localhost:5000/events/1 with JSON payload 
{ "name": "Updated Music Festival", "date": "2024-08-16", "location": "Updated Park" }

Delete Event: DELETE http://localhost:5000/events/1

Create Booking: POST http://localhost:5000/events/bookings with JSON payload 
{ "user_id": 1, "event_id": 1, "booking_date": "2024-08-15" }

Get Bookings by User: GET http://localhost:5000/events/bookings/1

Update Booking: PUT http://localhost:5000/events/bookings/1 with JSON payload 
{ "user_id": 1, "event_id": 1, "booking_date": "2024-08-16" }

Delete Booking: DELETE http://localhost:5000/events/bookings/1

** Hotels **

Create Event: POST http://localhost:5000/hotels with JSON payload 
{ "name": "Music Festival", "location": "Jakarta", "price": "100" }

Get All Events: GET http://localhost:5000/hotels

Update Event: PUT http://localhost:5000/hotels/1 with JSON payload 
{ "name": "Music Festival", "location": "Jakarta", "price": "100" }

Delete Event: DELETE http://localhost:5000/hotels/1

Create Booking: POST http://localhost:5000/hotels/bookings with JSON payload 
{ "user_id": 1, "hotel_id": 1, "booking_date": "2024-08-15", "nights": 3}

Get Bookings by User: GET http://localhost:5000/events/bookings/1

Update Booking: PUT http://localhost:5000/hotels/bookings/1 with JSON payload 
{ "user_id": 1, "hotel_id": 1, "booking_date": "2024-08-15", "nights": 3}

Delete Booking: DELETE http://localhost:5000/hotels/bookings/1
