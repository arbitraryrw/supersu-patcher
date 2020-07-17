#!/usr/bin/env python3

from src.utils.config import Config

import r2pipe
import os 
from sys import exit

class Patcher:
    
    init_patch_dict = {}

    clean_up_patch_dict = {
        "nupernu":"supernu",
        "nupersu":"supernu"
    }

    file_patch_dict={
        "/arm64/libsupol.so":                           "/arm64/libnupol.so",
        "/arm64/su":                                    "/arm64/nu",
        "/arm64/suinit":                                "/arm64/nuinit",
        "/arm64/sukernel":                              "/arm64/nukernel",
        "/arm64/supolicy":                              "/arm64/nupolicy",
        "/arm64/chromeos/futility":                     "/arm64/chromeos/futility",

        "/META-INF/MANIFEST.MF":                        "/META-INF/MANIFEST.MF",
        "/META-INF/CERT.SF":                            "/META-INF/CERT.SF",

        "/META-INF/com/google/android/update-binary":   "/META-INF/com/google/android/update-binary",

        "/common/000000deepsleep":                      "/common/000000deepsleep",
        "/common/file_contexts_image":                  "/common/file_contexts_image",
        "/common/install-recovery.sh":                  "/common/install-recovery.sh",
        "/common/Superuser.apk":                        "/common/Superuser.apk" ,
        "/common/init.supersu.rc":                      "/common/init.supernu.rc",
        "/common/frp_install":                          "/common/frp_install",
        "/common/launch_daemonsu.sh":                   "/common/launch_daemonnu.sh",
        "/common/init.supersu.rc.24":                   "/common/init.supernu.rc.24"
    }

    def __init__(self):
        pass

    def patch(self):
        for file in self.file_patch_dict.keys():
            file_abs_path = Config.unzip_dir_path + file

            print("[I] Patching File :: {}".format(file_abs_path))

            # Don't patch APK...
            if "/common/Superuser.apk" in file:
                continue

            if os.path.isfile(file_abs_path):
                r = r2pipe.open(file_abs_path, flags=['-w'])

                print("[i] Patching using init_patch_dict")
                self.apply_dict_patches(r, self.init_patch_dict)

                print("[i] Patching using clean_up_patch_dict")
                self.apply_dict_patches(r, self.clean_up_patch_dict)

                r.quit()

            else:
                exit(f"[ERROR] could not patch file {file_abs_path}")

        self.rename_libs()

    def apply_dict_patches(self, r2p, patch_dict):
        for key in patch_dict.keys():
            print ("Patching ::")
            print ("\tFrom -> {}".format(key))
            print ("\tTo -> {}".format(patch_dict[key]))
            r2p.cmd("w {} @@/ {}".format(patch_dict[key], key))
    
    def rename_libs(self):

        for old_name, new_name in self.file_patch_dict.items():
            old_name = Config.unzip_dir_path + old_name
            new_name = Config.unzip_dir_path + new_name

            if os.path.isfile(old_name):
                print('Renaming::')
                print('\t From -> {}'.format(old_name))
                print('\t To -> {}'.format(new_name))
                os.rename(old_name, new_name)
            else:
                print('[E] Cannot find original file {}'.format(old_name))