import io
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import json

def handle_uploaded_file(image_data):
    """
    Read the request file and send the fetched data from the pytesseract
    """
    try:
        receipt_image = Image.open(io.BytesIO(image_data.read()))
        image_data = pytesseract.image_to_data(receipt_image, output_type=pytesseract.Output.DICT)
        return image_data.get("text")
    except Exception as ex:
        return None
    
