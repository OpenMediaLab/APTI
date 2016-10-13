/**
 * Created by dtysky on 16/10/11.
 */

(function($) {
    var acceptableType = ["audio/ogg", "audio/acc", "audio/mp3"];

    $("#file-upload-button")
        .click(function() {
            $('#file-upload').click();
        });

    $('#file-upload').fileupload({
        dataType: 'json',
        singleFileUploads: true,
        add: function (e, data) {
            if (!data.started) {
                data.started = false;
            }
            if (data.started) {
                data.abort();
            }
            $('#uploader-start')
                .prop('disabled', false)
                .click(function () {
                    data.submit();
                });
            $('#uploader-cancel')
                .prop('disabled', true)
                .click(function () {
                    data.abort();
                });
            $('#file-name').text(data.files[0].name);
        },
        submit: function (e, data) {
            var allow = true;
            $.each(data.files, function (index, file) {
                if (acceptableType.indexOf(file.type) === -1) {
                    alert('File type mast be ' + acceptableType.join(', '));
                    allow = false;
                }
            });
            if (allow) {
                $('#uploader-start').prop('disabled', true);
                $('#uploader-cancel').prop('disabled', false);
            }
            return allow;
        },
        started: function (e, data) {
            data.started = true;
        },
        done: function (e, data) {
            console.log('done');
            data.started = false;
            $('#uploader-start').prop('disabled', true);
            $('#uploader-cancel').prop('disabled', true);
        },
        fail: function (e, data) {
            console.log(e);
            data.started = false;
            $('#uploader-start').prop('disabled', true);
            $('#uploader-cancel').prop('disabled', true);
            $('#progress-bar').css('width', 0);
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