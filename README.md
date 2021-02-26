# Youtube2Gif

<--- ![Aesthetic Pixel Rain](rain.gif) --->

Youtube2Gif is a command line utility written in python that let's you easily downlaod and convert youtube videos into GIF animations.
Great if you want to create animated desktops backgrounds!

## Requirements

To use youtube to GIF you'll just need need to have both ffmpeg and youtube-dl installed. 
These can be found in the package repostiories of most major distrobutions.
```
# On Ubuntu or Debian 
sudo apt install ffmpeg youtube-dl -y
# On Arch
sudo pacman -S ffmpeg youtube-dl
```

## Usage

To use the program just run the following subsituting the video you want to convert for this charming video of [rap god geohot](https://www.youtube.com/watch?v=9iUvuaChDEg)

```
python ./yt2gif.py -t https://www.youtube.com/watch\?v\=9iUvuaChDEg -o geohot.gif
```

And then view your master piece in your image viewr of choice!

<--- ![Rap god geohot sued by sony](./geohot.gif) --->

## Contirubtions

I plan to add alot more fucntionality to this app (mostly relating to adding more commandline options for fomrating output size and duration etc) however if there's anything you want to add to the project don't hesitate to branch it!
