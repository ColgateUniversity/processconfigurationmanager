from datetime import date

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
import requests

# Models representing the tables from the database
from .models import processInfo
from .models import processElements
from .models import groupInfo
from .models import processAccessInfo
from .models import processUpdateLog
from .models import scheduledUpdatesInfo

ms_identity_web = settings.MS_IDENTITY_WEB


def index(request):

    print("Request is")
    print(request.POST)

    if (not(request.identity_context_data.authenticated)):
        return redirect('sign_in')
    

   

   

    if (request.method == "POST"):
        print("Request method is post")

        if ("Update" in request.POST):
            print("Update")
            processID = request.POST["processID"]

            # Get the Username 
            userName = request.POST["userName"]

            #Get the processName
            processName = request.POST["processName"]

            groupInfoObject = groupInfo.objects.get(pk = "1")

            parameterName = request.POST["parameterName"]
            
            valueAfter = request.POST["parameterValue"]
            print(valueAfter)

            

            retrievedObjects = processElements.objects.all().filter(processID = processID)
            valueBefore = 0
            for object in retrievedObjects:
                print("Object")
                print(object.elementName)
                print(parameterName)

                if (object.elementName == parameterName):
                        print("Same parameter")

                        if (valueBefore != valueAfter):
                            print("Value has changed")

                            valueBefore = object.elementValue
                            processElementID = object.processElementID

                            processInfoObject = processInfo.objects.get(pk = processID)
                    
                            processElementObject = processElements.objects.get(pk = processElementID)

                            if ("Update" in request.POST):
                                print("Performing an Update")

                                object.elementValue = valueAfter
                                object.save()
                                
                                processInfoObject = processInfo.objects.get(pk = processID)
                    
                                processElementObject = processElements.objects.get(pk = processElementID)


                                update = processUpdateLog(processID=processInfoObject, userID = userName, groupID = groupInfoObject, processElementID = processElementObject,valueBefore = valueBefore, valueAfter = valueAfter)

                                update.save()

                            if ("Schedule" in request.POST):
                                print("Performing a scheduled update")

                                effectiveDate = request.POST["effectiveDate"]
                                scheduledUpdate = scheduledUpdatesInfo(processID=processInfoObject, userID = userName, groupID = groupInfoObject, processElementID = processElementObject,valueBefore = valueBefore, valueAfter = valueAfter, dateScheduled = effectiveDate )


                                scheduledUpdate.save()





        ### Logging the Update ###

        # Process ID for which the update was performed
        
                

    # Getting all the processes from processInfo Table
    '''
        processID
        processName
        processDescription
        processType
    '''
    processes = processInfo.objects.all()
    processList = []


    x = requests.get("http://localhost:4000/api/v1/processInfo/getProcesses")
    print("This is X")
    print(x.text)
    
    for process in processes:
        
        valueArray = []

        for object in processElements.objects.all().filter(processID = process):
            print("Element Name")
            print(object.elementName)
            valueArray.append([object.elementName, object.elementValue])

        print("-------")
        print(process)
        print(valueArray)
        print("-------")


        processList.append([
            process.processID, process.processName, process.processDescription, valueArray
        ])

    updates = processUpdateLog.objects.all()

    updatesArray = []
    for update in updates:
       

        processName = (processInfo.objects.get(pk = update.processID.processID)).processName

        userID = update.userID

        groupName = groupInfo.objects.get(pk = "1").groupName
        elementName = (processElements.objects.get(pk = update.processElementID.processElementID)).elementName
        valueBefore = update.valueBefore
        valueAfter = update.valueAfter
        timeStamp = update.timestamp

        updatesArray.append([
            processName, userID, groupName, elementName, valueBefore, valueAfter, timeStamp
        ])


    updatesArray.reverse()


    

    return render(request, "auth/status.html", {"processes":processList, "updates":updatesArray})

@ms_identity_web.login_required
def token_details(request):
    return render(request, 'auth/token.html')

@ms_identity_web.login_required
def call_ms_graph(request):
    ms_identity_web.acquire_token_silently()
    graph = 'https://graph.microsoft.com/v1.0/users'
    authZ = f'Bearer {ms_identity_web.id_data._access_token}'
    results = requests.get(graph, headers={'Authorization': authZ}).json()

    # trim the results down to 5 and format them.
    if 'value' in results:
        results ['num_results'] = len(results['value'])
        results['value'] = results['value'][:5]

    return render(request, 'auth/call-graph.html', context=dict(results=results))

