var express = require('express');
var router = express.Router();

const developers = require('../data/developers.json');

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.json({ developers });
});

module.exports = router;
