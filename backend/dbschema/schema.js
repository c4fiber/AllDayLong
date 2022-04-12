var mongoose = require('mongoose');
  
var imageSchema = new mongoose.Schema({
    name: String,
    imgpath: String,
    syncTime: {type: Date, default: Date.now},
    imgfolderpath: String
});
  
//Image is a model which has a schema imageSchema
  
module.exports = new mongoose.model('Image', imageSchema);