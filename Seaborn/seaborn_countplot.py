def read_tiff(image, encoding_index, resize=None):
    
    '''
    read tiff images and mask.
    ----------------------------
    
    Arguments:
    image -- tiff image
    encoding_index -- corresponding tiff file encoding index.
    
    Returns:
    tiff_image -- tiff image
    tiff_mask -- segmentation mask
    '''
    
    tiff_image = tiff.imread(os.path.join(ROOT, f'train/{image}.tiff'))
    
    if len(tiff_image.shape) == 5:
        tiff_image = np.transpose(tiff_image.squeeze(), (1,2,0))
        
    tiff_mask = rle2mask(train['encoding'][encoding_index],
                         (tiff_image.shape[1], tiff_image.shape[0]))
    
    print(f'Image Shape: {tiff_image.shape}')
    print(f'Image Shape: {tiff_mask.shape}')
    
    if resize:
        rescaled = (tiff_image.shape[1] // resize, tiff_image.shape[0] // resize)
        tiff_image = cv2.resize(tiff_image, rescaled)
        tiff_mask = cv2.resize(tiff_mask, rescaled)

    return tiff_image, tiff_mask

def plot(image, mask):
    
    '''
    plot image and mask
    ---------------------
    
    Arguments:
    image -- tiff image 
    mask -- segmentation mask
    
    Returns:
    matplotlib plot
    '''
    plt.figure(figsize=(15, 15))

    # Image
    plt.subplot(1, 3, 1)
    plt.imshow(image)
    plt.title("Image", fontsize=16)

    # Mask
    plt.subplot(1, 3, 2)
    plt.imshow(mask)
    plt.title("Image Mask", fontsize=16)

    # Image + Mask
    plt.subplot(1, 3, 3)
    plt.imshow(image)
    plt.imshow(mask, alpha=0.5)
    plt.title("Image + Mask", fontsize=16);

def plot_subset(image, mask, start_rh, end_rh, start_cw, end_cw):
    
    '''
    plot image and mask
    ---------------------
    
    Arguments:
    image -- tiff image 
    mask -- segmentation mask
    start_rh -- height start
    end_rh -- height end
    start_cw -- width start 
    end_cw -- width end
    
    Returns:
    matplotlib plot
    '''

    # Figure size
    plt.figure(figsize=(15, 15))

    # subset image and mask
    subset_image = image[start_rh:end_rh, start_cw:end_cw, :]
    subset_mask = mask[start_rh:end_rh, start_cw:end_cw]

    # Image
    plt.subplot(1, 3, 1)
    plt.imshow(subset_image)
    plt.title("Zoomed Image", fontsize=16)

    # Mask
    plt.subplot(1, 3, 2)
    plt.imshow(subset_mask)
    plt.title("Zoomed Image Mask", fontsize=16)

    # Image + Mask
    plt.subplot(1, 3, 3)
    plt.imshow(subset_image)
    plt.imshow(subset_mask, alpha=0.5)
    plt.title("Zoomed Image + Mask", fontsize=16);
    
def countplot(column, plot_type='multiple', gridstyle='whitegrid', gs=None,
              palette='Accent', xlab=None, ylab=None, title=None, fontsize=12):
    
    '''
    Make countplots
    -----------------
    
    Arguments:
    column -- column with categorical values
    plot_type -- multiple grid ('multiple/single')
    gridstyle -- seaborn gridstyle
    gs -- gridspec (if using subplots)
    palette -- color palette
    xlab -- x-axis label
    ylab -- y-axis label
    title -- plot title
    fontsize -- fontsize
    
    Returns:
    sns.countplot()
    '''
    if plot_type=='multiple':
        with sns.axes_style(gridstyle):
            ax = f.add_subplot(gs)
            aa = sns.countplot(column, palette=palette)
            for p in ax.patches:
                height = p.get_height()
                aa.text(p.get_x()+p.get_width()/2.,
                        height,
                        '{:1.2f}%'.format(height/len(column)*100),
                        ha="center", fontsize=fontsize)
            plt.xlabel(xlab,fontsize=fontsize)
            plt.ylabel(ylab,fontsize=fontsize)
            plt.title(title)
            
    elif plot_type=='single':
        with sns.axes_style("whitegrid"):
            aa = sns.countplot(column, palette=palette)
            for p in aa.patches:
                height = p.get_height()
                aa.text(p.get_x()+p.get_width()/2.,
                        height,
                        '{:1.2f}%'.format(height/len(column)*100),
                        ha="center", fontsize=fontsize)
            plt.xlabel(xlab,fontsize=fontsize)
            plt.ylabel(ylab,fontsize=fontsize)
            plt.title(title)
            
def distplot(column, gridstyle='whitegrid', gs=None, stats=False, 
             color='yellow', xlab=None, ylab=None, title=None, fontsize=12):
    
    '''
    Make distplots
    -----------------
    
    Arguments:
    column -- column with categorical values
    gridstyle -- seaborn gridstyle
    gs -- gridspec (if using subplots)
    stats -- mean, median, mode.
    color -- matplotlib color
    xlab -- x-axis label
    title -- plot title
    fontsize -- fontsize
    
    Returns:
    sns.distplot()
    '''
    with sns.axes_style(gridstyle):
        if gs:
            ax = f.add_subplot(gs)
            
        aa = sns.distplot(column, color=color)
        
        if stats:
            mean = column.mean()
            median = column.median()
            mode = column.mode()[0] 
            ax.axvline(int(mean), color='r', linestyle='--')
            ax.axvline(int(median), color='g', linestyle='-')
            ax.axvline(mode, color='b', linestyle='-')
            plt.legend({'Mean':mean,'Median':median,'Mode':mode})
            
        plt.xlabel(xlab,fontsize=fontsize)
        plt.title(title)