import os
import xml.etree.ElementTree as ET

# Directory containing the XML files
directory = "Combined_Frames"

# List to store unique annotated object names
unique_object_names = set()

# Iterate over XML files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".xml"):
        # Parse the XML file
        xml_path = os.path.join(directory, filename)
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # Extract object names from the XML file
        for obj in root.findall("object"):
            name = obj.find("name").text
            unique_object_names.add(name)

# # Print the unique annotated object names
# for name in unique_object_names:
#     print(name)
output_file = "labels.txt"

# Open the file in write mode
with open(output_file, "w") as f:
    c = 1
    # Write the content for each label to the file
    for label in unique_object_names:
        content = f"item {{\n    id: {c}\n    name: '{label}'\n}}\n"
        c +=1
        f.write(content)


