import click
import subprocess
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from textract2alto.convert_aws import convert

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
# @click.option('-O', '--output-file', default='-', help='Output filename (or "-" for standard output, the default)',
#               type=click.Path(dir_okay=False, writable=True, exists=False, allow_dash=True))
# @click.option('--alto-version', default='4.2', help='Choose version of ALTO-XML schema to produce (older versions may not preserve all features)',
#               type=click.Choice(['4.2', '4.1', '4.0', '3.1', '3.0', '2.1', '2.0']))
# @click.option('--check-words/--no-check-words', default=True, help='Check whether PAGE-XML contains any Words and fail if not')
# @click.option('--check-border/--no-check-border', default=True, help='Check whether PAGE-XML contains Border or PrintSpace')
# @click.option('--skip-empty-lines/--no-skip-empty-lines', default=False, help='Whether to omit or keep empty lines in PAGE-XML')
# @click.option('--trailing-dash-to-hyp/--no-trailing-dash-to-hyp', default=False, help='Whether to add a <HYP/> element if the last word in a line ends in "-"')
# @click.option('--dummy-textline/--no-dummy-textline', default=True, help='Whether to create a TextLine for regions that have TextEquiv/Unicode but no TextLine')
# @click.option('--dummy-word/--no-dummy-word', default=True, help='Whether to create a Word for TextLine that have TextEquiv/Unicode but no Word')
# @click.option('--textequiv-index', default=0, help='If multiple textequiv, use the n-th TextEquiv by @index')
# @click.option('--textequiv-fallback-strategy', default='first', type=click.Choice(['raise', 'first', 'last']), 
#               help="What to do if selected TextEquiv @index is not available: 'raise' will lead to a runtime error, "
#               "'first' will use the first TextEquiv, 'last' will use the last TextEquiv on the element")
# @click.option('--region-order', default='document', help="Order in which to iterate over the regions", type=click.Choice(['document', 'reading-order', 'reading-order-only']))
# @click.option('--textline-order', default='document', help="Order in which to iterate over the textlines", type=click.Choice(['document', 'index', 'textline-order']))
# @click.option('--timestamp-src', default='LastChange', help="Which element to use for the timestamp", type=click.Choice(['Created', 'LastChange', 'none']))
@click.argument("aws-json-file", type=click.Path(dir_okay=False, exists=True))
@click.argument("image-file", type=click.Path(dir_okay=False, exists=True))
def cli(aws_json_file, image_file):
    """Convert an AWS Textract JSON file to a PAGE XML file.

    Also requires the original input image of AWS OCR to get absolute image coordinates."""
    
    convert(aws_json_file, image_file)

if __name__ == "__main__":
    cli()