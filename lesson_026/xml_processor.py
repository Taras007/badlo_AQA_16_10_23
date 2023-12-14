from xml.etree import ElementTree as ET

class XMLProcessor:
    def __init__(self, xml_data):
        self.root = ET.fromstring(xml_data)

    def xml_to_string(self):
        return ET.tostring(self.root, encoding='unicode')

    def string_to_xml(self, xml_string):
        self.root = ET.fromstring(xml_string)

    def perform_operation(self, operation):
        return operation(self.root)

# Example XML data
xml_data = '''<collection>
    <genre category="Action">
        <!-- Your XML structure here -->
    </genre>
</collection>'''

processor = XMLProcessor(xml_data)
xml_string = processor.xml_to_string()
print(xml_string)  # Output: XML in string format

processor.string_to_xml(xml_string)
# Example of operation: print all titles
titles = processor.perform_operation(lambda root: [movie.get('title') for movie in root.findall('.//movie')])
print(titles)