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



const connectToDb = () => {
    console.log("Called")
    var connection = new Connection(config);  
    connection.on('connect', (err) => {
        if (err) {
          console.log(err)
        } else {
          console.log("Connected to the database")
        }
      })

    connection.connect()
}

module.exports = {connectToDb}

