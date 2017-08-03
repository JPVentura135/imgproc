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


bias_set2 = [(path + 'lmi.0%d.fits'   %n) for n in    range(327,337)]

#for j in bias_set2:
    #print(j.shape)

# Assert: bias frames must have equal dimentions.


# concatenate component lists.

all_bias = bias_set1 + bias_set2

# Create master-bias image by combining bias images and taking the mean. **ccdproc admits a list of fits files. output file must be .fits else error.

mbias_avg = ccd.combine(all_bias, output_file = path + 'jp_mbias_avg.fits', method = 'average')


### Subtract mbias from each flat ###

# Create lists of flats in order to iterate the mbias subtraction over them.

flatlist_OH = [(path + 'lmi.00%d.fits' %n) for n in range(41,51)]

flat_list_NH = [(path + 'lmi.00%d.fits' %n) for n in range(51,62)]

flatlist_UC = [(path + 'lmi.00%d.fits' %n) for n in range(62,73)]

flatlist_CN = [(path + 'lmi.00%d.fits' %n) for n in range(73,84)]

flatlist_BC = [(path + 'lmi.00%d.fits' %n) for n in range(84,95)]

flatlist_RC = [(path + 'lmi.00%d.fits' %n) for n in range(95,100)] + [(path + 'lmi.0%d.fits' %n) for n in range(100,106)]

flatlist_C2 = [(path + 'lmi.0%d.fits' %n) for n in range(106,117)]

flatlist_SDSS_R = [(path + 'lmi.0%d.fits' %n) for n in range(117,129)]

flatlist_SDSS_G = [(path + 'lmi.0%d.fits' %n) for n in range(129,142)]

# Subtract mbias from flat images in flat lists

for flat in flatlist_OH:
   ccd.subtract_bias(ccd.CCDData(fits.getdata(os.path.join(path,flat)),unit='adu'),ccd.CCDData(fits.getdata('jp_mbias_avg.fits'),unit='adu'), add_keyword='mbias subtracted flat_OH')

for flat in flatlist_NH:
    ccd.subtract_bias(ccd.CCDData(fits.getdata(os.path.join(path,flat)),unit='adu'),ccd.CCDData(fits.getdata('jp_mbias_avg.fits'),unit='adu'), add_keyword='mbias subtracted flat_NH')

for flat in flatlist_UC:
    ccd.subtract_bias(ccd.CCDData(fits.getdata(os.path.join(path,flat)),unit='adu'),ccd.CCDData(fits.getdata('jp_mbias_avg.fits'),unit='adu'), add_keyword='mbias subtracted flat_UC')

for flat in flatlist_CN:
    ccd.subtract_bias(ccd.CCDData(fits.getdata(os.path.join(path,flat)),unit='adu'),ccd.CCDData(fits.getdata('jp_mbias_avg.fits'),unit='adu'), add_keyword='mbias subtracted flat_CN')

for flat in flatlist_BC:
    ccd.subtract_bias(ccd.CCDData(fits.getdata(os.path.join(path,flat)),unit='adu'),ccd.CCDData(fits.getdata('jp_mbias_avg.fits'),unit='adu'), add_keyword='mbias subtracted flat_BC')

for flat in flatlist_RC:
    ccd.subtract_bias(ccd.CCDData(fits.getdata(os.path.join(path,flat)),unit='adu'),ccd.CCDData(fits.getdata('jp_mbias_avg.fits'),unit='adu'), add_keyword='mbias subtracted flat_RC')

for flat in flatlist_C2:
    ccd.subtract_bias(ccd.CCDData(fits.getdata(os.path.join(path,flat)),unit='adu'),ccd.CCDData(fits.getdata('jp_mbias_avg.fits'),unit='adu'), add_keyword='mbias subtracted flat_C2')

for flat in flatlist_SDSS_R:
    ccd.subtract_bias(ccd.CCDData(fits.getdata(os.path.join(path,flat)),unit='adu'),ccd.CCDData(fits.getdata('jp_mbias_avg.fits'),unit='adu'), add_keyword='mbias subtracted flat_SDSS_R')

for flat in flatlist_SDSS_G:
    ccd.subtract_bias(ccd.CCDData(fits.getdata(os.path.join(path,flat)),unit='adu'),ccd.CCDData(fits.getdata('jp_mbias_avg.fits'),unit='adu'), add_keyword='mbias subtracted flat_SDSS_G')

### mbias has now been subtracted from all of the flat filter-images ###

### Now normalize each flat image to one by dividing by the image mode###
