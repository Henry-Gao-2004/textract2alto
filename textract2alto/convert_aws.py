from textract2page import convert_file
from ocrd_page_to_alto.convert import OcrdPageAltoConverter 
import os
import subprocess

def convert(response_path: str, img_path: str):
    #convert response to page xml
    convert_file(response_path, img_path, "tmp.xml")

    # convert page xml to alto xml
    converter = OcrdPageAltoConverter(
        alto_version='4.2',
        page_filename="tmp.xml",
        check_words=True,
        timestamp_src='LastChange',
        check_border=False,
        skip_empty_lines=False,
        trailing_dash_to_hyp=False,
        dummy_textline=True,
        dummy_word=True,
        textequiv_index=0,
        textequiv_fallback_strategy='first',
        region_order='document',
        textline_order='document'
    )
    converter.convert()
    with open(img_path+".xml", 'w') as output:
        output.write(str(converter))
        
    # os.system("page-to-alto tmp.xml --no-check-border > "+img_path+".xml") # alternative method

    os.remove("tmp.xml") # remove the temp file


if __name__ == '__main__':
    convert("../resources/1926-Nakcok-UTL-0234.jpg.json", "../resources/1926-Nakcok-UTL-0234.jpg")