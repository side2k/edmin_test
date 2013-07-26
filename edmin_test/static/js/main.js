$(function(){
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
});
