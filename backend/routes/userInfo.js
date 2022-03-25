const express = require('express');
const router = express.Router();

const users = require('../data/users.json');

/* GET login */
router.get('/', function(req, res) {
    var id = req.baseUrl.split('/')[2]
    console.log(id)

    if (id) {
        res.json({ user:users[id] })
    } else {
        res.json({ user:null })
    }
});

module.exports = router;