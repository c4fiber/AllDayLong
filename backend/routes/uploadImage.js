var express = require('express');
var router = express.Router();
var imgModel = require('../dbschema/schema');
var multer = require('multer');
var imagebaseURL = "http://localhost:3000/uploadedImages/";
var imagefolderpath = "../../public/uploadedImages/";
var jsonfolderpath ="../public/uploadedImages/"

let testfilename;
//image upload

var storage = multer.diskStorage({
  destination:function(req,file,cb){
    cb(null,'./public/uploadedImages')
  },
  filename: function(req,file,cb){
    var date = Date.now();
    var basename = Buffer.from(file.originalname,"utf8").toString('base64');
    var path = require("path");
    var filename = date +'-'+ basename + path.extname(file.originalname);

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
        return console.log("please check the file extension") ;
      } else {
        if (req.file == undefined) {
          return console.log("please select a file") ;
        } else {
          console.log(req.file) ;
          var spawn = require('child_process').spawn;
          var net = spawn('python',['./RunOCREngine.py',imagefolderpath + req.file.filename], {cwd: './ocr-modules/OCR-Attn'});

          net.stdout.on('data',function(data){
            console.log('not err');
          })
          net.stderr.on('data',function(data){
            console.log('err occured: '+ data);
            console.log('-------------------');
          })
          net.on('exit', function(){
            testfilename=req.file.filename;
            console.log(testfilename);
          });
        }
      }
    });
});

////////////////////////////////////////////////////
// Get 관련

router.get('/',(req,res,next)=>{
  var test = require(jsonfolderpath+testfilename+".json");
  var test2=[imagebaseURL+"ocred_"+testfilename];
  res.json({test,test2});
 
  console.log(testfilename);
  testfilename=null;
});

module.exports = router;
