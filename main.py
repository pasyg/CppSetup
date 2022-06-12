import os

from test import write_test
from structure import structure
from classw import write_classes
from cmake import cmake

# name of project
proj_name = "Template"
# ["array", "iostream", "vector"] e.g.
std_include = ["array", "iostream", "vector"]
# ["Asio", "Beast", "Regex"] e.g.
boost_include = ["Asio", "JSON"]
# class name, capitalized e.g. ["MyClass"]
classes = ["Dummy", "Dummy2", "DummyClass"]
# benchmark | rng
tools = ["rng"]

files = {

}
    
if __name__ == '__main__':
    structure(proj_name, tools, classes, files)
    if "benchmark" in tools:
        benchmark = True
    else:
        benchmark = False
    write_test(files, benchmark)
    write_classes(files, classes)
    cmake(proj_name, tools, classes, files)