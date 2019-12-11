# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "export_cam",
    "author" : "Samuel Delepoulle",
    "description" : "Export Camera position",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "File > Export > Camera position",
    "warning" : "",
    "category" : "Import-Export",
    "wiki_url" : ""
}

import bpy

from . cam_op import CameraExporter



def menu_export(self, context):
    import os    
    
    default_path = os.path.splitext(bpy.data.filepath)[0]     
    self.layout.operator(CameraExporter.bl_idname, text="Camera position (.txt)").filepath = default_path
    


def register():
    print("register")
    bpy.utils.register_class(CameraExporter)
    bpy.types.TOPBAR_MT_file_export.append(menu_export)


def unregister():
    bpy.utils.unregister_class(CameraExporter)
    bpy.types.TOPBAR_MT_file_export.remove(menu_export)
