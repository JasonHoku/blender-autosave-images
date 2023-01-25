

import os
import traceback
import bpy
from bpy.app.handlers import persistent

bl_info = {
    "name": "UnpackAndSave",
    "author": "Jason Hoku",
    "blender": (3, 4, 0),
    "version": (1, 0, 2),
    "category": "System"
}


# async def main():
#     with open(os.path.splitext(bpy.data.filepath)[0] + ".txt", 'w') as fs:
#         for img in bpy.data.images:
#             try:
#                 print(img)
#                 print(img.size)
#                 print(img.filepath)
#                 img.save()
#             except:
#                 traceback.print_exc()
#     print('\nSaved All Images To ./textures/')


# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# try:
#     loop.run_until_complete(main())
# finally:
#     loop.run_until_complete(loop.shutdown_asyncgens())
#     loop.close()

@persistent
def save_external_images(a, b):
    with open(os.path.splitext(bpy.data.filepath)[0] + ".txt", 'w') as fs:
        for img in bpy.data.images:
            try:
                if 'textures' in img.filepath:
                    break
                else:
                    print(img)
                    print(img.size)
                    print(img.filepath)
                    print(img.name)
                    # img.save_all_images()
                    # img.name = img.id
                    textures_path = bpy.path.abspath("//textures/")
                    img_path = str(textures_path + str(img.name) + ".png")
                    img.filepath_raw = img_path
                    img.file_format = 'PNG'
                    fs.write(img_path)
                    img.save_render(filepath=img_path)
                    img.save(filepath=img_path)
            except:
                traceback.print_exc()
        bpy.ops.image.save_all_modified()
        print('\nSaved All Images To ./textures/')



@persistent
def register():
    bpy.app.handlers.save_pre.append(save_external_images)


def unregister():
    bpy.app.handlers.save_pre.remove(save_external_images)


if __name__ == "__main__":
    register()
