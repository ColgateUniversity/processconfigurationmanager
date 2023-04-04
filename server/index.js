const express = require("express")
require("dotenv").config()
const {connectToDb} = require("./dbSetup.js")
const cors = require("cors")
const { getProcesses } = require("./controllers/processInfo/processInfoController.js")


const app = express()
app.use(cors())
const PORT = 4000





// Make Database Connection



// GET Processes


// processInfo

app.get("/", async (req, res) => {
    console.log("/")
    res.status(200).send("Welcome to Express")
})

app.get("/api/v1/processInfo/getProcesses", async (req, res) => {
    console.log("/api/v1/processInfo/getProcesses")
    getProcesses(req, res)
})




app.get("/api/v1/processElements/getProcesses", async (req, res) => {
    console.log("/api/v1/processElements/getProcesses")

})
app.get("/api/v1/processAccessInfo/getProcesses", async (req, res) => {
    console.log("/api/v1/groupInfo/getProcesses")
})
app.get("/api/v1/groupInfo/getProcesses", async (req, res) => {
    console.log("/api/v1/groupInfo/getProcesses")
})
app.get("/api/v1/processUpdateLog/getProcesses", async (req, res) => {
    console.log("/api/v1/processUpdateLog/getProcesses")
})
app.get("/api/v1/scheduledUpdatesInfo/getProcesses", async (req, res) => {
    console.log("/api/v1/scheduledUpdatesInfo/getProcesses")
})


let sql = `SELECT * FROM Sample_processinfo`;

app.listen(PORT, () => {
    
    console.log(`Server listening on ${PORT}`);
});









  




// GET Process Parameters

// GET Scheduled Updates


// GET Log
