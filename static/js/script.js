$(document).ready(function () {

    $('#btn-write-post').click(function () {
        $('#form-write-post').removeClass('d-none')
    })

    $('.check-post-open').click(function(){
        var id_input = $(this).children('input').attr('id')
        if(id_input == 'check-post-lock'){
            $('#row-password').removeClass('d-none')
            $('#input-post-pwd').addAttr('required')
        }else{
            $('#row-password').addClass('d-none')
            $('#input-post-pwd').removeAttr('required')
        }
    })

})