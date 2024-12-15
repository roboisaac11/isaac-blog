---
title: My Obsidian Setup
date: 2024-12-14
draft: false
tags:
  - "#Obsidian"
---
# Introduction
---
Hello random people on the internet that I do not know!
![Image Description](/isaac-blog/images/Pasted-image-20241215140327.png)
Today I will be talking about my current obsidian setup. Just to show you what it all looks like, here's a screenshot:
![Image Description](/isaac-blog/images/Pasted-image-20241215141856.png)
Yeeeeep, so I'm gonna be showing you how I made that.

# Plugins & Themes
---
Here is a list of plugins and the theme I used:
- [ExcaliDraw](https://github.com/zsviczian/obsidian-excalidraw-plugin)
- [Templater](https://github.com/SilentVoid13/Templater)
- [Iconize](https://github.com/FlorianWoelki/obsidian-iconize)
- [Calendar](https://github.com/liamcain/obsidian-calendar-plugin)
- [Style Settings](https://github.com/mgmeyers/obsidian-style-settings)
* [Vauxhall](https://github.com/CyanVoxel/vauxhall-obsidian)
> *You only need Style Settings for changing the look of the theme*

## Configuration
### Style Settings
In Style Settings I only changed the `Color Intensity` to `Nebula` for more of a contrast.

### Colored Sidebar
To get the colorful folders, I used a CSS snippet [Colored Sidebar](https://github.com/CyanVoxel/Obsidian-Colored-Sidebar). To apply it,
- Download the CSS file
- Go to `Options` > `Appearance` > `CSS snippets` and open the file location
- Copy the CSS file into that folder (should be `.obsidian/snippets`)
- Back in Obsidian click on `reload snippets`.

Now it should apply colors to your folders. You have to name your folders starting with `00` to `07`, and `99` also works. 
![Image Description](/isaac-blog/images/Pasted-image-20241215143657.png)
You can change all the colors and these rules in the CSS file you copied over.

### Iconize
To add the nice little icons to folders, I used the Iconize plugin. After enabling it I didn't change any configurations, but you can if you want. Now you can just right-click a folder and press `Change Icon` and select one you want!

### Calendar
This is just a nice little widget that displays a calendar. You can also click on a day to open a daily note for that day. After enabling, it shows up in the right sidebar, but I dragged it over to be under my folders.

### ExcaliDraw
I use ExcaliDraw to create little drawings and quickly sketch out random stuff. That image at the beginning of the article was created with it. Because I have Obsidian in dark mode, it looks better to have it also in dark mode. Go to `Options` > `ExcaliDraw` > `Appearance and Behaviour` > `Theme and Styling`, and enable `New drawings to match Obsidian theme`.

### Templater
I keep a folder with templates for different types of notes I want to make. More on that later. Templater makes it easy to create a note from a template, and have it be created in a specific folder. After enabling, go to it's options and specify the template folder. Now when you click on the icon on the left sidebar, you can select a template.

To make certain temples create notes in different folders, you have to turn on `Enable folder templates`. You can add a folder, and the type of template. Here's an example:
![Image Description](/isaac-blog/images/Pasted-image-20241215144459.png)
Now when I create an blog post it automatically goes into my blog folder.

## Templates
### Daily Notes
I have it so that when I create a new daily note, it used my Daily Note template and puts it in my Daily folder. This is pretty easy to setup.

* Navigate to `Options` > `Daily notes`. Here you can select what folder they go it, and what template they use.

# Outro
---
So that's about everything. Cya.