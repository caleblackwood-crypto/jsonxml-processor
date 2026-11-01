import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path

def xml_to_records(path):
    root=ET.parse(path).getroot()
    if root.tag!='tickets': raise ValueError('Root element must be tickets')
    records=[]
    for node in root.findall('ticket'):
        ticket_id=node.get('id')
        title=node.findtext('title')
        priority=node.findtext('priority')
        if not ticket_id or not title or priority not in ('low','medium','high'):
            raise ValueError('Invalid ticket: id/title/priority required')
        records.append({'id':ticket_id,'title':title,'priority':priority})
    return records

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('input',type=Path);parser.add_argument('output',type=Path)
    args=parser.parse_args()
    args.output.write_text(json.dumps(xml_to_records(args.input),indent=2),encoding='utf-8')
    print(f'Wrote {args.output}')
if __name__=='__main__':main()
