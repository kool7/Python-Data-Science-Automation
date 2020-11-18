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
    ylab -- y-axois label
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