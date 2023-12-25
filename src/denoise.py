# %%
from PIL import Image
import cv2 
import matplotlib.pyplot as plt
import numpy as np
import math

path = r"C:\Users\chang\source\repos\Denoising\data\410235141_367436305836058_3589902287613083535_n.jpg"
img = Image.open(path)
cv_img = cv2.imread(path)
cv2.imshow('image', cv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%

a = np.asarray(cv_img)
print(a.shape)

def get_rect(img, x, x2, y, y2):
    return img[x:x2, y:y2, :]

rows, cols, depth = a.shape
img = (get_rect(a, rows//4, rows//2, cols//4, cols//2))
cv2.imshow('roi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
from PIL import Image
import cv2 
import matplotlib.pyplot as plt
import numpy as np
import math

class ImageConvolutionRGB:
    def __init__(self, img):
        # Load the image
        self.image = img
        
        # Convert the image to a numpy array
        self.image_array = np.array(self.image)
        
        # Get the dimensions of the image
        self.image_height, self.image_width, self.image_cols = self.image_array.shape


    def convolve(self, kernel):
        """
        Reference:
        (f*g)(t):=\int _{-\infty }^{\infty }f(\tau )g(t-\tau )\,d\tau 
        """
        kernel_height, kernel_width = kernel.shape
        convolved_img = np.zeros([self.image_height - kernel_height + 1, self.image_width - kernel_width + 1, self.image_cols])
        for k in range(0, self.image_cols):
            for i in range(0, convolved_img.shape[0]):
                for j in range(0, convolved_img.shape[1]):
                    convolved_img[i, j, k] = np.sum(np.multiply(self.image_array[i:i+kernel_height, j:j+kernel_width, k], kernel))
        # sum_convolved_img = np.sum(convolved_img)
        normalized_convolved_img = (normalize(convolved_img)* 255).astype(np.uint8)

        # normalized_convolved_img = normalized_convolved_img.astype(np.uint8)
        print(normalized_convolved_img)
        return normalized_convolved_img
        # return convolved_img
        
    def get_roi(self, x, y, l1, l2):
        return self.image_array[x:(x+l1), y:(y+l2), :]


def normalize(x):
    min_x = np.min(x)
    max_x = np.max(x)
    y = (x - min_x) / (max_x - min_x)
    return y

def gaussian_kernel(size, sigma):
    """
    Reference:
    G(x, y) = (1 / (2 * pi * sigma^2)) * exp(-(x^2 + y^2) / (2 * sigma^2))
    """
    
    center = (size - 1)/2
    kernel = np.zeros((size, size))
    
    for i in range(size):
        for j in range(size):
            x = i - center
            y = j - center
            kernel[i, j] = (1 / (2 * math.pi * sigma**2)) * math.exp(-(x**2 + y**2) / (2 * sigma**2))
                # Normalize the kernel so that its values sum to 1
    kernel = kernel / np.sum(kernel)
    return kernel

def std(img):
    # std = sqrt(mean(a-a.mean)^2)
    return np.std(img)
    
path = r"C:\Users\chang\source\repos\Denoising\cat.png"
img = cv2.imread(path)
Img = ImageConvolutionRGB(img)
Img_ROI = ImageConvolutionRGB(Img.get_roi(128, 128, 256, 256))
identity =  np.identity(21)
new_img = Img_ROI.convolve(kernel=identity)

print(std(Img.image_array), std(Img_ROI.image_array))

cv2.imshow('image', Img_ROI.image_array)
# cv2.imshow('roi', img.image_array)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%

