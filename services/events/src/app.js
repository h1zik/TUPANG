const express = require('express');
const bodyParser = require('body-parser');
const eventsRouter = require('./routes/events');
const bookingsRouter = require('./routes/bookings');

const app = express();

app.use(bodyParser.json());

app.use('/events', eventsRouter);
app.use('/bookings', bookingsRouter);

const PORT = process.env.PORT || 5001;
app.listen(PORT, () => {
  console.log(`Events service running on port ${PORT}`);
});
