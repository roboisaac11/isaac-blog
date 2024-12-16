$base_url = "/isaac-blog/"

# Use | findstr "error" to only display errors

# Update posts
robocopy "C:\Users\isaac\OneDrive\Documents\Obsidian Vault\00 - Isaac Blog" "C:\Users\isaac\OneDrive\Coding\isaacblog\content\posts" /mir | findstr "error"

# Update images:
python images.py $base_url

# Build
hugo -b $base_url --quiet

# push to github
git add . | findstr "error"
git commit -m "update posts" | findstr "error"
git push origin master | findstr "error"
git subtree split --prefix public -b release | findstr "error"
git push origin release --force | findstr "error"

echo "Completed"