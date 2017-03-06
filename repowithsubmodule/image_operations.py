'''
just some basic image operations
'''

import numpy as np
import skimage as sk
import scipy.ndimage  as nd

class LinearOperations(object):
    def __init__(self, fname):
        '''
        an image object. Loads in some image from jpg and converts it to useful
        '''
        self.image = nd.imread(fname,flatten=True)
    
    def fft2(self):
        '''
        takes the two dimensional fourier transfrom of the object
        '''
        tmp = self.image
        self.image = np.fft.fft2(np.fft.fftshift(tmp))

    def median(self, kernel):
        '''
        takes as median filter of an image
        '''
        tmp = self.image
        self.image = nd.median(tmp, size=kernel)
        
    def gaussian(self, sigma):
        '''
        applies a gaussian filter
        '''
        tmp = self.image
        self.image = nd.gaussian_filter(tmp, sigma)
        
    def sobel(self):
        '''
        applies a sobel filter to the image
        '''
        tmp=self.image
        self.image = nd.sobel(tmp)
        
    def affine_transform(self, matrix=[5,5]):
        tmp = self.image
        self.image = nd.affine_transform(tmp, np.array(matrix))
        
    def get_image(self):
        '''
        returns an image
        '''
        return self.image