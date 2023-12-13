import subprocess
import os

def run_latexmk(file_name):
    # Check if the file exists
    if os.path.isfile(file_name):
        # Command to run
        cmd = f"latexmk -pdf -lualatex {file_name}"
        
        # Execute the command
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print("Successfully compiled the LaTeX file.")
            print(stdout.decode("utf-8"))
        else:
            print("Error in compiling the LaTeX file.")
            print(stderr.decode("utf-8"))
    else:
        print("File does not exist.")

# Replace 'yourfile.tex' with the actual file name
file_name = 'final_latex_template.tex'
run_latexmk(file_name)
