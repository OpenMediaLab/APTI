/**
 * Created by dtysky on 16/10/11.
 */

(function($) {
    var acceptableType = ["audio/ogg", "audio/acc", "audio/mp3"];
    var state= {
        initDone: false,
        started: false,
        currentId: ''
    };

    setImage("/static/image/default.png");

    $("#file-upload-button")
        .click(function() {
            $('#file-upload').click();
        });

    window.onbeforeunload = function (e) {
        if (state.initDone) {
            deleteTemp(state.currentId);
        }
    };

    $('#file-upload').fileupload({
        dataType: 'json',
        singleFileUploads: true,
        add: function (e, data) {
            console.log(state);
            if (state.initDone) {
                deleteTemp(state.currentId)
            }
            if (state.started) {
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
            state.started = true;
        },
        done: function (e, data) {
            console.log('done', data);
            state.started = false;
            state.initDone = true;
            $('#uploader-start').prop('disabled', true);
            $('#uploader-cancel').prop('disabled', true);
            state.currentId = data.result[0].id;
            setImage('/static/tmp/' + state.currentId + '.tiff');
        },
        fail: function (e, data) {
            console.log(e);
            state.started = false;
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

    function setImage(src) {
        $("#current-image")
            .attr('src', src);
    }

    function deleteTemp(id) {
        $.ajax({
            url: '/delete/' + id,
            method: 'post',
            success: function (data, status) {
                console.log('Delete successful!');
            },
            error: function (error) {
                console.log(error);
            }
        });
    }

})($);