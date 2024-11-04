from PIL import Image as PILImage
import os
import tkinter.messagebox

def show_message(message, title="Debug"):
    tkinter.messagebox.showinfo(title,  message)

def create_cropped_versions(image_path, pixelsPerCut = 10):
    try:
        original_image = PILImage.open(image_path)
        width, height = original_image.size
    except Exception as e:
        show_message(f"Error opening image: {e}", "Error")
        return

    # Load the original image
    minWidth = max(640, width - width // 10)
    minHeight = max(320, height - height // 10)

    # Extract the original photo's name without the extension
    photo_name = os.path.splitext(os.path.basename(image_path))[0]

    # Determine the output folder path
    output_dir = os.path.join(os.path.dirname(image_path), f'cropped_{photo_name}')
    os.makedirs(output_dir, exist_ok=True)

    amountOfPossibleWidths = width - minWidth + 1
    amountOfPossibleHeights = height - minHeight + 1
    for w in range(amountOfPossibleWidths // pixelsPerCut):
        newWidth = width - (w * pixelsPerCut)
        for h in range(amountOfPossibleHeights // pixelsPerCut):
            newHeight = height - (h * pixelsPerCut)

            if newHeight < minHeight or newWidth < minWidth:
                break

            left = (width - newWidth) // 2
            right = left + newWidth
            top = (height - newHeight) // 2
            bottom = top + newHeight

            # Crop and save the image if the region is valid
            if right > left and bottom > top:
                cropped_image = original_image.crop((left, top, right, bottom))
                output_filename = os.path.join(output_dir, f'cropped_{photo_name}_{w * pixelsPerCut}_{h * pixelsPerCut}.jpg')
                try:
                    cropped_image.save(output_filename)
                except Exception as e:
                    show_message(f"Error saving image: {e}", "Error")