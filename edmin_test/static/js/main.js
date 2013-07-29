function showDialog($dlg, options) {
    $dlg.find("form").find("input[type=text], textarea").val("");
    $dlg.find("form label .errorlist").html("");
    $dlg.find(".modal-body.dialog").show();
    $dlg.find(".modal-body.success").hide();
    $dlg.find(".modal-body.error").hide();    
    if (options) {
        if (options.action) {
            $dlg.find("form").attr("action", options.action);
        }
    }
    if (options && options.action && options.request_values) {
        $.getJSON(options.action, function(values){
            $.each(values.values, function(field, value){
                $label = $dlg.find("form label[for=" + field + "]") 
                $input = $label.find("input, textarea").val(value);
            });
            $dlg.modal();
        });
    } else {
        $dlg.modal();
    }    
}

function cinemaAddDlg() {
    showDialog($("#cinema-add-dlg"));
}

function cinemaEditDlg(editURL) {
    showDialog($("#cinema-edit-dlg"), {'action': editURL, 'request_values':true});
}

function cinemaDeleteDlg(deleteURL) {
    showDialog($("#cinema-delete-dlg"), {'action': deleteURL});
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
                    $dlg.on("hidden", function(){
                        window.location.href = window.location.href;
                    });                    
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
    prepareDlg($("#cinema-edit-dlg"));
    prepareDlg($("#cinema-delete-dlg"));


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
