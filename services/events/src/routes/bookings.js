const express = require('express');
const router = express.Router();
const db = require('../db');

// Create a booking
router.post('/', (req, res) => {
  const { user_id, event_id, booking_date } = req.body;
  db.query('INSERT INTO event_bookings (user_id, event_id, booking_date) VALUES (?, ?, ?)', [user_id, event_id, booking_date], (err) => {
    if (err) throw err;
    res.status(201).json({ message: 'Booking successful' });
  });
});

// Update a booking
router.put('/:id', (req, res) => {
  const { id } = req.params;
  const { user_id, event_id, booking_date } = req.body;
  db.query('UPDATE event_bookings SET user_id = ?, event_id = ?, booking_date = ? WHERE id = ?', [user_id, event_id, booking_date, id], (err) => {
    if (err) throw err;
    res.json({ message: 'Booking updated' });
  });
});

// Delete a booking
router.delete('/:id', (req, res) => {
  const { id } = req.params;
  db.query('DELETE FROM event_bookings WHERE id = ?', [id], (err) => {
    if (err) throw err;
    res.json({ message: 'Booking deleted' });
  });
});

// Get bookings by user
router.get('/:user_id', (req, res) => {
  const { user_id } = req.params;
  db.query(`
    SELECT eb.id, e.name, e.date, e.location, eb.booking_date
    FROM event_bookings eb
    JOIN events e ON eb.event_id = e.id
    WHERE eb.user_id = ?
  `, [user_id], (err, results) => {
    if (err) throw err;
    res.json(results);
  });
});

module.exports = router;
