# write a program to detect double spaces in a string

story = "hello  world, there  are some  python programs to clear the basics. welcome to python."

print("Double Spaces : ", story.find("  "))

# replace double spaces with single spaces
print("New Story : ", story.replace("  ", " "))
