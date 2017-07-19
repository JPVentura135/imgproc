from astropy import units as u
from astropy.io import fits
import numpy as np
import ccdproc as ccd


## General Reduction process:
#   1.) Avg Bias frames
#   do I just read each fits file and and
#   2.) Subtract avg bias from flat
#       - Normalize each flat to 1.0
#   3.) Median/ avg flat for each filter
#       - Normalize avg flats to 1
#   4.) Suntract Bias from object images
#   5.) Divide image by flat field.

path = '/Users/JPeg/umdastrodata/20170617/'
count = 0


# create bias frame from files of correct dimensions (not subframe) in path:

bias_set1 = [fits.getdata(path + 'lmi.00%d.fits'  %n) for n in    range(10,41)]

for i in bias_set1:
    print(i.shape)

bias_set2 = [fits.getdata(path + 'lmi.0%d.fits'   %n) for n in  range(327,337)]

for j in bias_set2:
    print(j.shape)

# add all bias images to be able to take the mean and obtain the master bias.
all_bias = np.mean(bias_set1 + bias_set2)

img_sum = 0
average = 0

for img in all_bias:
    img_sum = img_sum + img
    average = img_sum/len(all_bias)

print(all_bias.shape) # assert: should be (3128,3080)
    
# Image of C/2015 OI PanSTARRS pos3
#image = ccd.CCDData.read('/Users/JPeg/code_abode/ipynb/lmi.0200.fits')

# Several functions exist within ccdproc.CCDData to perform general reduction
# pipeline procedures
