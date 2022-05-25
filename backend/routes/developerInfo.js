const express = require('express');
const router = express.Router();

const developers = require('../data/developers.json');

/* GET login */
router.get('/', function(req, res) {
    var id = req.baseUrl.split('/')[2]
    console.log(id)

    if (id) {
        res.json({ developer:developers[id] })
    } else {
        res.json({ developer:null })
    }
});

module.exports = router;