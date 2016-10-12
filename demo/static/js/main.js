/**
 * Created by dtysky on 16/10/11.
 */

(function($) {
    var acceptableType = ["audio/ogg", "audio/acc", "audio/mp3"];

    $('#file-upload').fileupload({
        dataType: 'json',
        singleFileUploads: true,
        submit: function (e, data) {
            var allow = true;
            $.each(data.files, function (index, file) {
                if (acceptableType.indexOf(file.type) === -1) {
                    alert('File type mast be ' + acceptableType.join(', '));
                    allow = false;
                }
            });
            return allow;
        },
        done: function (e, data) {
            $.each(data.result.files, function (index, file) {
                $('<p/>').text(file.name).appendTo(document.body);
            });
        },
        progress: function (e, data) {
            var progress = parseInt(data.loaded / data.total * 100, 10);
            console.log(progress);
            $('#progress-bar').css(
                'width',
                progress + '%'
            );
        }
    });
})($);