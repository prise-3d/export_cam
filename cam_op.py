import bpy
from bpy_extras.io_utils import ExportHelper


def write_cameras(context, filepath) :

    fw = open(filepath, 'w').write
    obj_camera = bpy.context.scene.camera
    fw(str(obj_camera.location[0])+" "+str(obj_camera.location[1])+" "+str(obj_camera.location[2])+" ")


class CameraExporter(bpy.types.Operator, ExportHelper):

    """Save the camera postion"""
    bl_idname = "object.exportcam"
    bl_label = "Export Camera Position"

    filename_ext = ".txt"


    def execute(self, context):
        write_cameras(context, self.filepath)
        return {'FINISHED'}