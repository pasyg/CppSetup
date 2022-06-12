import os

def write_test(files, benchmark):
    # test header
    files["testh"].write("#pragma once\n\n")
    files["testh"].write("#include <array>\n#include <fstream>\n#include <string>\n#include <string_view>\n#include <vector>\n\n")
    files["testh"].write("#include \"tools/benchmark.hpp\"\n")
    files["testh"].write("\n")
    files["testh"].write("class Test{\npublic:\n\tTest();\n\t~Test();\n\tvoid test_all();\n\n")
    files["testh"].write("\ttemplate<typename Func>\n")
    files["testh"].write("\tvoid check(std::string_view funcname, Func func){\n")
    files["testh"].write("\t\tif(func()){\n")
    files["testh"].write("\t\t\tstd::cout << funcname << \"test successful\\n\\n\";\n")
    files["testh"].write("\t\t}\n")
    files["testh"].write("\t\telse{\n")
    files["testh"].write("\t\t\tstd::cout << funcname << \" test NOT successful\\n\\n\";\n")
    files["testh"].write("\t\t}\n\t}\n")
    files["testh"].write("private:\n")
    files["testh"].write("}")

    # test source
    files["tests"].write("#include \"test.h\"\n\n")
    files["tests"].write("Test::Test(){}\n\n")
    files["tests"].write("Test::Test(){}\n\n")
    files["tests"].write("void Test::test_all(){\n")
    if(benchmark):
        files["tests"].write("\tTimer timer;\n")
    files["tests"].write("\n}")