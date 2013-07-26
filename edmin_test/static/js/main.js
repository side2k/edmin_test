$(function(){
    $(".cinema-add").click(function(){
        $("#cinema-add-dlg").modal({
            'remote': '/cinema/add'
        });
    });
});
