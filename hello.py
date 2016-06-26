import feedparser
from flask import Flask
app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

# @app.route("/")
# def get_news():
# 	# return "no news is good news"
# 	feed = feedparser.parse(BBC_FEED)
# 	first_article = feed['entries'][0]
# 	return """<html>
# 	<body>
# 	      <h1> BBC Headlines </h1>
# 	      <b> {0}</b> <br>
# 	      <i> {1} </i> <br>
# 	      <p> {2} </p> <br>
# 	</body>
# 	</html>""".format(first_article.get("title"),first_article.
# 		get("published"),first_article.get("summary"))
@app.route("/")
@app.route("/<publication>"
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    render_template("home.html",
    title=first_article.get("title"),
    published=first_article.get("published"),
    summary=first_article.get("summary"))

if  __name__ == '__main__':
	app.run(port = 5000, debug = True)