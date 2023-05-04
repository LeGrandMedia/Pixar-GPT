import os
import os.path
import sys
import bpy
import subprocess
import tempfile


# Set a dedicated folder for file I/O
working_directory = "auto_gpt_workspace"
# Create the directory if it doesn't exist
if not os.path.exists(working_directory):
    os.makedirs(working_directory)

is_blender_open = False

def safe_join(base, *paths):
    """Join one or more path components intelligently."""
    new_path = os.path.join(base, *paths)
    norm_new_path = os.path.normpath(new_path)

    if os.path.commonprefix([base, norm_new_path]) != base:
        raise ValueError("Attempted to access outside of working directory.")

    return norm_new_path



def open_blender():
    global is_blender_open  # Add this line to access the global variable
    if not is_blender_open:
        blender_executable = "C:/Users/smile/Auto-GPT/auto_gpt_workspace/AI_tools/Blender Foundation/Blender 3.5/blender.exe" # Update this with the correct path to the Blender executable
        blender_script = os.path.join(os.path.dirname(__file__), "open_blender_delete_cube.py")
        
        with open(blender_script, "w") as script_file:
            script_file.write("import bpy\n")
            script_file.write("bpy.ops.object.select_all(action='DESELECT')\n")
            script_file.write("bpy.ops.object.select_by_type(type='MESH')\n")
            script_file.write("bpy.ops.object.delete()\n")
        
        try:
            subprocess.Popen([blender_executable, "-P", blender_script])
            is_blender_open = True
            return "Blender opened"
        except Exception as e:
            return "Error: " + str(e)
    else:
        return "Blender is already open"





def write_blender_script(script):
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.py') as temp:
#temp.write("import sys\n")
        #temp.write("print('Executing Blender script...', {script})\n")
        temp.write(script)
        temp.flush()
        temp_name = temp.name
        temp.close()

    blender_executable = "C:/Users/smile/Auto-GPT/auto_gpt_workspace/AI_tools/Blender Foundation/Blender 3.5/blender.exe"  # Replace with the full path to your Blender executable

    try:
        proc = subprocess.Popen([blender_executable, "-b", "--python", temp_name], stderr=subprocess.PIPE)

        while proc.poll() is None:
            output_line = proc.stderr.readline().decode('utf-8')
            if output_line:
                print(output_line.strip())

        return f"Blender script executed successfully./nscript = {script}" 
    except Exception as e:
        return f"Error: {e} /nscript = {script}"
    #finally:
        #os.remove(temp_name)





def close_blender(filepath):
    global is_blender_open
    subprocess.run(["blender", "--background", "--python-expr", "bpy.ops.wm.quit_blender()"])
    is_blender_open = False
    return "blender is now closed"
