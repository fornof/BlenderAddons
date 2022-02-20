''' Created by Robert Fornof'''

import bpy 
def frame_changer(scene):
    text = bpy.utils.smpte_from_frame(scene.frame_current)
    text_obj = bpy.data.objects['Text']
    text_obj.data.body = text[3:]
	
#bpy.app.handlers.frame_change_post.remove(frame_changer)
bpy.app.handlers.frame_change_post.append(frame_changer)

#google: bpy.app.handlers.frame_change_post.append