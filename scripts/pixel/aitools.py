import os
import os.path

# Set a dedicated folder for file I/O
working_directory = "auto_gpt_workspace"

# Create the directory if it doesn't exist
if not os.path.exists(working_directory):
    os.makedirs(working_directory)


def safe_join(base, *paths):
    """Join one or more path components intelligently."""
    new_path = os.path.join(base, *paths)
    norm_new_path = os.path.normpath(new_path)

    if os.path.commonprefix([base, norm_new_path]) != base:
        raise ValueError("Attempted to access outside of working directory.")

    return norm_new_path


def open_blender():
    """Read a file and return the contents"""
    try:
        filepath = safe_join(working_directory, filename)
        with open(filepath, "r", encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        return "Error: " + str(e)




'''import bpy
import shutil

blender_bin = shutil.which("blender")
if blender_bin:
   print("Found:", blender_bin)
   bpy.app.binary_path = blender_bin
else:
   print("Unable to find blender!")'''