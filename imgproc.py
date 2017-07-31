from astropy import units as u
from astropy.io import fits
import numpy as np
import ccdproc as ccd


# General Reduction process:
#   1.) Avg Bias frames

#   2.) Subtract avg bias from flat
#       - Normalize each flat to 1.0

#   3.) Median/ avg flat for each filter
#       - Normalize avg flats to 1

#   4.) Subtract Bias from object images

#   5.) Divide image by flat field.

path  = '/Users/JPeg/umdastrodata/20170617/'


# Create list of bias frame filenames.

bias_set1 = [(path + 'lmi.00%d.fits'  %n) for n in    range(21,41)]

#for i in bias_set1:
    #print(i.shape)


bias_set2 = [(path + 'lmi.0%d.fits'   %n) for n in  range(327,337)]

#for j in bias_set2:
    #print(j.shape)

# Assert: bias frames must have equal dimentions.


# concatenate component lists.

all_bias = bias_set1 + bias_set2

# Create master-bias image by combining bias images and taking the mean. **ccdproc admits a list of fits files. output file must be .fits else error.

mbias_avg = ccd.combine(all_bias, output_file = path + 'jp_mbias_avg.fits', method = 'average')


# Create average flat for each filter:

flatlist_OH = [(path + 'lmi.00%d.fits' %n) for n in range(41,51)]

flat_set_NH = [(path + 'lmi.00%d.fits' %n) for n in range(51,62)]

flat_set_UC = [(path + 'lmi.00%d.fits' %n) for n in range(62,73)]

flat_set_CN = [(path + 'lmi.00%d.fits' %n) for n in range(73,84)]

flat_set_BC = [(path + 'lmi.00%d.fits' %n) for n in range(84,95)]

flat_set_RC = [(path + 'lmi.00%d.fits' %n) for n in range(95,100)] + [(path + 'lmi.0%d.fits' %n) for n in range(100,106)]

flat_set_C2 = [(path + 'lmi.0%d.fits' %n) for n in range(106,117)]

flat_set_SDSS_R = [(path + 'lmi.0%d.fits' %n) for n in range(117,129)]

flat_set_SDSS_G = [(path + 'lmi.0%d.fits' %n) for n in range(129,142)]
