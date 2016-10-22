/**
 * Created by Ernst-JanHuijbers on 20-10-16.
 */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

function update_filter(checkBox){
    var cb_id = checkBox.id;
    var cb_val = checkBox.checked;
    var csrf_token = getCookie('csrftoken');
    $.ajax({
        url: "api/filter",
        type: 'POST',
        data: {'filter_id':cb_id,
               'filter_val':cb_val },

        success: function(json) {
            console.log("Filter values gepost");
            $('#calendar').fullCalendar( 'refetchEvents' );
        },

        error: function (xhr, errmsg, err) {
            console.log("Failure");
            console.log(xhr);
            console.log(errmsg);
            console.log(err);
        },
    })
}

function set_filter(filter){
//    todo: gebruikersprofiel bevat filter opties. Na inloggen moeten die ingesteld worden in het filter.
}