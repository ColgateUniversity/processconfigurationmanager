
$(document).ready(function() {
    $('button').click(function(event) {
        var id = $(this).attr('id')
        var formId = $(this).attr('form')
        var buttonName = $(this).attr('name')
        console.log(buttonName + " clicked!")
        
        switch (buttonName) {
            case 'ShowParameters':
                console.log("Show Parameters inside")

                $("." + id).slideToggle("fast", "linear");
                var text = $("#" + id).text()
                $("#" + id).text(text == "Show Parameters" ? "Hide Parameters" : "Show Parameters")

              break;

            case 'Edit':
                event.preventDefault()
                console.log("Edit inside")

                $("." + id).attr('readonly', false);
                $("." + id).focus()
                
                $("#" + id).text("Save")
                $("#" + id).attr('name', "Save");
                $("#" + id).attr('type', "submit");

                break;
            case 'Save':

                console.log("Save Inside")

                
                $("." + id).attr('readonly', true);
                $("." + id).blur()
                
                $("#" + id).text("Edit")
                $("#" + id).attr('name', "Edit");

                break;

            case 'ScheduleAnUpdate':
                console.log("Schedule an Update inside")

                $("." + id).slideToggle("fast", "linear");
         


                 break;

            default:
              console.log("No Corresponding code block found for this button")          }
    });
});

