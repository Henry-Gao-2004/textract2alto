from textract2page import convert_file
from ocrd_page_to_alto.convert import OcrdPageAltoConverter 
import os
import subprocess

def convert(response_path: str, img_path: str):
    convert_complex(response_path, img_path, '4.2', True, False, False, False, True, True, 0, 'first', 'document', 'document', 'LastChange')

def convert_complex(response_path, img_path, alto_version, check_words, check_border, skip_empty_lines, trailing_dash_to_hyp, dummy_textline, dummy_word, 
         textequiv_index, textequiv_fallback_strategy, region_order, textline_order, timestamp_src):
    #convert response to page xml
    convert_file(response_path, img_path, "tmp.xml")

    # convert page xml to alto xml
    converter = OcrdPageAltoConverter(
        alto_version=alto_version,
        page_filename="tmp.xml",
        check_words=check_words,
        timestamp_src=timestamp_src,
        check_border=check_border,
        skip_empty_lines=skip_empty_lines,
        trailing_dash_to_hyp=trailing_dash_to_hyp,
        dummy_textline=dummy_textline,
        dummy_word=dummy_word,
        textequiv_index=textequiv_index,
        textequiv_fallback_strategy=textequiv_fallback_strategy,
        region_order=region_order,
        textline_order=textline_order
    )
    converter.convert()
    with open(img_path+".xml", 'w') as output:
        output.write(str(converter))
        
    # os.system("page-to-alto tmp.xml --no-check-border > "+img_path+".xml") # alternative method

    os.remove("tmp.xml") # remove the temp file


if __name__ == '__main__':
    convert("../resources/1926-Nakcok-UTL-0234.jpg.json", "../resources/1926-Nakcok-UTL-0234.jpg")