# Porkchop-Plot-Generator Libraries
import sys 

sys.path.append('D:/Yongjin/Code/ACML/src/python_tools')

import planetary_data as pd
from porkchap import interplanetary_porkchop

# Main script

def main():
    print('===========================================================')
    print('===============Prok Chap Plot을 만드는 파일================')
    print('===========================================================')

    departure0 = input("Enter initial departure date (YYYY-MM-DD): ")
    departure1 = input("Enter final departure date (YYYY-MM-DD): ")
    arrival0 = input("Enter initial arrival date (YYYY-MM-DD): ")
    arrival1 = input("Enter final arrival date (YYYY-MM-DD): ")

    # config parameters for porkchop plot generator
    config = {
        'planet0'       : pd.earth[ 'SPICE_ID' ],     # Departure planet
        'planet1'       : pd.mars[ 'SPICE_ID' ],      # Target planet
        'departure0'    : departure0,                 # Intial departure date
        'ideparture1'   : departure1,                 # Final departure date
        'arrival0'      : arrival0,             # Inital arrival date
        'arrival1'      : arrival1,             # Final arrival date
        'mu'            : pd.sun[ 'mu' ],       # Gravitational parameter in km**3/s**2
        'step'          : 1,                    # Step size in days
        'frame'         : 'J2000',              # Ecliptic of J2000
        'observer'      : '500@0',              # Solar Sytem Barycenter
        'cutoff_v'      : 40.0,                 # Maximum vinf to consider             
        'c3_levels'     : None,                 # C3 levels for contour plot
        'vinf_levels'   : None,                 # vinf levels for contour plot
        'tof_levels'    : None,                 # tof levels for contour plot
        'dv_levels'     : None,                 # dv levels for contour plot
        'dv_cmap'       : 'RdPu_r',             # color map for dv contours
        'figsize'       : ( 10, 10 ),            # figure size for contour plot
        'lw'            : 1.5,                  # linewidth for contour lines
        'title'         : 'Porkchop Plot',      # Plot title
        'fontsize'      : 15,                   # Axes fontsize
        'show'          : True,                 # For displaying the figure
        'filename'      : None,                 # Specify filename for c3 plot
        'filename_dv'   : None,                 # Specify filename for dv plot
        'dpi'           : 300,                  # Specify target dpi
        'load'          : False                 # Load existing ephemeris data
    }

    # Call porkchop plot generator
    interplanetary_porkchop( config, config.get('departure0'), config.get('ideparture1'), config.get('arrival0'), config.get('arrival1'),config.get('cutoff_v'))

if __name__ == "__main__":
    main()