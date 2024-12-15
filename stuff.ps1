$base_url = "/isaac-blog/"

# Update posts
robocopy "C:\Users\isaac\OneDrive\Documents\Obsidian Vault\00 - Isaac Blog" "C:\Users\isaac\OneDrive\Coding\isaacblog\content\posts" /mir

# Update images:
python images.py $base_url

# Build
hugo -b $base_url

# push to github
git add .
git commit -m "update posts"
git push origin master
git subtree split --prefix public -b release
git push origin release --force