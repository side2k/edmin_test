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

$(function(){    
    // cinemas
    $(".cinema-add").click(function(){
        $("#cinema-add-dlg").modal({
            'remote': '/cinema/add'
        });
    });

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
