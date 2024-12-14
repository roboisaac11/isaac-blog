import os
import re
import shutil
import sys

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"C:\\Users\\isaac\\OneDrive\\Coding\\isaacblog\\content\\posts"
attachments_dir = r"C:\\Users\\isaac\\OneDrive\\Documents\\Obsidian Vault\\attachments"
static_images_dir = r"C:\\Users\\isaac\\OneDrive\\Coding\\isaacblog\static\\images"

root_directory = "/"

try:
    root_directory = sys.argv[1]
except IndexError:
    root_directory = "/"

# Root directory should end with a slash
if not root_directory.endswith("/"):
    root_directory += "/"
    
# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Step 2: Find all image links in the format ![Image Description](/images/Pasted%20image%20...%20.png)
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
        print(images)
        
        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image in images:
            # Prepare the Markdown-compatible link with %20 replacing spaces
            markdown_image = f"[Image Description]({root_directory}images/{image.replace(' ', '-')})"
            content = content.replace(f"[[{image}]]", markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                print(f"Copying {image} to {static_images_dir}")
                shutil.copy(image_source, static_images_dir)

                # Rename the file in the destination to use dashes instead of spaces
                image_dest = os.path.join(static_images_dir, image)
                new_image_name = image.replace(' ', '-')
                new_image_dest = os.path.join(static_images_dir, new_image_name)
                if os.path.exists(image_dest):
                    try:
                        os.rename(image_dest, new_image_dest)
                    except Exception:
                        print("Skipped because file already exists")


        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")