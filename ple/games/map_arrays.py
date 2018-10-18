import numpy as np
map_dict = dict(map = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 2, 2, 9], [9, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 12, 12, 12, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map19 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 11, 0, 0, 0, 11, 0, 21, 0, 0, 9], [9, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 11, 0, 0, 0, 2, 2, 0, 0, 20, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map18 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 21, 0, 1, 1, 1, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 20, 0, 0, 0, 2, 2, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 11, 0, 0, 0, 2, 2, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map_3 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 2, 2, 9], [9, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 12, 12, 12, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map8 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 11, 0, 0, 9], [9, 0, 0, 0, 12, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 9], [9, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 20, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 21, 0, 2, 2, 0, 0, 11, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map9 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 20, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 9], [9, 1, 12, 12, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 21, 0, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 12, 12, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 11, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map7 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 20, 0, 0, 0, 2, 2, 1, 12, 12, 1, 1, 9], [9, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 21, 0, 2, 2, 0, 0, 11, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map13 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 20, 0, 9], [9, 0, 21, 0, 0, 0, 11, 0, 0, 1, 1, 1, 1, 1, 1, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 9], [9, 1, 12, 12, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 2, 2, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map12 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 20, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 9], [9, 1, 12, 12, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 9], [9, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 2, 2, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map6 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 21, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 9], [9, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 11, 0, 0, 20, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map4 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 21, 0, 0, 0, 11, 0, 0, 0, 0, 20, 9], [9, 12, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map10 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 21, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 9], [9, 1, 12, 12, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 12, 12, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 11, 0, 20, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map11 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 9], [9, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 2, 2, 0, 9], [9, 1, 12, 12, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 9], [9, 0, 0, 0, 0, 0, 20, 0, 0, 11, 0, 0, 2, 2, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map5 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 21, 0, 0, 0, 2, 2, 1, 1, 1, 1, 1, 9], [9, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 9], [9, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 12, 12, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 11, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map1 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 2, 2, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 12, 12, 12, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map15 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 2, 2, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 9], [9, 0, 0, 0, 0, 11, 0, 0, 0, 0, 11, 2, 2, 20, 0, 9], [9, 1, 12, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map14 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 0, 0, 20, 0, 0, 1, 1, 1, 0, 0, 9], [9, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 12, 12, 12, 12, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map0 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 0, 0, 0, 0, 0, 11, 0, 21, 0, 0, 0, 1, 2, 2, 9], [9, 12, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 12, 12, 12, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map2 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 2, 2, 0, 0, 0, 20, 0, 11, 0, 1, 1, 1, 2, 2, 9], [9, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 9], [9, 2, 2, 0, 0, 0, 11, 0, 21, 0, 0, 0, 1, 2, 2, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 12, 12, 12, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map16 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 20, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 21, 9], [9, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0, 0, 1, 1, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map17 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 20, 2, 2, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 9], [9, 0, 0, 0, 0, 0, 0, 11, 0, 21, 0, 2, 2, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map3 = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 2, 2, 0, 20, 9], [9, 12, 12, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 9], [9, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 2, 2, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ),
map_similarity = np.asarray( [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 3, 3, 9], [9, 7, 7, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 3, 3, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 9], [9, 2, 2, 4, 4, 4, 4, 4, 4, 0, 0, 5, 5, 5, 5, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], [9, 1, 1, 1, 1, 1, 1, 1, 1, 12, 12, 12, 7, 7, 7, 9], [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]] ))
