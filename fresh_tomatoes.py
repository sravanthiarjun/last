import re
import os
import webbrowser

main_head = '''
<!DOCTYPE html>
<html>
<head>
    <script src="https://code.jquery.com/jquery-1.12.3.min.js"
    integrity="sha256"-aaODHAgvwQW1bFOGXMeX+pC4PZIPsvn2h1sArYOhgXQ="
        crossorigin = "anonymous">
    </script>
    <link href = "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/"
    "bootstrap.min.css" rel="stylesheet" type="text/css" />
    <script src = "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/"
    "bootstrap.min.js">
    </script>
    <script>
        $(document).ready(function () {
            $("#myModal").on("hidden.bs.modal", function () {
                $("#iframeYoutube").attr("src", "#");
            })
        })
        function change(video) {
            var iframe = document.getElementById("iframeYoutube");
            iframe.src = "https://www.youtube.com/embed/" + video;
            $("#myModal").modal("show");
       }
    </script>
    <style>
    .one{
color:black;
}
.two {
float:left;
margin-left:20px;
color:green;
}
.three{
float:left;
margin-left:20px;
color:blue;
}
.four{
float:left;
margin-left:20px;
color:black;
}
.five{
float:left;
margin-left:20px;
color:red;
margin-top:40px;
}
.six{
float:left;
margin-left:20px;
color:blue;
margin-top:40px;
}
.two:hover{
background-color:red;
}
.three:hover{
background-color:green;
}
.four:hover{
background-color:blue;
}
.five:hover{
background-color:orange;
}
.six:hover{
background-color:black;
}
'''
main_content = '''
<body>
    <h1>MOVIE TRAILER</h1>
<div class="two">
<img class="two"onclick=changeVideo("mhhb6JAJKbE") src="https://bit.ly/2kcHbu1"
alt="movie1"style="width:400px;height:450px;">
<h2>rangastalam</h2>
</div>
<div class="three">
<img class="three"onclick=changeVideo("UcIL3qsd1-0")
    src="https://bit.ly/2J0YHiT"alt="movie2"style="width:400px;height:450px;">
<h2>ok bangaram</h2>
</div>
<div class="four">
<img class="four"onclick=changeVideo("CnbspuM3jxU")
src="https://bit.ly/2IXRO1k"
alt="movie2"style="width:400px;height:450px;">
<h2>lovers</h2>
</div>
<div class="five">
<img class="five"onclick=changeVideo("cmf3R2PNMJ0")
src="https://bit.ly/2s3B5Q2"
alt="movie4"style="width:400px;height:450px;">
<h2>nenu local</h2>
</div>
<div class="six">
<img class="six"onclick=changeVideo("VgQUwsUHdqc") src="https://bit.ly/2kcHbu1"
alt="movie5"style="width:350px;height:450px;">
<h2>golmol</h2>
</div>
</div>
    <div class="modal fade" id="myModal"
    tabindex="-1"aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
    <div class="modal-content">
     <div class="modal-body">
        <div class="modal-footer">
            <button type="button" data-dismiss="modal">&times;</button>
        </div>
            <iframe id="iframeYoutube" width="555" height="350"
            src="" frameborder="1"></iframe>
      </div>
    </div>
    </div>
    </div>
</style>
</head>
</body>
</html>
'''
movie_title_content = '''
<div class="col-md-6 col-lg-4 movie-title text-center" data-trailer-yutube-
id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}"width="220" height="342">
    <h2 style="color:white;">{movie_title}</h2>
</div>
'''


def create_movie(movies):
    content = ''
    for i in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', i.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', i.trailer_youtube_url)
        trailer_youtube_url = (youtube_id_match.group(0) if youtube_id_match
                               else None)
        content += movie_title_content.format(
                   movie_title=i.title,
                   poster_image_url=i.poster_image_url,
                   trailer_youtube_id=trailer_youtube_url
        )
    return content


def open_page(movies):
    output_file = open('fresh_tomatoes.html', 'w')
    rendered_content = main_content.format(
                                           movie_tiles=create_movie(movies))
    output_file.write(main_head + rendered_content)
    output_file.close()
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
