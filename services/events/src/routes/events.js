const express = require('express');
const router = express.Router();
const db = require('../db');

// Get all events
router.get('/', (req, res) => {
  db.query('SELECT * FROM events', (err, results) => {
    if (err) throw err;
    res.json(results);
  });
});

// Create an event
router.post('/', (req, res) => {
  const { name, date, location } = req.body;
  db.query('INSERT INTO events (name, date, location) VALUES (?, ?, ?)', [name, date, location], (err) => {
    if (err) throw err;
    res.status(201).json({ message: 'Event added' });
  });
});

// Update an event
router.put('/:id', (req, res) => {
  const { id } = req.params;
  const { name, date, location } = req.body;
  db.query('UPDATE events SET name = ?, date = ?, location = ? WHERE id = ?', [name, date, location, id], (err) => {
    if (err) throw err;
    res.json({ message: 'Event updated' });
  });
});

// Delete an event
router.delete('/:id', (req, res) => {
  const { id } = req.params;
  db.query('DELETE FROM events WHERE id = ?', [id], (err) => {
    if (err) throw err;
    res.json({ message: 'Event deleted' });
  });
});

module.exports = router;
