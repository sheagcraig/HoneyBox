#!/usr/bin/env python


#import argparse
import csv
import pygal
import readline


#def build_argparser():
#    """Create an argument parser.
#
#    Returns:
#        Configured ArgumentParser.
#    """
#    parser = argparse.ArgumentParser(description="Generate SVG box plots.")
#    parser.add_argument("datafile", help="Path to a csv of values.")
#    parser.add_argument("output", help="Path to write output svg.")
#
#    return parser
output = """<!DOCTYPE html>
<html>
  <head>
  <script type="text/javascript" src="http://kozea.github.com/pygal.js/javascripts/svg.jquery.js"></script>
  <script type="text/javascript" src="http://kozea.github.com/pygal.js/javascripts/pygal-tooltips.js"></script>
    <!-- ... -->
  </head>
  <body>
    <figure>
      <!-- Pygal render() result: -->
      %RESULTS%
      <!-- End of Pygal render() result: -->
    </figure>
  </body>
</html>"""


def web_box(req, title, file=None):
    box_plot = pygal.Box()
    box_plot.title = title
    box_plot.title = "Test"
    #result = csv.reader(file.file.read())
    for line in csv.reader(file.file):
        box_plot.add(line[0], [float(num) for num in line[1:]])

    return output.replace("%RESULTS%", box_plot.render())
    #return str(type(csv.reader(file.file)))

def main():
    #parser = build_argparser()
    #args = parser.parse_args()
    box_plot = pygal.Box()
    box_plot.title = raw_input("Please enter a title: ")

    for line in csv.reader(open(args.datafile, "r")):
        print line[0], line[1:]
        box_plot.add(line[0], [float(num) for num in line[1:]])

    # box_plot.render_to_file(args.output)
    box_plot.render_in_browser()


if __name__ == "__main__":
    main()
