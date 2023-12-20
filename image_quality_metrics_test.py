# %%
import cv2
import numpy as np

def calculate_snr(image_path: str) -> None:
    """
    Calculate Signal-to-Noise Ratio (SNR) for an image.

    Parameters:
        image_path (str): The file path of the image.

    Returns:
        None: Prints the calculated SNR.
    """
    image = cv2.imread(image_path)
    mean_pixel_value = np.mean(image)
    std_dev_pixel_value = np.std(image)
    snr = 20 * np.log10(mean_pixel_value / std_dev_pixel_value)
    print(f"SNR: {snr}")

def calculate_psnr(original_image_path: str, reconstructed_image_path: str) -> None:
    """
    Calculate Peak Signal-to-Noise Ratio (PSNR) between two images.

    Parameters:
        original_image_path (str): File path of the original image.
        reconstructed_image_path (str): File path of the reconstructed image.

    Returns:
        None: Prints the calculated PSNR.
    """
    original_image = cv2.imread(original_image_path)
    reconstructed_image = cv2.imread(reconstructed_image_path)
    mse = np.mean((original_image - reconstructed_image) ** 2)
    max_pixel_value = np.max(original_image)
    psnr = 10 * np.log10((max_pixel_value ** 2) / mse)
    print(f"PSNR: {psnr}")

def calculate_sharpness(image_path: str) -> None:
    """
    Calculate image sharpness using Laplacian operator.

    Parameters:
        image_path (str): The file path of the image.

    Returns:
        None: Prints the calculated sharpness.
    """
    image = cv2.imread(image_path)
    sharpness = cv2.Laplacian(image, cv2.CV_64F).var()
    print(f"Sharpness: {sharpness}")

def calculate_contrast(image_path: str) -> None:
    """
    Calculate image contrast.

    Parameters:
        image_path (str): The file path of the image.

    Returns:
        None: Prints the calculated contrast.
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    contrast = np.std(image)
    print(f"Contrast: {contrast}")

# %%
# Example usage
path = r"C:\Users\chang\Downloads\drive-download-20231128T022421Z-001\Experiment B - On Off Test"
image_auto = path + r"\NightModeAuto_ISO2500_24mm_f1d78_s1over9.jpeg"
image_off = path + r"\NightModeOff_ISO4000_24mm_f1d78_s1over15.jpeg"
image_on = path + r"\NightModeOn_ISO2000_24mm_f1d78_s1over7.jpeg"

calculate_psnr(image_off, image_on)
calculate_snr(image_on)
calculate_sharpness(image_on)
calculate_contrast(image_on)
# %%
