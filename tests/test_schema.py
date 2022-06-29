from lxml import etree
import pathlib
import pytest

here = pathlib.Path(__file__).resolve().parent
example_files = (here.parent / 'examples').glob('*.xml')


def test_schema():
    # Checks that the schema is valid xsd
    xmlschema_doc = etree.parse(str(here / '..' / 'schemas' / 'HPXML.xsd'))
    xmlschema = etree.XMLSchema(xmlschema_doc)  # noqa: F841

@pytest.mark.parametrize('filename', example_files, ids=lambda x: x.stem)
def test_example_file(filename):
    xmlschema_doc = etree.parse(str(here / '..' / 'schemas' / 'HPXML.xsd'))
    xmlschema = etree.XMLSchema(xmlschema_doc)  # noqa: F841
    doc = etree.parse(str(filename))
    assert xmlschema.validate(doc)
