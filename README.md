HEAD
# SeniorThesis
Files for My Senior Thesis; repository base is from ARC373 class (SEE BELOW).

# ARC373_Fall2025
This repository contains the files for the course ARC373 Creative Computation and Robotics 
<<<<<<< HEAD
66e21aa (Initial commit)
=======

## Requirements

* Minimum OS: Windows 10 Pro or Mac OS Sierra 10.12
* [Anaconda 3](https://www.anaconda.com/distribution/) Anaconda is an open source scientific Python distribution. With this tool, we can easily create a Python environment. Install Anaconda using default options.
* [Docker Desktop](https://www.docker.com/products/docker-desktop) Docker is a virtualization platform. We use it to run Linux containers for ROS on Windows machines. 
* After installation, it is required to enable "Virtualization" on the BIOS of the computer. Usually this requires rebooting your computer and pressing a vendor-specific key (`F2`, `F4`, `Del` are typical options) to enter the BIOS.

* [Rhino 7 & Grasshopper](https://www.rhino3d.com/download)
* [Visual Studio Code](https://code.visualstudio.com/): Any Python editor works, but we recommend using VS Code along with the recommended extensions listed in the [Working in Visual Studio Code](#working-in-visual-studio-code) section below.


> [!NOTE]  
> On Windows, you may need to install [Microsoft Visual C++ 14.0](https://www.scivision.dev/python-windows-visual-c-14-required/).


## Installation

We use `conda` to make sure we have clean, isolated environment for dependencies.

<details><summary>First time using <code>conda</code>?</summary>
<p>

Make sure you run this at least once:

    conda config --add channels conda-forge

</p>
</details>

    conda env create -f https://dfab.link/fs2023.yml

### Add to Rhino

   conda activate arc373
   python -m compas_rhino.install -v 7.0 

<!-- ### Get the workshop files

    <!-- (fs2023) cd Documents
    (fs2023) git clone https://github.com/compas-teaching/COMPAS-II-FS2023 --> -->

### Verify installation

python -m compas

Yay! COMPAS is installed correctly!

COMPAS: 2.13.0
Python: 3.13.5 (CPython)
Extensions: ['compas', 'compas-robots', 'compas-fab']

### Update installation


(arc373) conda env update -f https://dfab.link/fs2023.yml 


---

## Getting the ROS-UR-Planner Docker Image

Download the Docker image:

- Go to the [gramaziokohler/ros-ur-planner Docker Hub page](https://hub.docker.com/r/gramaziokohler/ros-ur-planner).
- Click the **Run in Docker Desktop** button to open the image in Docker Desktop.
- Follow the prompts in Docker Desktop to pull and start the container.


## Working in Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is a free and open source text editor with very good support for Python programming.

We recommend installing the following VS Code extensions:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)  
  *Official extension to add support for Python programming, including debugging, auto-complete, formatting, etc.*

- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)  
  *Add support for `Dockerfile` and `docker-compose.yml` files to VS Code.*

- [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)  
  *Add support for `.editorconfig` files to VS Code.*


To install the above extensions, open the `Extensions` view by clicking on the corresponding icon in the Activity Bar on the left side of VS Code and search the extension name in the search box. Once found, select it and click `Install`.

We recommend tweaking some of the default VS Code settings:

- Python Linter
Select `flake8` as your default python linter: open the `Command Palette` (`Ctrl+Shift+P`), type `Python: Select Linter`, select it and select `flake8` from the list.

- *[Windows Only]* Default Shell
Change the default shell from `PowerShell` to `Command Prompt`: open the `Command Palette` (`Ctrl+Shift+P`), type `Select Default Shell`, select it and from the options, select `Command Prompt`. Kill all opened terminals for it to take effect.

---

### Run scripts
To run Python scripts from within VS Code, simply open the file and press `F5`. This will start the script with the debugger attached, which means you can add breakpoints (clicking on the gutter, next to the line numbers), inspect variables and step into your code for debugging.

Alternatively, use `Ctrl+F5` to start the script without debugger.

---

### Virtual environments
If you are using conda to manage your virtual environments, VS Code has built-in support for them. When a `.py` file is open on VS Code, the bottom right side of the Status bar will show the Python interpreter used to run scripts. Click on it and a list of all available interpreters including all environments will be shown. Select one, and the next time you run a script, the newly selected interpreter will be used.

>>>>>>> f7d0291 (update readme)
