import json
import xml.etree.ElementTree as ET


def json_to_plist(json_file, plist_file):
    """ convert json to plist for Mac OSX
    Args:
        json_file (str): file path of json data (input)
        plist_file (str): file path of plist data (output)
    """

    # load JSON data
    with open(json_file) as f:
        data = json.load(f)

    # build plist
    _DECLARATION = ('<?xml version="1.0" encoding="UTF-8"?>'
                    '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">' )
    plist = ET.Element('plist', attrib={'version': '1.0'})
    tree = ET.ElementTree(element=plist)
    array = ET.SubElement(plist, 'array')

    for k, v in data.items():
        dct = ET.SubElement(array, 'dict')

        # shortcut (key) : phrase (value)
        key = ET.SubElement(dct, 'key')
        key.text = 'phrase'
        string = ET.SubElement(dct, 'string')
        string.text = v

        key = ET.SubElement(dct, 'key')
        key.text = 'shortcut'
        string = ET.SubElement(dct, 'string')
        string.text = k

    with open(plist_file, 'wb') as f:
        f.write(_DECLARATION.encode('utf-8'))
        tree.write(f, encoding='utf-8')

    print('Successfully converted!')
    print('  {} -> {}'.format(json_file, plist_file))


if __name__ == '__main__':
    json_to_plist('pgo_dict.json', 'Text Substitutions.plist')
