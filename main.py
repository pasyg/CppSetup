import os

from test import write_test
from structure import structure
from classw import write_classes
from cmake import cmake
from tools import write_tools

# name of project
proj_name = "Template"
# ["array", "iostream", "vector"] e.g.
std_include = ["array", "iostream", "vector"]
# ["Asio", "Beast", "Regex"] e.g.
boost_include = ["Asio", "JSON"]
# class name, capitalized e.g. ["MyClass"]
classes = ["Dummy", "Dummy2", "DummyClass"]
# benchmark | rng
tools = ["benchmark", "rng"]

files = {

}

def main():
    structure(proj_name, tools, classes, files)
    if "benchmark" in tools:
        benchmark = True
    else:
        benchmark = False
    write_test(files, benchmark)
    write_classes(files, classes)
    cmake(proj_name, tools, classes, files)
    write_tools(files, tools, proj_name)
    
if __name__ == '__main__':
    main()