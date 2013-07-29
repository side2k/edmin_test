function cinemaAddDlg() {
    var $dlg = $("#cinema-add-dlg");
    $dlg.find("form").find("input[type=text], textarea").val("");
    $dlg.find("form label .errorlist").html("");
    $dlg.find(".modal-body.dialog").show();
    $dlg.find(".modal-body.success").hide();
    $dlg.find(".modal-body.error").hide();    
    $dlg.modal();
}

function cinemaEditDlg(editUrl) {
    $("#cinema-edit-dlg").modal({
        'remote': editUrl
    });
}

function presentationAddDlg(addUrl) {
    $("#presentation-add-dlg").modal({
        'remote': addUrl
    });
}

function presentationDeleteDlg(deleteUrl) {
    $("#presentation-delete-dlg").modal({
        'remote': deleteUrl
    });    
}

function showFieldError($dlg, field, error) {
    var $errorlist = $dlg.find("form label[for=" + field + "] ul.errorlist");
    if ($errorlist.length) {
        $errorlist.html("<li>" + error + "</li>");
    }
}

function prepareDlg($dlg) {
    $dlg.find("form").ajaxForm({
        'dataType': 'json',
        'success': 
            function(response){
                if (response.success) {
                    $dlg.find(".modal-body.dialog").hide();
                    $dlg.find(".modal-body.success").show();
                } else {
                    $dlg.find("form ul.errorlist").html("");
                    $.each(response.errors, function(field, error){
                        showFieldError($dlg, field, error);
                    });
                }
            },
        'error': 
            function(response) {
                $dlg.find(".modal-body.dialog").hide();
                $dlg.find(".modal-body.success").hide();
                $dlg.find(".modal-body.error").show();
            }
    });
}

$(function(){    
    // cinemas
    prepareDlg($("#cinema-add-dlg"));


    $("button.cinema-delete").click(function(){
        var cinema_id = $(this).attr('data-cinema');
        $("#cinema-delete-dlg").modal({
            'remote': '/cinema/' + cinema_id + '/delete'
        });
    });

    // presentations

    $(".presentations-date").datepicker({
        'format': 'yyyy-mm-dd'
    });
    $(".presentations-date").on("hide", function(){
        var date = $(".presentations-date input").val();
        window.location = "/cinema/" + CINEMA_ID + "/" + date;
    });
});
