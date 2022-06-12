import os

def cmake(proj_name, tools, classes, files):
    files["cmake"].write("cmake_minimum_required(VERSION 3.0.0)\n")
    files["cmake"].write("project " + proj_name + " VERSION 0.1.0\n\n")

    files["cmake"].write("set(CMAKE_CXX_STANDARD 20)\n\n")
    files["cmake"].write("if(NOT CMAKE_BUILD_TYPE)\n")
    files["cmake"].write("\tset(CMAKE_BUILD_TYPE Debug)\n")
    files["cmake"].write("endif()\n\n")
    files["cmake"].write("#set(CMAKE_CXX_FLAGS \"-Wall -Wextra\"\n")
    files["cmake"].write("set(CMAKE_CXX_FLAGS_DEBUG \"-g\")\n")
    files["cmake"].write("set(CMAKE_CXX_FLAGS_RELEASE \"-O4\")\n\n")
    files["cmake"].write("set_property(GLOBAL PROPERTY USE_FOLDERS ON)\n\n")
    files["cmake"].write("INCLUDE_DIRECTORIES(")
    files["cmake"].write("\t${PROJECT_SOURCE_DIR}\n")

    for class_ in classes:
        files["cmake"].write("\t${PROJECT_SOURCE_DIR}/src/" + class_.lower() + "\n")

    files["cmake"].write("\t${PROJECT_SOURCE_DIR}/src/tools\n\n")
    files["cmake"].write("\t${PROJECT_SOURCE_DIR}/src/test\n\n")
    files["cmake"].write(")\n\n")

    files["cmake"].write("set(EXECUTABLE_OUTPUT_PATH ../)\n\n")

    files["cmake"].write("set(" + proj_name + "_SOURCES\n")

    for class_ in classes:
        files["cmake"].write("\t\"src/" + class_.lower() + "/" + class_.lower() + ".cpp\"\n\n")

    for tool in tools:
        files["cmake"].write("\t\"src/tools/" + tool.lower() + ".cpp\"\n")

    files["cmake"].write(")\n\n")

    files["cmake"].write("add_executable(" + proj_name + " ${" + proj_name + "_SOURCES})")