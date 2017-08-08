import numpy      as np
import ccdproc    as ccd
from   astropy.io import fits
from   astropy    import units as u
from   ccdproc    import ImageFileCollection as ifc

path      = '/Users/JPeg/umdastrodata/jpventura/20170617/'

fileKeys  = ['FILENAME','NAXIS1','NAXIS2','OBJECT','OBSTYPE', 'FILTERS' ]

allfiles  = ccd.ImageFileCollection(path,keywords = fileKeys)

gain      = 2.89 * u.electron/u.adu

rdnoise   = 6 * u.electron

# correct bias images for overscan and trim the image:

biasImages=[]

for filename in allfiles.files_filtered(NAXIS1=3128,NAXIS2=3080,OBSTYPE = 'BIAS'):
    ccd = CCDData.read(allfiles.location + filename, unit = u.adu)
    ccd = ccdproc.subtract_overscan(ccd,overscan_axis=0,fits_section =ccd.header['BIASSEC'])
    ccd = ccdproc.trim_image(ccd,fits_section=ccd.header['TRIMSEC'])
    biasImages.append(ccd)

# Create the master bias frame and write to file

master_bias = ccdproc.combine(biasImages,method='average')
master_bias.write('mbias_avg.fits')



# Create the flat fields



# assemble lists of filter-specific flat files.

flatlist_OH     = allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS =     'OH')
flatlist_NH     = allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS =     'NH')
flatlist_UC     = allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS =     'UC')
flatlist_CN     = allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS =     'CN')
flatlist_BC     = allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS =     'BC')
flatlist_RC     = allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS =     'RC')
flatlist_C2     = allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS =     'C2')
flatlist_SDSS_R = allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS = 'SDSS-R')
flatlist_SDSS_G = allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS = 'SDSS-G')
