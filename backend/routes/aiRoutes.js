// routes/aiRoutes.js
const express = require('express');
const router = express.Router();
const aiController = require('../controllers/aiController');

// Route for planning a trip
router.post('/plan-trip', aiController.planTrip);

module.exports = router;