import os
Import("env", "projenv")

# Relocate firmware from 0x08000000 to 0x08008000
for define in list (env['CPPDEFINES']):
    if define[0] == "VECT_TAB_ADDR":
        env['CPPDEFINES'].remove(define)
env['CPPDEFINES'].append(("VECT_TAB_ADDR", "0x08008000"))

custom_ld_script = os.path.abspath("buildroot/share/PlatformIO/ldscripts/WEEDOR72.ld")
for i, flag in enumerate(env["LINKFLAGS"]):
    if "-Wl,-T" in flag:
        env["LINKFLAGS"][i] = "-Wl,-T" + custom_ld_script
    elif flag == "-T":
        env["LINKFLAGS"][i + 1] = custom_ld_script


