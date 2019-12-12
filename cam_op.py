import bpy
from bpy_extras.io_utils import ExportHelper
from mathutils import Vector

def write_cameras(context, filepath) :

    fw = open(filepath, 'w').write

    # write position
    obj_camera = bpy.context.scene.camera   
    fw(str(obj_camera.location[0])+" "+str(obj_camera.location[1])+" "+str(obj_camera.location[2])+"\n")

    # write look-at
    cam_direction = obj_camera.matrix_world.to_quaternion() @ Vector((0.0, 0.0, -1.0))
    lookat = obj_camera.location+cam_direction
    fw(str(lookat[0])+" "+str(lookat[1])+" "+str(lookat[2])+" ")





class CameraExporter(bpy.types.Operator, ExportHelper):

    """Save the camera postion"""
    bl_idname = "object.exportcam"
    bl_label = "Export Camera Position"

    filename_ext = ".txt"


    def execute(self, context):
        write_cameras(context, self.filepath)
        return {'FINISHED'}