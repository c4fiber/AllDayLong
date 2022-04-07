var express = require('express');
var router = express.Router();
var imgModel = require('../dbschema/schema');
var multer = require('multer');
var dbconfig = require('../config/db');
var mongoose = require('mongoose');
var imagebaseURL = "http://localhost:3000/uploadedImages/";
var imagefolderpath = "../public/uploadedImages/";

var app     = express();

//image upload

var storage = multer.diskStorage({
    destination:function(req,file,cb){
        cb(null,'./public/uploadedImages')
    },
    filename: function(req,file,cb){
      var date = Date.now();
      var filename = date +'-'+ file.originalname;
      cb(null,filename);
           
      var newimagedata = new imgModel({
        name:filename,
        imgpath:imagebaseURL + filename,
        syncTime:date,
        imgfolderpath: imagefolderpath + file.originalname
      });
      newimagedata.save(function(error,data){
        if(error){
          console.log(error);
        }else{
          console.log('Saved!');
        }
      });
    }
  });
  var fileFilter = (req, file, cb) => {
    if (file.mimetype==='image/jpeg'|| file.mimetype==='image/png' || file.mimetype ==='image/jpg' ) {
   
    cb(null, true);
   
    } else {
    cb(null, false);
    }
   };
var uploadedimage = multer({storage: storage,fileFilter: fileFilter }).single("file");



//////////////////////////////////////////////////////
// Post 관련

router.post('/',(req,file,res)=>{
    
    uploadedimage(req,res,(err) => {
     
      if (err) {
        return console.log("hello world") ;
    } else {
      if (req.file == undefined) {
        return console.log("please select a file") ;
      }else{
       console.log(req.file) ;
      }
    }
  });
});




////////////////////////////////////////////////////
// Get 관련

router.get('/',(req,res,next)=>{
  imgModel.find()
    .exec()
    .then(docs =>{
        console.log(docs);
        })


});



module.exports = router;