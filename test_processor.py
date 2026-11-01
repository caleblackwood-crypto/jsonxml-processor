from pathlib import Path
from processor import xml_to_records

def test_sample():
    result=xml_to_records(Path(__file__).with_name('sample.xml'))
    assert len(result)==2
    assert result[0]['priority']=='high'
