$(document).ready(function(){
    $('.like-reply').click(function() {
        var _$this = $(this);
        var pk = _$this.attr('data-id');
        var like_url = "/replies/" + pk + '/like';
        var data = JSON.stringify({
        });
        if(_$this.hasClass('like-active')){
            $.ajax ({
                type : "DELETE",
                url : like_url,
                data:data,
                contentType: 'application/json;charset=UTF-8',
                success: function(response) {
                    if (response.status === '200')
                    {
                        _$this.attr("title","赞");
                        _$this.removeClass("like-active");
                        _$this.addClass("like-no-active");
//                        console.log(_$this.getElementsByClassName('reply-count').innerHTML)
                        like_count = parseInt(_$this.children(".reply-count").text()) - 1;
                        _$this.children(".reply-count").text(like_count);
                    } else {
                        window.location.href = response.url;
                    }
                }});
        }else {
            $.ajax ({
                type : "POST",
                url : like_url,
                data:data,
                contentType: 'application/json;charset=UTF-8',
                success: function(response) {
                    if (response.status === '200')
                    {
                        _$this.attr("title","取消赞");
                        _$this.removeClass("like-no-active");
                        _$this.addClass("like-active");
                        like_count = parseInt(_$this.children(".reply-count").text()) + 1;
                        _$this.children(".reply-count").text(like_count);
                    } else
                    {
                        window.location.href = response.url;
                    }
                }});
        }
    });
    $('.reply-author').click(function() {
        var _$this = $(this);
        var author = _$this.attr('data-id');
        $('#content').focus();
        $('#content').val('@' + author + ' ');
    });
    $('#topic-preview').click(function() {
        var contentType = $('#content_type').val();
        if (contentType == "1") {
            $("#show-preview").html(marked($('#content').val()));
        } else if (contentType == "2") {
            var parser = new Org.Parser();
            var orgDocument = parser.parse($('#content').val());
            var orgHTMLDocument = orgDocument.convert(Org.ConverterHTML, {
                headerOffset: 1,
                exportFromLineNumber: false,
                suppressSubScriptHandling: false,
                suppressAutoLink: false
            });
            $("#show-preview").html(orgHTMLDocument.toString());
        } else {
            $("#show-preview").html($('#content').val());
        }
    });
    $('#tokenfield').tokenfield({
        limit:4
    });
    $('#topic-put-btn').click(function() {
        var _$this = $(this);
        var url = '/topic/' + _$this.attr("data-id");
        if ($('input[name="title"]').val().length < 4 | $('input[name="title"]').val().length > 36){
              text = '<div class="alert alert-info"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><ul><li>标题: 字段长度必须介于 4 到 36 个字符之间。</li></ul></div>';
              $('.alert-self').html(text);
              return false;
        }
        if ($('input[name="tags"]').val().length < 2 | $('input[name="tags"]').val().length > 36){
            text = '<div class="alert alert-info"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><ul><li>节点: 字段总长度必须介于 2 到 36 个字符之间。</li></ul></div>';
            $('.alert-self').html(text);
            return false;
        }
        if ($('textarea[name="content"]').val().length < 6){
            text = '<div class="alert alert-info"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><ul><li>内容: 字段长度必须至少 6 个字符。</li></ul></div>';
            $('.alert-self').html(text);
            return false;
        }
        var data = {
            csrf_token:$('input[name="csrf_token"]').val(),
            title:$('input[name="title"]').val(),
            tags:$('input[name="tags"]').val(),
            category:$('select[name="category"]').val(),
            content:$('textarea[name="content"]').val(),
            content_type:$('select[name="content_type"]').val()
        };
        $.ajax ({
            type : "PUT",
            url : url,
            data:JSON.stringify(data),
            contentType: 'application/json;charset=UTF-8',
            success: function(response) {
                if (response.status === '200') {
                    window.location.href= url;
                }
            }
        });
    });
    $('#topic-post-btn').click(function() {
        var _$this = $(this);
//        console.log('topic-post-btn');
        var url = '/topic';

        if ($('input[name="title"]').val().length < 4 | $('input[name="title"]').val().length > 36){
              text = '<div class="alert alert-info"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><ul><li>标题: 字段长度必须介于 4 到 36 个字符之间。</li></ul></div>';
              $('.alert-self').html(text);
              return false;
        }
        if ($('input[name="tags"]').val().length < 2 | $('input[name="tags"]').val().length > 36){
            text = '<div class="alert alert-info"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><ul><li>节点: 字段总长度必须介于 2 到 36 个字符之间。</li></ul></div>';
            $('.alert-self').html(text);
            return false;
        }
        if (editor.html().length < 6){
            text = '<div class="alert alert-info"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><ul><li>内容: 字段长度必须至少 6 个字符。</li></ul></div>';
            $('.alert-self').html(text);
            return false;
        }
        var data = {
            csrf_token:$('input[name="csrf_token"]').val(),
            title:$('input[name="title"]').val(),
            tags:$('input[name="tags"]').val(),
            category:$('select[name="category"]').val(),
//            content:$('textarea[name="content"]').val(),
            content: editor.html(),
            content_type:$('select[name="content_type"]').val()
        };
        $.ajax ({
            type : "POST",
            url : url,
            data:JSON.stringify(data),
            contentType: 'application/json;charset=UTF-8',
            success: function(response) {
                if (response.status === '200') {
                   window.location.href= url;
                      // document.location.href = 'http://www.cnblogs.com/chenyablog'
                }
            }
        });
//        event.preventDefault();
    });
});
