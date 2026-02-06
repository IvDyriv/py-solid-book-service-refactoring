import json
import xml.etree.ElementTree as ET


def serialize_json(title: str, content: str) -> str:
    return json.dumps({"title": title, "content": content})


def serialize_xml(title: str, content: str) -> str:
    root = ET.Element("book")
    title_el = ET.SubElement(root, "title")
    title_el.text = title
    content_el = ET.SubElement(root, "content")
    content_el.text = content
    return ET.tostring(root, encoding="unicode")
