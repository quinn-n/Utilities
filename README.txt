make -- local-install will add soft links to your local bin. (~/.local/bin/).
make -- install will add soft links to /bin
make -- uninstall will remove soft links in /bin and in ~/.local/bin.

len.py <string> prints the length of the string <string>.
replace.py <file> <toBeReplaced> <toReplaceWith> <number> replaces every instance of toBeReplaced with toReplaceWith in the file file number times. -- probably the most useful tool I've made to date.
mass-append.py <file> <number> <string> appends string to file number times.
choose.py <choices> randomly choses one of the choices.
repeat.py <string> <number> prints string number times.
counter.py <delay> prints the number of times per second a delay will occur - ex. .05 will return 20, .1 will return 10.
getInstances.py <file> <searches> finds the number of instances of your searches in file.
loop.py <songs> Since mpg123 doesn't have any form of looping function, I decided to write my own. Plays songs over and over again, until you tell it to stop.
shuffle.py <songs> randomly selects a song and plays it.
railroad.py runs sl over and over again.
convertImage.py <input image> <output image> converts an input image to an output image - ex. ./convertImage.py image.jpg image.png
showImage.py <image> prints the greyscale value of an image, to form an image on the terminal.
cpStatus.py <source> <destination> copies a file from the souce to the destination, much like cp. Except it also constantly prints the status. Useful for long file copies.
numWords.py <string> prints the number of words in a string
runInBackground.py <command> -- runs a command in the background.
type.py <string> <[delay (default 1)]> -- waits delay and then types string on your keyboard.
camel_to_underscore.py <file> -- converts the variables and functions from camelCase to underscore_spacing.
search_files.py <path-to-dir> <search> -- recursively searches the contents of every file in the directory and prints out all the matching filepaths.
get-pixel-value.py <delay> -- Get the pixel values and cursor position after delay seconds.
repeatkeys.py <string> <times> <[delay]> -- types string a given number of times after an optional delay. If no delay is given, it defaults to 1 sec.
remove-youtubedl-chars <file(s) / dir(s)> -- Renames youtube-dl files to remove the extra chars. Eg. video-abcdefghijkl.webm -> video.webm
convert-video.py -- Converts video files to audio files. Useful for converting audio taken from youtube.
rename-jpg-large.py -- Renames .jpg_large files to .jpg files
nfiles.py <[dir]> -- Prints the number of files in a given directory. If no directory is provided, prints the number of files in the local directory instead.

Requirements:
convertImage.py & showImage.py - PIL/Pillow
railroad.py - sl
