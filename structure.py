import os

def structure(proj_name, tools, classes, files):
    
    if not os.path.isdir(proj_name):
        os.makedirs(proj_name)
        os.chdir(proj_name)
    if not os.path.isdir("src"):
        os.makedirs("src")
    if not os.path.isdir("test"):
        os.makedirs("test")

    files["readme"] = open("README.md", "a")

    files["cmake"] = open("CMakeLists.txt", "a")

    os.chdir("test")
    files["testh"] = open("test.hpp", "a")
    files["tests"] = open("test.cpp", "a")
    os.chdir("..")
    os.chdir("src")

    files["main"] = open("main.cpp", "a")
    files["constants"] = open("constants.hpp", "a")

    if tools:
        if not os.path.exists("tools"):
            os.makedirs("tools")
        os.chdir("tools")
        
        for tool in tools:
            files[tool + "s"] = open(tool + ".cpp", "a")
            files[tool + "h"] = open(tool + ".hpp", "a")
        os.chdir("..")

    for class_ in classes:
        if not os.path.exists(class_.lower()):
            os.makedirs(class_.lower())
        os.chdir(class_.lower())
        files[class_ + "s"] = open(class_.lower() + ".cpp", "a")
        files[class_ + "h"] = open(class_.lower() + ".hpp", "a")
        os.chdir("..")