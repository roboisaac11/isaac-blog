# Update posts
robocopy "C:\Users\isaac\OneDrive\Documents\Obsidian Vault\isaac-blog" "C:\Users\isaac\OneDrive\Coding\isaacblog\content\posts" /mir

# Build
hugo

# Update images:
python images.py

echo "Running server"
hugo server -t terminal