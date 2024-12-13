# Update posts
robocopy "C:\Users\isaac\OneDrive\Documents\Obsidian Vault\isaac-blog" "C:\Users\isaac\OneDrive\Coding\isaacblog\content\posts" /mir

# Build
hugo -b "/isaac-blog/"

# Update images:
python images.py

# push to github
git add .
git commit -m "update posts"
git push origin master
git subtree split --prefix public -b release
git push origin release --force