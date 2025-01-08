'''
Interplanetary Trajectory V-Infinity Matcher (ITVIM) Unit Tests
'''

# 3rd party libraries
import pytest
import spiceypy as spice
import sys

sys.path.append('D:/Yongjin/Code/ACML/src/python_tools')

# AWP library
from ITVIM import ITVIM
import numerical_tools as nt
import planetary_data  as pd
import spice_data      as sd

# Treat all warnings as errors
pytestmark = pytest.mark.filterwarnings( 'error' )

def test_ITVIM_empty_sequence_expect_throw():
	with pytest.raises( RuntimeError ):
		ITVIM( {} )

def test_mars_2020( plot = True ):

	spice.furnsh( sd.leapseconds_kernel )
	spice.furnsh( sd.de432 )

	sequence = [ 
		{
		'planet': 3,
		'time'  : '2020-07-30',
		'tm'    : 1
		},
		{
		'planet'   : 4,
		'planet_mu': pd.mars[ 'mu' ],
		'time'     : '2021-02-18',
		'tm'       : -1,
		'tol'      : 1e-5
		}
	]
	itvim = ITVIM( { 'sequence': sequence } )
	itvim.print_summary()

	t0_target = spice.str2et( '2020-07-30' )
	t1_target = spice.str2et( '2021-02-18' )
	t_targets = [ t0_target, t1_target ]
	t_tol     = 90 * 24 * 3600.0 # t2_target is about 3 days different

	if plot:
		itvim.plot_orbits( {
			'planets'  : [pd.mars, pd.earth ],
			'colors'   : [ 'm', 'c', 'lime' ],
			'sc_labels': [ 'Mars2020' ],
			'traj_lws' : 2,
			'show'     : True
			} )

if __name__ == '__main__':
	test_mars_2020( plot = True )