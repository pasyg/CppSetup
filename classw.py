import os

def write_classes(files, classes):
    for class_ in (classes):
        # class header
        files[class_ + "h"].write("#pragma once\n\n")
        files[class_ + "h"].write("class " + class_ + "{\n")
        files[class_ + "h"].write("public:\n")
        files[class_ + "h"].write("\t" + class_ + "();\n")
        files[class_ + "h"].write("\t~" + class_ + "();\n\n")
        files[class_ + "h"].write("private:\n")
        files[class_ + "h"].write("};")
        
        #class source
        files[class_ + "s"].write("#include \"" + class_.lower() + ".hpp\"\n\n")      
        files[class_ + "s"].write(class_ + "::" + class_ + "(){\n\n")
        files[class_ + "s"].write("}\n\n")     
        files[class_ + "s"].write(class_ + "::~" + class_ + "(){\n\n")
        files[class_ + "s"].write("}")