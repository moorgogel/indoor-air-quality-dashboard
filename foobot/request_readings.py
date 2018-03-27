import sys
import foobot_tools
import dashboard_tools
from datetime import datetime, timedelta
import commandline_tools

C_MAX_DAYS = 10

(start_timestamp, end_timestamp) = commandline_tools.parse_args(sys.argv)

file_name=sys.argv[len(sys.argv)-1]
config = foobot_tools.read_config_file(file_name)		
print("||sd=",start_timestamp,"||et=",end_timestamp,"||cfg=",file_name)

day_count=0
while True:	
	print("start_timestamp=",start_timestamp.strftime("%a, %d %b %Y %H:%M:%S +0000"),"||",start_timestamp,"||",start_timestamp.strftime('%s'))

	try:
		range_data = foobot_tools.request_foobot_readings(start_timestamp, start_timestamp+timedelta(hours=24)-timedelta(seconds=1), config)

		"""
		range_data={u'end': 1520924121, u'uuid': u'25004664144000A1', u'start': 1520838029, u'datapoints': [[1520838029, 9.5, 18.066, 43.932, 2073, 572, 57.166664], [1520838332, 9.040009, 18.027, 43.891, 2067, 570, 56.54001], [1520838635, 9.040009, 17.982, 43.808, 2052, 566, 56.206673], [1520838938, 9.040009, 17.943, 43.781, 2039, 563, 55.956673], [1520839241, 8.580017, 17.911, 43.75, 2023, 558, 55.080017], [1520839544, 8.580017, 17.874, 43.724, 2018, 557, 54.99668], [1520839847, 9.040009, 17.84, 43.696, 2021, 558, 55.54001], [1520840150, 8.580017, 17.799, 43.657, 2030, 560, 55.24668], [1520840454, 8.580017, 17.76, 43.636, 2040, 563, 55.49668], [1520840757, 8.119995, 17.719, 43.593, 2050, 566, 55.28666], [1520841060, 8.119995, 17.678, 43.564, 2071, 572, 55.78666], [1520841363, 7.6600037, 17.633, 43.541, 2095, 578, 55.826668], [1520841666, 8.119995, 17.585, 43.539, 2114, 583, 56.70333], [1520841969, 8.119995, 17.545, 43.53, 2133, 588, 57.119995], [1520842272, 7.6600037, 17.502, 43.534, 2149, 593, 57.076668], [1520842576, 7.200012, 17.46, 43.544, 2164, 597, 56.950012], [1520842879, 7.200012, 17.421, 43.537, 2173, 600, 57.200012], [1520843182, 7.6600037, 17.379, 43.552, 2180, 602, 57.826668], [1520843485, 7.200012, 17.339, 43.57, 2170, 599, 57.116676], [1520843788, 7.200012, 17.3, 43.564, 2156, 595, 56.783348], [1520844091, 8.119995, 17.265, 43.555, 2125, 586, 56.95333], [1520844395, 8.119995, 17.228, 43.556, 2091, 577, 56.20333], [1520844698, 8.580017, 17.198, 43.581, 2052, 566, 55.74668], [1520845001, 8.580017, 17.164, 43.585, 2015, 556, 54.913353], [1520845304, 8.580017, 17.129, 43.604, 1976, 545, 53.99668], [1520845607, 9.040009, 17.087, 43.605, 1933, 534, 53.54001], [1520845910, 9.040009, 17.041, 43.6, 1896, 523, 52.623344], [1520846214, 8.580017, 17.006, 43.585, 1869, 516, 51.580017], [1520846517, 8.580017, 16.968, 43.591, 1846, 509, 50.99668], [1520846820, 8.580017, 16.927, 43.587, 1824, 504, 50.580017], [1520847123, 9.040009, 16.9, 43.713, 1831, 505, 51.123344], [1520847426, 8.580017, 16.893, 43.899, 1867, 515, 51.49668], [1520847729, 8.580017, 16.883, 43.877, 1865, 515, 51.49668], [1520848032, 8.580017, 16.87, 43.827, 1869, 516, 51.580017], [1520848335, 8.119995, 16.838, 43.87, 1893, 522, 51.619995], [1520848638, 8.580017, 16.833, 44.118, 1981, 547, 54.163353], [1520848942, 8.580017, 16.828, 44.243, 2064, 570, 56.080017], [1520849245, 8.119995, 16.815, 44.151, 2052, 566, 55.28666], [1520849548, 8.580017, 16.781, 44.139, 2080, 574, 56.413353], [1520849851, 8.580017, 16.757, 44.362, 2196, 606, 59.080017], [1520850154, 8.119995, 16.761, 45.052, 2421, 668, 63.78666], [1520850457, 8.580017, 16.76, 44.848, 2366, 653, 62.99668], [1520850760, 8.119995, 16.749, 44.469, 2308, 637, 61.20333], [1520851063, 8.119995, 16.732, 44.281, 2317, 639, 61.369995], [1520851367, 8.580017, 16.713, 44.362, 2415, 666, 64.08002], [1520851670, 8.580017, 16.703, 44.746, 2591, 715, 68.163345], [1520851973, 8.119995, 16.695, 44.751, 2575, 710, 67.28667], [1520852282, 7.6600037, 16.691, 44.502, 2508, 692, 65.326675], [1520852579, 8.119995, 16.677, 44.301, 2468, 681, 64.869995], [1520852882, 8.119995, 16.672, 44.361, 2522, 696, 66.119995], [1520853185, 8.580017, 16.691, 44.701, 2648, 730, 69.413345], [1520853489, 8.119995, 16.752, 44.608, 2602, 718, 67.95332], [1520853792, 8.119995, 16.868, 44.512, 2557, 705, 66.869995], [1520854095, 8.119995, 17.026, 44.467, 2531, 698, 66.28667], [1520854398, 8.119995, 17.196, 44.459, 2516, 694, 65.95332], [1520854701, 7.6600037, 17.363, 44.467, 2503, 690, 65.16], [1520855004, 7.200012, 17.527, 44.483, 2489, 686, 64.366684], [1520855307, 7.6600037, 17.687, 44.48, 2481, 684, 64.66], [1520855611, 8.580017, 17.833, 44.47, 2494, 688, 65.913345], [1520855914, 9.5, 17.878, 44.379, 2534, 699, 67.75], [1520856217, 9.5, 17.928, 44.429, 2499, 689, 66.91667], [1520856520, 9.960022, 18.012, 44.363, 2694, 743, 71.87669], [1520856823, 10.880005, 18.17, 44.079, 2711, 748, 73.21333], [1520857126, 9.960022, 18.182, 43.997, 2613, 721, 70.04335], [1520857430, 10.880005, 18.129, 43.931, 2554, 704, 69.54668], [1520857733, 11.339996, 18.121, 43.837, 2465, 680, 68.00666], [1520858036, 11.339996, 18.093, 43.75, 2361, 651, 65.59], [1520858339, 11.800018, 17.963, 43.927, 2253, 622, 63.633354], [1520858642, 10.880005, 17.905, 43.955, 2165, 597, 60.630005], [1520858945, 9.960022, 17.885, 43.909, 2102, 580, 58.293358], [1520859248, 9.960022, 17.868, 43.869, 2035, 561, 56.710022], [1520859551, 10.880005, 17.828, 43.844, 1977, 546, 56.380005], [1520859854, 11.339996, 17.787, 43.852, 1954, 539, 56.25666], [1520860157, 11.339996, 17.74, 43.931, 1862, 514, 54.173332], [1520860461, 10.420013, 17.694, 43.925, 1764, 487, 51.003345], [1520860764, 10.420013, 17.638, 43.888, 1658, 458, 48.58668], [1520861067, 10.420013, 17.501, 43.944, 1582, 437, 46.83668], [1520861370, 9.960022, 17.312, 44.079, 1520, 420, 44.960022], [1520861673, 9.5, 17.261, 44.05, 1472, 406, 43.333332], [1520861977, 9.5, 17.218, 44.04, 1419, 392, 42.166668], [1520862280, 9.960022, 17.16, 44.087, 1409, 389, 42.37669], [1520862583, 9.960022, 17.094, 44.131, 1379, 381, 41.710022], [1520862886, 10.420013, 17.03, 44.189, 1357, 375, 41.670013], [1520863189, 9.960022, 16.976, 44.284, 1352, 374, 41.126686], [1520863492, 9.960022, 16.923, 44.45, 1353, 374, 41.126686], [1520863795, 9.5, 16.88, 44.426, 1349, 373, 40.583336], [1520864099, 10.420013, 16.832, 44.435, 1365, 377, 41.836678], [1520864402, 9.5, 16.781, 44.371, 1400, 387, 41.75], [1520864705, 9.960022, 16.74, 44.311, 1445, 399, 43.210022], [1520865008, 9.5, 16.711, 44.339, 1518, 419, 44.416668], [1520865311, 9.5, 16.72, 44.336, 1645, 454, 47.333332], [1520865615, 9.040009, 16.744, 44.18, 1760, 486, 49.54001], [1520865918, 9.5, 16.716, 44.097, 1843, 509, 51.916664], [1520866221, 9.040009, 16.848, 43.806, 1932, 533, 53.456673], [1520866524, 9.040009, 16.841, 43.917, 2129, 588, 58.04001], [1520866827, 9.960022, 16.842, 44.027, 2210, 610, 60.793358], [1520867131, 9.960022, 16.842, 44.019, 2250, 621, 61.710022], [1520867434, 9.960022, 16.854, 43.898, 2254, 621, 61.710022], [1520867737, 9.960022, 16.832, 43.925, 2279, 629, 62.376686], [1520868040, 9.5, 16.826, 44.031, 2365, 652, 63.833336], [1520868343, 9.040009, 16.831, 44.026, 2380, 656, 63.706673], [1520868647, 9.040009, 16.839, 43.917, 2371, 654, 63.54001], [1520868950, 9.040009, 16.831, 43.856, 2393, 660, 64.04001], [1520869253, 9.040009, 16.815, 43.854, 2463, 680, 65.70667], [1520869556, 9.040009, 16.799, 43.881, 2520, 695, 66.95668], [1520869859, 9.040009, 16.793, 43.872, 2526, 697, 67.12334], [1520870162, 8.580017, 16.787, 43.851, 2543, 701, 66.99669], [1520870466, 9.040009, 16.784, 43.857, 2553, 704, 67.70668], [1520870769, 9.040009, 16.774, 43.88, 2502, 690, 66.54001], [1520871072, 9.040009, 16.765, 43.898, 2438, 673, 65.123344], [1520871375, 9.040009, 16.759, 43.898, 2388, 659, 63.956673], [1520871678, 8.580017, 16.752, 43.898, 2321, 640, 61.913353], [1520871982, 9.040009, 16.737, 43.911, 2233, 616, 60.373344], [1520872285, 9.040009, 16.723, 43.936, 2136, 589, 58.123344], [1520872588, 8.580017, 16.708, 43.986, 2063, 569, 55.99668], [1520872891, 9.040009, 16.702, 43.997, 1998, 551, 54.956673], [1520873194, 8.580017, 16.698, 43.997, 1949, 538, 53.413353], [1520873497, 9.040009, 16.688, 44.005, 1890, 522, 52.54001], [1520873801, 9.040009, 16.675, 44.029, 1813, 500, 50.706673], [1520874104, 8.580017, 16.648, 44.058, 1738, 480, 48.580017], [1520874407, 9.040009, 16.482, 44.33, 1664, 459, 47.29001], [1520874710, 8.119995, 16.464, 44.414, 1616, 446, 45.286663], [1520875013, 8.119995, 16.473, 44.409, 1542, 426, 43.619995], [1520875316, 7.6600037, 16.474, 44.394, 1465, 405, 41.410004], [1520875620, 7.6600037, 16.477, 44.401, 1414, 391, 40.243336], [1520875923, 8.580017, 16.483, 44.482, 1412, 390, 41.080017], [1520876226, 9.040009, 16.483, 44.61, 1384, 382, 40.873344], [1520876529, 9.040009, 16.489, 44.62, 1360, 376, 40.373344], [1520876832, 8.580017, 16.486, 44.64, 1330, 367, 39.163353], [1520877136, 8.580017, 16.486, 44.648, 1293, 357, 38.330017], [1520877439, 9.040009, 16.479, 44.63, 1249, 345, 37.79001], [1520877742, 8.580017, 16.473, 44.604, 1201, 332, 36.24668], [1520878045, 9.040009, 16.47, 44.596, 1159, 320, 35.706673], [1520878348, 8.580017, 16.48, 44.598, 1117, 309, 34.330017], [1520878651, 8.119995, 16.5, 44.561, 1080, 299, 32.97714], [1520878954, 8.580017, 16.614, 44.346, 1051, 290, 32.151443], [1520879258, 9.5, 16.644, 44.223, 1024, 283, 32.071426], [1520879561, 9.5, 16.647, 44.192, 1000, 276, 31.071428], [1520879864, 9.960022, 16.654, 44.145, 985, 272, 30.960022], [1520880167, 9.960022, 16.675, 44.148, 986, 273, 31.102879], [1520880470, 9.040009, 16.731, 44.104, 980, 271, 29.897152], [1520880773, 8.580017, 16.773, 44.077, 972, 269, 29.151445], [1520881077, 9.040009, 16.796, 44.068, 972, 269, 29.611437], [1520881380, 9.5, 16.82, 44.013, 979, 271, 30.357143], [1520881683, 9.040009, 16.841, 43.991, 987, 273, 30.182865], [1520881986, 9.040009, 16.856, 44.018, 984, 272, 30.040009], [1520882289, 9.5, 16.877, 43.992, 980, 271, 30.357143], [1520882593, 9.5, 16.902, 43.965, 976, 270, 30.214285], [1520882896, 9.5, 16.919, 43.937, 974, 269, 30.071428], [1520883199, 9.960022, 16.929, 43.936, 972, 269, 30.53145], [1520883502, 9.960022, 16.938, 43.995, 961, 266, 30.102879], [1520883805, 9.960022, 16.947, 44.053, 947, 262, 29.53145], [1520884108, 9.960022, 16.958, 44.05, 940, 260, 29.245737], [1520884412, 9.5, 16.973, 44.098, 931, 257, 28.357143], [1520884715, 9.5, 16.996, 44.155, 912, 252, 27.642857], [1520885018, 10.420013, 17.009, 44.184, 904, 250, 28.277157], [1520885321, 9.960022, 17.027, 44.201, 893, 247, 27.388594], [1520885624, 10.420013, 17.035, 44.237, 884, 245, 27.56287], [1520885928, 9.960022, 17.036, 44.254, 874, 242, 26.674307], [1520886231, 9.5, 17.04, 44.254, 863, 239, 25.785715], [1520886534, 10.420013, 17.046, 44.254, 853, 236, 26.277157], [1520886837, 10.420013, 17.053, 44.254, 845, 234, 25.991442], [1520887140, 9.960022, 17.061, 44.254, 836, 231, 25.102879], [1520887443, 10.420013, 17.064, 44.254, 830, 230, 25.420013], [1520887746, 9.960022, 17.068, 44.254, 826, 229, 24.817165], [1520888049, 9.960022, 17.075, 44.254, 820, 227, 24.53145], [1520888353, 11.339996, 17.082, 44.254, 816, 226, 25.768568], [1520888656, 10.420013, 17.09, 44.254, 816, 226, 24.848585], [1520889262, 11.339996, 17.108, 44.323, 797, 221, 25.054283], [1520889565, 10.880005, 17.107, 44.345, 796, 220, 24.451433], [1520889869, 10.880005, 17.118, 44.43, 796, 220, 24.451433], [1520890172, 11.339996, 17.123, 44.504, 794, 220, 24.911425], [1520890477, 10.880005, 17.13, 44.51, 789, 219, 24.308577], [1520890778, 11.339996, 17.133, 44.507, 783, 217, 24.482853], [1520891081, 11.339996, 17.141, 44.515, 775, 215, 24.19714], [1520891384, 10.880005, 17.149, 44.522, 768, 212, 23.308577], [1520891688, 10.880005, 17.161, 44.531, 757, 210, 23.022861], [1520891991, 10.880005, 17.179, 44.545, 747, 207, 22.594292], [1520892294, 11.339996, 17.199, 44.537, 731, 202, 22.339996], [1520892597, 10.880005, 17.248, 44.529, 726, 201, 21.737148], [1520892900, 11.339996, 17.366, 44.513, 703, 195, 21.339996], [1520893203, 11.339996, 17.528, 44.513, 685, 190, 20.62571], [1520893507, 11.339996, 17.732, 44.568, 687, 190, 20.62571], [1520893810, 11.339996, 17.957, 44.646, 699, 194, 21.19714], [1520894113, 10.880005, 18.152, 44.731, 715, 198, 21.308577], [1520894416, 11.339996, 18.288, 44.731, 727, 201, 22.19714], [1520894719, 11.800018, 18.432, 44.709, 735, 204, 23.085732], [1520895023, 12.26001, 18.56, 44.718, 742, 205, 23.688581], [1520895326, 12.720001, 18.662, 44.692, 744, 206, 24.29143], [1520895629, 13.180023, 18.766, 44.658, 745, 206, 24.751451], [1520895932, 12.720001, 18.887, 44.606, 739, 205, 24.148573], [1520896235, 8.119995, 18.982, 44.558, 734, 203, 19.262852], [1520896538, 7.6600037, 19.041, 44.496, 728, 202, 18.660004], [1520896842, 7.6600037, 19.086, 44.439, 720, 200, 18.37429], [1520897145, 7.6600037, 19.1, 44.401, 708, 196, 17.80286], [1520897448, 7.6600037, 19.108, 44.37, 701, 194, 17.517147], [1520897751, 8.580017, 19.125, 44.324, 690, 191, 18.008589], [1520898054, 9.040009, 19.142, 44.363, 683, 189, 18.182865], [1520898357, 9.040009, 19.159, 44.316, 682, 189, 18.182865], [1520898660, 9.040009, 19.176, 44.276, 678, 188, 18.040009], [1520898963, 9.960022, 19.192, 44.407, 670, 186, 18.674309], [1520899266, 9.040009, 19.201, 44.507, 662, 183, 17.325722], [1520899570, 9.5, 19.21, 44.484, 649, 180, 17.357143], [1520899873, 9.960022, 19.217, 44.521, 642, 178, 17.53145], [1520900176, 9.040009, 19.235, 44.584, 660, 183, 17.325722], [1520900479, 8.580017, 19.256, 44.563, 667, 185, 17.151445], [1520900782, 8.580017, 19.272, 44.589, 659, 183, 16.86573], [1520901085, 9.040009, 19.286, 44.655, 654, 181, 17.040009], [1520901388, 9.040009, 19.282, 44.717, 650, 180, 16.897152], [1520901691, 8.580017, 19.308, 44.75, 645, 179, 16.294304], [1520901994, 9.960022, 19.378, 44.674, 647, 179, 17.674309], [1520902297, 11.800018, 19.361, 44.715, 649, 180, 19.657162], [1520902600, 10.420013, 19.326, 44.815, 648, 179, 18.1343], [1520902903, 11.339996, 19.338, 44.847, 645, 179, 19.054283], [1520903206, 10.880005, 19.34, 44.857, 639, 177, 18.308577], [1520903509, 10.420013, 19.332, 44.841, 635, 176, 17.705727], [1520903813, 10.880005, 19.32, 44.85, 630, 174, 17.880005], [1520904116, 10.420013, 19.322, 44.868, 626, 173, 17.277157], [1520904419, 10.420013, 19.298, 44.913, 626, 174, 17.420013], [1520904722, 9.960022, 19.291, 45.021, 630, 175, 17.102879], [1520905025, 9.5, 19.275, 45.1, 634, 176, 16.785713], [1520905328, 9.960022, 19.268, 45.18, 635, 176, 17.245735], [1520905631, 10.880005, 19.255, 45.324, 639, 177, 18.308577], [1520905935, 11.339996, 19.247, 45.449, 642, 178, 18.911425], [1520906238, 10.420013, 19.236, 45.488, 648, 180, 18.277157], [1520906541, 10.880005, 19.226, 45.575, 662, 184, 19.308577], [1520906844, 9.960022, 19.232, 45.651, 679, 188, 18.960022], [1520907147, 10.420013, 19.238, 45.695, 691, 191, 19.848585], [1520907450, 9.960022, 19.247, 45.723, 707, 196, 20.102879], [1520907753, 9.960022, 19.254, 45.765, 733, 203, 21.102879], [1520908056, 9.040009, 19.261, 45.728, 751, 208, 20.897152], [1520908359, 8.119995, 19.268, 45.648, 753, 208, 19.977139], [1520908662, 7.6600037, 19.277, 45.538, 747, 207, 19.37429], [1520908966, 8.580017, 19.284, 45.409, 771, 214, 21.294304], [1520909269, 8.580017, 19.288, 45.228, 769, 213, 21.151445], [1520909572, 8.119995, 19.286, 45.097, 746, 207, 19.834282], [1520909875, 7.200012, 19.278, 44.976, 724, 201, 18.057156], [1520910178, 8.580017, 19.267, 44.888, 714, 198, 19.008589], [1520910481, 7.6600037, 19.257, 44.807, 700, 194, 17.517147], [1520910784, 8.119995, 19.255, 44.733, 686, 190, 17.405708], [1520911087, 7.6600037, 19.245, 44.706, 693, 192, 17.231432], [1520911390, 8.119995, 19.237, 44.711, 770, 213, 20.691423], [1520911694, 8.580017, 19.227, 44.699, 829, 229, 23.43716], [1520911997, 8.119995, 19.224, 44.68, 858, 238, 24.262852], [1520912300, 7.6600037, 19.218, 44.663, 908, 251, 25.660004], [1520912603, 8.580017, 19.213, 44.656, 883, 244, 25.580017], [1520912906, 8.119995, 19.212, 44.63, 856, 237, 24.119995], [1520913209, 8.580017, 19.206, 44.628, 837, 232, 23.86573], [1520913512, 8.119995, 19.205, 44.619, 832, 230, 23.119995], [1520913816, 8.580017, 19.202, 44.62, 875, 242, 25.294302], [1520914119, 9.5, 19.196, 44.616, 889, 246, 26.785715], [1520914422, 9.960022, 19.188, 44.621, 880, 243, 26.817165], [1520914725, 9.960022, 19.176, 44.622, 874, 242, 26.674307], [1520915028, 9.5, 19.166, 44.638, 863, 239, 25.785715], [1520915331, 9.040009, 19.154, 44.67, 843, 233, 24.46858], [1520915634, 8.580017, 19.145, 44.7, 819, 227, 23.151445], [1520915937, 9.040009, 19.135, 44.727, 795, 220, 22.611437], [1520916240, 8.119995, 19.124, 44.742, 763, 211, 20.405708], [1520916544, 8.119995, 19.114, 44.744, 736, 204, 19.405708], [1520916847, 8.119995, 19.113, 44.79, 763, 211, 20.405708], [1520917150, 7.6600037, 19.105, 44.769, 834, 231, 22.80286], [1520917453, 7.200012, 19.088, 44.703, 778, 215, 20.057156], [1520917756, 6.7400208, 19.07, 44.658, 712, 197, 17.025734], [1520918059, 6.7400208, 19.077, 44.561, 671, 186, 15.454307], [1520918362, 8.119995, 19.116, 44.424, 645, 179, 15.834281], [1520918665, 9.5, 19.117, 44.402, 624, 173, 16.357143], [1520918969, 10.420013, 19.109, 44.353, 610, 169, 16.705727], [1520919272, 10.880005, 19.112, 44.261, 595, 165, 16.594292], [1520919575, 10.880005, 19.111, 44.233, 585, 162, 16.165718], [1520919878, 11.339996, 19.119, 44.202, 578, 160, 16.339996], [1520920181, 11.339996, 19.083, 44.188, 574, 159, 16.19714], [1520920484, 9.960022, 19.112, 44.134, 568, 158, 14.674308], [1520920787, 11.339996, 19.108, 44.123, 565, 157, 15.911425], [1520921091, 10.420013, 19.089, 44.083, 560, 155, 14.705728], [1520921394, 11.339996, 19.069, 44.027, 571, 159, 16.19714], [1520921697, 10.880005, 19.038, 43.997, 600, 166, 16.737148], [1520922000, 9.5, 18.965, 44.027, 611, 169, 15.785714], [1520922303, 9.5, 18.944, 43.967, 599, 166, 15.357143], [1520922606, 9.5, 18.973, 43.886, 586, 163, 14.928572], [1520922909, 9.960022, 18.915, 43.909, 575, 160, 14.960022], [1520923212, 9.5, 18.9, 43.867, 562, 156, 13.928572], [1520923515, 9.5, 18.88, 43.831, 556, 154, 13.642857], [1520923818, 9.960022, 18.851, 43.784, 555, 154, 14.102879], [1520924121, 9.960022, 18.827, 43.747, 564, 157, 14.53145]], u'units': [u's', u'ugm3', u'C', u'pc', u'ppm', u'ppb', u'%'], u'sensors': [u'time', u'pm', u'tmp', u'hum', u'co2', u'voc', u'allpollu']}
		"""
		print("range_data=",range_data)          
		print("start=",range_data['start'])
		print("end=",range_data['end'])
		print("uuid=",range_data['uuid'])                     
		print("datapoints=",range_data['datapoints'])
		print("datapoints[0][0]=",range_data['datapoints'][0][0])
		print("units=",range_data['units'])
		print("sensors=",range_data['sensors'])
		print("sensors[0]=",range_data['sensors'][0])

		foobot_tools.validate_sensors(range_data)
		normalized_data = foobot_tools.normalize_readings(range_data)
		
		shifted_data = foobot_tools.get_intervals_shifted(normalized_data)
		dashboard_tools.send_requests(shifted_data, config)
	except ImportError as e:
		print(e)

	start_timestamp=start_timestamp+timedelta(hours=24)
	day_count=day_count+1
	if day_count>=C_MAX_DAYS:
		break
	if end_timestamp==None or start_timestamp>end_timestamp:
		break

