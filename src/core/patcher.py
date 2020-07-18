#!/usr/bin/env python3

from src.utils.config import Config

import r2pipe
import os 
from sys import exit

class Patcher:
    
    init_patch_dict = {
        "/.supersu":                                   "/.supersu",

        "/system/xbin/su":                              "/system/xbin/nu",
        "/system/xbin/daemonsu":                        "/system/xbin/daemonnu",
        "/system/xbin/sugote":                          "/system/xbin/nugote",
        "/system/xbin/sugote-mksh":                     "/system/xbin/nugote-mksh",
        "/system/xbin/supolicy":                        "/system/xbin/nupolicy",
        "/system/xbin/ku.sud":                          "/system/xbin/ku.nud",
        "/system/xbin/.ku":                             "/system/xbin/.nu",
        "/system/xbin/.su":                             "/system/xbin/.nu",
        "/system/lib/libsupol.so":                      "/system/lib/libnupol.so",
        "/system/lib64/libsupol.so":                    "/system/lib64/libnupol.so",
        "/system/bin/.ext/.su":                         "/system/bin/.ext/.nu",
        "/system/etc/init.d/99SuperSUDaemon":           "/system/etc/init.d/99SuperNUDaemon",
        "/system/etc/.installed_su_daemon":             "/system/etc/.installed_nu_daemon",

        "/system/app/Superuser.apk":                    "/system/app/Superuser.apk",
        "/system/app/Superuser.odex":                   "/system/app/Superuser.odex",
        "/system/app/Superuser":                        "/system/app/Superuser",
        "/system/app/SuperUser.apk":                    "/system/app/SuperUser.apk",
        "/system/app/SuperUser.odex":                   "/system/app/SuperUser.odex",
        "/system/app/SuperUser":                        "/system/app/SuperUser",
        "/system/app/superuser.apk":                    "/system/app/superuser.apk",
        "/system/app/superuser.odex":                   "/system/app/superuser.odex",
        "/system/app/superuser":                        "/system/app/superuser",
        "/system/app/Supersu.apk":                      "/system/app/Supersu.apk",
        "/system/app/Supersu.odex":                     "/system/app/Supersu.odex",
        "/system/app/Supersu":                          "/system/app/Supersu",
        "/system/app/SuperSU.apk":                      "/system/app/SuperSU.apk",
        "/system/app/SuperSU.odex":                     "/system/app/SuperSU.odex",
        "/system/app/SuperSU":                          "/system/app/SuperSU",
        "/system/app/supersu.apk":                      "/system/app/supersu.apk",
        "/system/app/supersu.odex":                     "/system/app/supersu.odex",
        "/system/app/supersu":                          "/system/app/supersu",
        "/system/app/VenomSuperUser.apk":               "/system/app/VenomSuperUser.apk",
        "/system/app/VenomSuperUser.odex":              "/system/app/VenomSuperUser.odex",
        "/system/app/VenomSuperUser":                   "/system/app/VenomSuperUser",

        "/sutmp":                                       "/nutmp",
        "SU=su":                                        "SU=nu",
        "SU=su.pie":                                    "SU=nu.pie",
        "APKNAME=/system/app/SuperSU/SuperSU.apk":      "APKNAME=/system/app/SuperSU/SuperSU.apk",

        "/system/bin/su":                               "/system/bin/nu",
        "/system/sbin/su":                              "/system/sbin/nu",
        "/vendor/sbin/su":                              "/vendor/sbin/nu",
        "/vendor/bin/su":                               "/vendor/bin/nu",
        "/vendor/xbin/su":                              "/vendor/xbin/nu",
        "/data/su.img":                                 "/data/nu.img",
        "/cache/su.img":                                "/cache/nu.img",

        "/su/bin":                                      "/nu/bin",
        "/su/xbin":                                     "/nu/xbin",
        "/su/lib":                                      "/nu/lib",
        "/su/etc":                                      "/nu/etc",
        "/su/su.d":                                     "/nu/nu.d",

        "/su/bin/app_process":                          "/nu/bin/app_process",
        "/su/bin/sush":                                 "/nu/bin/nush",
        "/su/bin/su":                                   "/nu/bin/nu",
        "/su/bin/su_*":                                 "/nu/bin/nu_*",


        "/su/xbin_bind":                                "/nu/xbin_bind",
        "${CPIO_PREFIX}su":                             "${CPIO_PREFIX}nu",
        "/suinit":                                      "/nuinit",
        "Superuser":                                    "Superuser",
        "superuser":                                    "superuser",
        "SuperUser":                                    "NuperUser",
        "sugote":                                       "nugote",
        "99SuperSUDaemon":                              "99SuperNUDaemon",

        # libsupol.so
        "libsupol":                                     "libnupol",

        #su
        "supersu":                                      "supernu",
        "Supersu":                                      "Supernu",
        "SuperSU":                                      "SuperNU",
        "daemonsu":                                     "daemonnu",
        "sudaemon":                                     "nudaemon",
    }

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