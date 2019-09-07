#!/usr/bin/python2


gym_start = "1.8.2019"


import datetime
from time import sleep

desktop_html_path = "desktop.html"
mobile_html_path = "mobile.html"


common_beginning = """
<!DOCTYPE html>
<title>combo-mon</title>
<html>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<meta http-equiv="refresh" content="3600"/>
<style>
	@font-face
	{
		font-family: monofonto;
		src: url("monofonto.ttf");
	}
	body
	{
		color: yellow;
		background-color: black;
		font-size: 100px;
		font-weight: bold;
		font-family: monofonto, monospace;
		}
	#wrap
	{
		padding: 10px;
		text-align:center; width:95%;
	}
</style>
<body>
"""

common_end = """
</body>
</html>
"""

def write_html(path, content, mode="a"):
	html_file = open(path, mode)
	html_file.write(content)
	html_file.close()


def write_common_beginning(path):
	write_html(path, common_beginning, "w")


def write_common_end(path):
	write_html(path, common_end)


def write_progress_bar(path, current, goal, color, icon):
	data = """
	<div class="progress">
	<div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="{}" aria-valuemin="0" aria-valuemax="{}" style="width: {}%">{}d</div>
	<div class="progress-bar bg-info" role="progressbar" aria-valuenow="{}" aria-valuemin="0" aria-valuemax="{}" style="width: {}%">{}d</div>
	</div>""".format(current, goal, current, current)
	write_html(path, data)

def create_desktop_html():
	write_common_beginning(desktop_html_path)
	write_progress_bar(desktop_html_path, 10, 30, "blue", "foo.png")
	write_common_end(desktop_html_path)


def main():
	create_desktop_html()


if __name__ == "__main__":
	main()