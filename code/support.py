import os
import pygame

def import_folder(path):
    surface_list = []
    
    # Standardize path format
    # path = os.path.normpath(path)  

    if not os.path.exists(path):
        print(f"Warning: The directory '{path}' does not exist.")
        return surface_list  # Return empty list if path doesn't exist

    for _, _, img_files in os.walk(path):
       for img in img_files:
           full_path = os.path.join(path, img)
           image_surf = pygame.image.load(full_path).convert_alpha()
           surface_list.append(image_surf)

    return surface_list
