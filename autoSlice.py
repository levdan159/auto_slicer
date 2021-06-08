import glob, os, time

# Print settings file
printer_def = "./printer_def/creality_cr10.def.json "

#os.chdir("./stl_unsliced")
while True:
    for file in glob.glob("./stl_unsliced/*.stl"):

        print("slicing now: " + file)
        stl_filename = os.path.basename(file)
        output_file = ("./gcode/" + stl_filename + ".gcode")

        # Slice the goddamn file!     
        os.system("CuraEngine slice -v -j " + printer_def + " -l " + file + " -o " + output_file  )
        # Move sliced STL file to safe directory
        os.system("mv " + file + " ./stl_sliced")

    print("Nothing to slice! waiting")
    time.sleep(10) 




#CuraEngine slice -v -j ./printer_def/creality_cr10.def.json -l ./stl_unsliced/vlamp.stl -o ./gcode/vlap.gcode
