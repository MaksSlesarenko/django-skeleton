$(function(){
    
    $('<div id="ajax-spinner">').ajaxStart(function () {
        $(this).show();
    }).ajaxComplete(function () {
        $(this).hide();
    }).appendTo($('.nav-collapse'));


    $("#alert-messages").ajaxError(function(event, jqXHR, ajaxSettings, thrownError) {
        if (ajaxSettings.dataType === 'json') {
            try {
                var data = jQuery.parseJSON(jqXHR.responseText);
                
                if (data.django_messages && data.django_messages.length) {
                    displayAlerts(data.django_messages);
                    return;
                }
            } catch (error) {
            }
        }
        createAlert('error', 'Error requesting page "' + ajaxSettings.url + '"');
    }).ajaxSuccess(function (event, jqXHR, ajaxSettings) {
        if (ajaxSettings.dataType === 'json') {
            try {
                var data = jQuery.parseJSON(jqXHR.responseText);
                displayAlerts(data.django_messages);
            } catch (error) {
                return;
            }
        }
    }).children().each(function(i){
        $(this).delay(4000 + (i * 1000)).fadeOut();
    });

    $(document).ajaxSend(function(event, xhr, settings) {
        function getCookie(name) 
        {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        function sameOrigin(url) 
        {
            // url could be relative or scheme relative or absolute
            var host = document.location.host; // host + port
            var protocol = document.location.protocol;
            var sr_origin = '//' + host;
            var origin = protocol + sr_origin;
            // Allow absolute or scheme relative URLs to same origin
            return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                // or any other URL that isn't scheme relative or absolute i.e relative.
                !(/^(\/\/|http:|https:).*/.test(url));
        }
        function safeMethod(method) 
        {
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
    
        if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        	console.log(document.cookie);
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    });
    
    $('body').on('click', '.ajax-modal', function(e) {
        e.preventDefault();

        var $this = $(this);
        var url   = $this.attr('href');
        

        $.get(url, function(data) {
            var dialog = $('<div class="modal hide fade"></div>').appendTo('body');
            
            console.log(dialog, data);
            dialog.append(data.form);
            dialog.modal();

            
            $('.ajax-form').ajaxForm({
                dataType: 'json',
                success: function(data) {
                    ajaxFormHandler(data, dialog, $this);
                }
            });
        });
    }).on('click', '.ajax-post, .ajax-get', function(e) {
        e.preventDefault();

        var $this = $(this);
        var callback = $this.attr('data-callback');

        $.ajax({
            type: $this.is('.ajax-post') ? "POST" : "GET",
            url: $this.attr('href'), 
            dataType: 'json'
        }).done(function(data) {
            if (window[callback]) {
                window[callback].call($this, data);
            }
        });
    });
    
    function ajaxFormHandler(data, dialog, el){
        if (true === data.success) {
            dialog.modal('hide');
            
            var callback = el.attr('data-callback');

            if (window[callback]) {
                window[callback].call(el);
            }
        } else {
            dialog.html(data.form).find('form').ajaxForm({
                dataType: 'json',
                success: function(data) {
                    ajaxFormHandler(data, dialog, el);
                }
            });
        }
    }
});

function displayAlerts(messages)
{
    for (var i in messages) {
        createAlert(messages[i].level, messages[i].message, messages[i].extra_tags);
    }
}

function createAlert(level, message, tags)
{
    switch (level) {
        case 25:
            type = 'success';
            break;
        case 30:
        case 40:
            type = 'error';
            break;
        case 10:
        case 20:
        default:
            type = 'info';
            break;
    }
    return $('\
    <div class="hide alert alert-block alert-'+type+'">\
        <button type="button" class="close" data-dismiss="alert">&times;</button>\
        <p>'+message+'</p>\
    </div>').appendTo($("#alert-messages")).fadeIn().delay(4000).fadeOut();
}