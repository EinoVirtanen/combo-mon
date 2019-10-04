#!/usr/bin/python2

#----------------------------------------------

trello_start =	"6.9.2019"
keto_start =	"9.9.2019"
sports_start =	"30.9.2019"
c_start =      "5.10.2019"

# "pause", if on hold

c_goal = 14
sports_combo_pb = 55

#----------------------------------------------

desktop_bar_size = 50
desktop_width = 80
desktop_height = 60

mobile_bar_size = 35
mobile_width = 90
mobile_height = 80

#----------------------------------------------

import datetime
from time import sleep
from math import ceil

desktop_html_path = "/usr/share/nginx/html/desk.html"
mobile_html_path = "/usr/share/nginx/html/mobile.html"

#----------------------------------------------

common_end = """
</div>
</div>
</body>
</html>
"""

def write_html(path, content, mode="a"):
	html_file = open(path, mode)
	html_file.write(content)
	html_file.close()


def write_beginning(path, size, width, height, width_adj=1.0, spacing_adj=1.0, bat_logo=" "):
	beginning = """
	<!DOCTYPE html>
	<title>combo-mon</title>
	<html>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<meta http-equiv="refresh" content="3600"/>
	<style>
		:root {{
			--bar-spacing: {}px;
			--font-height: {}px;
			--progress-bar-height: {}px;
			--padding: {}px;
			--padding-neg: {}px;
			--inner-padding: {}px;
                        --padding-mobile-opt: {}px;
		}}
		@font-face {{
			font-family: monofonto;
			src: url("monofonto.ttf");
		}}
		html {{
			height: 100%;
		}}
		body {{
			height: 100%;
			color: yellow;
			background-color: black;
			font-weight: bold;
			font-family: monofonto, monospace;
		}}
		.middle {{
			font-size: var(--bar-spacing);
			width: {}%;
			height: {}%;
			position: absolute;
			top: 0;
			bottom: 0;
			left: 0;
			right: 0;
			margin: auto;
			padding-left: var(--padding);
			padding-right: var(--padding-mobile-opt);
		}}
		.progress-bar-wrapper {{
			position: relative;
			width: 100%;
		}}
		img {{
			position: absolute;
			top: 0;
			left: var(--padding-neg);
			width: var(--progress-bar-height);
			height: var(--progress-bar-height);
		}}
		.height {{
			height: var(--progress-bar-height);
		}}
		.goal {{
			position: absolute;
			right: var(--padding-neg);
			top: 0;
			height: var(--progress-bar-height);
			width: var(--padding);
			color: white;
			text-align: center;
			font-size: {}px;
			vertical-align: middle;
		}}
		div {{
			font-size: var(--font-height);
		}}
                img.hidden {{
                    opacity: 0;
                    }}
                {}
	</style>
	<body>
        <img id="bat" class="hidden" src="battery.png">
	<div class="middle">
	""".format(int(1.5*size*spacing_adj), int(0.8*size), size, int(1.4*size), int(-1.3*size), int(0.5*size), int(size*width_adj), width, height, int(0.65*size), bat_logo)

	write_html(path, beginning, "w")


def write_common_end(path):
	write_html(path, common_end)


def write_progress_bar(icon, path, current, goal, color=" "):
	if goal == "&infin;":
		width = 100
	else:
		width = int(round(100.0*float(current)/float(goal)))
        if current == "0":
                current = " "
	data = """
	<div class="progress-bar-wrapper">
	<div class="goal">{}</div>
	<div class="progress height">
	<div class="progress-bar height progress-bar-striped progress-bar-animated {}" role="progressbar" aria-valuenow="{}" aria-valuemin="0" aria-valuemax="100" style="width: {}%">{}<img src="{}">
	</div>
	</div>
	</div>
	<br>""".format(goal, color, width, width, current, icon)
	write_html(path, data)


def get_color(ratio):
    if ratio == 1:
        return "bg-info"
    elif ratio < 0.25:
        return "bg-danger"
    elif ratio >= 0.25 and ratio < 0.5:
        return "bg-warning"
    else:
        return "bg-success"


def calculate_combo(start):
		return int(float((datetime.datetime.now()-datetime.datetime.strptime(start, '%d.%m.%Y')).days))+1


def write_progress_bars(path):
	if trello_start != "pause":
		write_progress_bar("trello.png", path, str(calculate_combo(trello_start)), "&infin;")
	if keto_start != "pause":
		keto_combo = calculate_combo(keto_start)
                keto_goal = int(ceil(float(keto_combo)/30.0)*30.0)
		write_progress_bar("keto.png", path, str(keto_combo), keto_goal, get_color(float(keto_combo)/keto_goal))
	if sports_start != "pause":
		sports_combo = int(float((datetime.datetime.now()-datetime.datetime.strptime(sports_start, '%d.%m.%Y')).days))+1
		write_progress_bar("sports.png", path, str(calculate_combo(sports_start)), sports_combo_pb, get_color(float(sports_combo)/sports_combo_pb))
	if c_start != "pause":
                c_combo = calculate_combo(c_start)
		write_progress_bar("c.png", path, str(c_combo), c_goal, get_color(float(c_combo)/21))


def create_desktop_html():
	bat_logo = """
img#bat {
    opacity: 100;
    position: absolute;
    top: 20px;
    left: 450px;
    width: 150px;
    height: 40px;
}
"""
	write_beginning(desktop_html_path, desktop_bar_size, desktop_width, desktop_height, 1.0, 0.5, bat_logo)
	write_progress_bars(desktop_html_path)
	write_common_end(desktop_html_path)


def create_mobile_html():
	write_beginning(mobile_html_path, mobile_bar_size, mobile_width, mobile_height, 2.4, 0.3)
	write_progress_bars(mobile_html_path)
	write_common_end(mobile_html_path)


def main():
	while True:
		create_desktop_html()
		create_mobile_html()
		sleep(6*3600)


if __name__ == "__main__":
	main()
