import os

def write_tools(files, tools, proj_name):
    os.chdir("../../copyfiles")
    if "benchmark" in tools:
        tmpbench = open("benchmark.hpp", "r")
        files["benchmarkh"].write(tmpbench.read())
        os.remove("../" + proj_name + "/src/tools/benchmark.cpp")
    if "rng" in tools:
        tmprngh = open("rng.hpp", "r")
        files["rngh"].write(tmprngh.read())

        tmprngs = open("rng.cpp", "r")
        files["rngs"].write(tmprngs.read())
    os.chdir("..")