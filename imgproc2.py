from   astropy    import units as u
from   astropy.io import fits
import matplotlib.pyplot as plt
import ccdproc as cp

# The path listed below is for the directory on ShadowHQ not local.
path      = '/Users/JPeg/cometdata/'

fileKeys  = ['FILENAME','NAXIS1','NAXIS2','OBJECT','OBSTYPE', 'FILTERS' ]

allfiles  = cp.ImageFileCollection(path,keywords = fileKeys)

gain      = 2.89 * u.electron/u.adu

rdnoise   = 6 * u.electron

# correct bias images for overscan and trim the image:

biasImages=[]

for filename in allfiles.files_filtered(NAXIS1=3128,NAXIS2=3080,OBSTYPE = 'BIAS'):
    ccd = fits.getdata(allfiles.location + filename)
    print(ccd)
    ccd = cp.CCDData(ccd, unit = u.adu)
    print(ccd)
    ccd = cp.subtract_overscan(ccd,overscan_axis = 1, overscan = ccd[:,3099:3125])
    print(ccd)
    ccd = cp.trim_image(ccd,fits_section = '[27:3095,3:3078]')
    print(ccd)
    biasImages.append(ccd)

# Create the master bias frame and write to file

master_bias = cp.combine(biasImages,output_file = path + 'mbias_avg.fits', method='average')
#master_bias.write('mbias_avg.fits',clobber=True)


# assemble lists of filter-specific flat files.
flatlist_OH = []
for filename in allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS='OH'):
    ccd = fits.getdata(allfiles.location + filename)
    ccd = cp.CCDData(ccd, unit= u.adu)
    ccd = cp.subtract_overscan(ccd,overscan_axis=1,overscan = ccd[:,3099:3125])
    ccd = cp.trim_image(ccd,fits_section='[27:3095,3:3078]')
    ccd = cp.subtract_bias(ccd,cp.CCDData(fits.getdata('mbias_avg.fits'),unit = u.adu)
    flatlist_OH.append(ccd)
master_flat_OH = cp.combine(flatlist_OH,output_file = 'mflat_OH_avg.fits', method='average')
master_flat_OH.write('master_flat_OH_avg.fits')

flatlist_NH     = []
for filename in allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS='NH'):
    ccd = fits.getdata(allfiles.location + filename)
    ccd = cp.CCDData(ccd, unit = u.adu)
    ccd = cp.subtract_overscan(ccd,overscan_axis=1,overscan = ccd[:,3099:3125]])
    ccd = cp.trim_image(ccd,fits_section='[27:3095,3:3078]')
    ccd = cp.subtract_bias(ccd, path + 'mbias_avg.fits')
    flatlist_NH.append(ccd)
master_flat_NH = cp.combine(flatlist_NH,method='average')
master_flat_NH.write('master_flat_NH_avg.fits')

flatlist_UC     = []
for filename in allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS='UC'):
    ccd = fits.getdata(allfiles.location + filename)
    ccd = cp.CCDData(ccd, unit = u.adu)
    ccd = cp.subtract_overscan(ccd,overscan_axis=1,overscan = ccd[:,3099:3125]])
    ccd = cp.trim_image(ccd,fits_section='[27:3095,3:3078]')
    ccd = cp.subtract_bias(ccd, path + 'mbias_avg.fits')
    flatlist_UC.append(ccd)
master_flat_UC = cp.combine(flatlist_UC,method='average')
master_flat_UC.write('master_flat_UC_avg.fits')

flatlist_CN     = []
for filename in allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS='CN'):
    ccd = fits.getdata(allfiles.location + filename)
    ccd = cp.CCDData(ccd, unit = u.adu)
    ccd = cp.subtract_overscan(ccd,overscan_axis=1,overscan = ccd[:,3099:3125])
    ccd = cp.trim_image(ccd,fits_section='[27:3095,3:3078]')
    ccd = cp.subtract_bias(ccd, path + 'mbias_avg.fits')
    flatlist_CN.append(ccd)
master_flat_CN = cp.combine(flatlist_CN,method='average')
master_flat_CN.write('master_flat_CN_avg.')

flatlist_BC     = []
for filename in allfiles.filesBCiltered(OBSTYPE='SKY FLAT',FILTERS='BC'):
    ccd = fits.getdata(allfiles.location + filename)
    ccd = cp.CCDData(ccd, unit = u.adu)
    ccd = cp.subtract_overscan(ccd,overscan_axis=1,overscan = ccd[:,3099:3125])
    ccd = cp.trim_image(ccd,fits_section='[27:3095,3:3078]')
    ccd = cp.subtract_bias(ccd, path + 'mbias_avg.fits')
    flatlist_BC.append(ccd)
master_flat_BC = cp.combine(flatlist_BC,method='average')
master_flat_BC.write('master_flat_BC_avg.fits')

flatlist_RC     = []
for filename in allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS='RC'):
    ccd = fits.getdata(allfiles.location + filename)
    ccd = cp.CCDData(ccd, unit = u.adu)
    ccd = cp.subtract_overscan(ccd,overscan_axis=1,overscan = ccd[:,3099:3125])
    ccd = cp.trim_image(ccd,fits_section='[27:3095,3:3078]')
    ccd = cp.subtract_bias(ccd, path + 'mbias_avg.fits')
    flatlist_RC.append(ccd)
master_flat_RC = cp.combine(flatlist_RC,method='average')
master_flat_RC.write('master_flat_RC_avg.fits')

flatlist_C2     = []
for filename in allfiles.files_filtßered(OBSTYPE='SKY FLAT',FILTERS='C2'):
    ccd = fits.getdata(allfiles.location + filename)
    ccd = cp.CCDData(ccd, unit = u.adu)
    ccd = cp.subtract_overscan(ccd,overscan_axis=1,overscan = ccd[:,3099:3125])
    ccd = cp.trim_image(ccd,fits_section='[27:3095,3:3078]')
    ccd = cp.subtract_bias(ccd, path + 'mbias_avg.fits')
    flatlist_C2.append(ccd)
master_flat_C2 = cp.combine(flatlist_C2,method='average')
master_flat_C2.write('master_flat_C2_avg.fits')

flatlist_SDSS_R = []
for filename in allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS='SDSS-R'):
    ccd = fits.getdata(allfiles.location + filename)
    ccd = cp.CCDData(ccd, unit = u.adu)
    ccd = cp.subtract_overscan(ccd,overscan_axis=1,overscan = ccd[:,3099:3125])
    ccd = cp.trim_image(ccd,fits_section='[27:3095,3:3078]')
    ccd = cp.subtract_bias(ccd, path + 'mbias_avg.fits')
    flatlist_SDSS_R.append(ccd)
master_flat_SDSS_R = cp.combine(flatlist_SDSS_R,method='average')
master_flat_SDSS_R.write('master_flat_SDSS_R_avg.fits')

flatlist_SDSS_G = []
for filename in allfiles.files_filtered(OBSTYPE='SKY FLAT',FILTERS='SDSS-G'):
    ccd = cp.CCDData.read(allfiles.location + filename, unit = u.adu)
    ccd = cp.subtract_overscan(ccd,overscan_axis=1,overscan = ccd[:,3099:3125])
    ccd = cp.trim_image(ccd,fits_section='[27:3095,3:3078]')
    ccd = cp.subtract_bias(ccd, path + 'mbias_avg.fits')
    flatlist_SDSS_G.append(ccd)
master_flat_SDSS_G = cp.combine(flatlist_OH,method='average')
master_flat_SDSS_G.write('master_flat_SDSS_G_avg.fits')
