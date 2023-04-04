/*
var Request = require('tedious').Request; 
var Connection = require('tedious').Connection;  

const userName = "configmgrusr"
const password = "33aiSBsWfW6Q"
const server = "SQLCLUS01.colgate.edu"


var config = {  
    server: server,  //update me
    authentication: {
        type: 'default',
        options: {
            userName: userName, //update me
            password: password  //update me
        }
    },
    options: {
        // If you are on Microsoft Azure, you need encryption:
        encrypt: true,
        database: 'ColgateIntegrations',  //update me
        trustServerCertificate: true,
    }
};  




const getProcesses = (req, res) => {

    var connection = new Connection(config);  
    connection.on('connect', function(err) {  
        // If no error, then good to proceed.  
        console.log("Connected");  
        console.log("getProcesses called")
            var request = new Request("SELECT * from [configmgr].[processInfo]", (err) => {

            if (err){
                console.log(`Error Encountered: ${err}`)
            }

            var result = "";  
            request.on('row', function(columns) {  
                columns.forEach(function(column) {  
                if (column.value === null) {  
                    console.log('NULL');  
                } else {  
                    result+= column.value + " ";  
                }  
                });  
                console.log(result);  
                result ="";  
            });  ``
        
    });  

    


        request.on('done', function(rowCount, more) {  
            console.log(rowCount + ' rows returned');  
            });  
            
            // Close the connection after the final event emitted by the request, after the callback passes
            request.on("requestCompleted", function (rowCount, more) {
                connection.close();
            });
            connection.execSql(request);

    })
}
*/


const getProcesses = (req, res) => {
    var sql = require("mssql");

    var config = {
        user: 'configmgrusr', // change
        password: '33aiSBsWfW6Q', //cjhange
        server: 'SQLCLUS01.colgate.edu', 
        database: 'ColgateIntegrations', 
    
        options: {
            
            trustServerCertificate: true // change to true for local dev / self-signed certs
          }
    }

    ;

       // connect to your database
       sql.connect(config, function (err) {
    
        if (err) {
            console.log(err)
        } else {
            console.log("Connected")
        }

        
        
        // create Request object
        var request = new sql.Request();
           
        // query to the database and get the records
        request.query('select * from configmgr.processInfo', function (err, result) {
            
            if (err) console.log(err)

            res.send(result.recordset);
            
        });
    });
}



module.exports = {getProcesses}

