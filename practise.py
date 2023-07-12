# l = [f"Images\Video001-Scene-{i:03d}" for i in range(1,50)]

# print(l)
# import os

# current_dir =os.path.join(os.getcwd(),"Images")
# img_dir = os.listdir(current_dir)
# # Path to the source directories
# source_directories = img_dir[:48]
# print(source_directories)
# Define the labels as sets
labels = {
    "car",
    "bike"
}

# Path to the output file
output_file = "labels.txt"

# Open the file in write mode
with open(output_file, "w") as f:
    # Write the content for each label to the file
    for label in labels:
        content = f"item {{\n    name: '{label}'\n}}\n"
        f.write(content)
