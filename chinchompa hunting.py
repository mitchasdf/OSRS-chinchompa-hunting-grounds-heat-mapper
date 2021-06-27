
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


''' Form Plus (+)
#  #  #  #  #  #  #
#  #  #  #  #  #  #
#  #  #  O  #  #  #
#  #  O  O  O  #  #
#  #  #  O  #  #  #
#  #  #  #  #  #  #
#  #  #  #  #  #  #
'''
''' Form X (x)
#  #  #  #  #  #  #
#  #  #  #  #  #  #
#  #  O  #  O  #  #
#  #  #  O  #  #  #
#  #  O  #  O  #  #
#  #  #  #  #  #  #
#  #  #  #  #  #  #
'''
''' Form Diamond (MLG for short, I guess)
#  #  #  #  #  #  #
#  #  #  O  #  #  #
#  #  #  #  #  #  #
#  O  #  O  #  O  #
#  #  #  #  #  #  #
#  #  #  O  #  #  #
#  #  #  #  #  #  #
'''

FORMPLUS = [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]
FORMX = [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)]
FORMDIAMOND = [(-2, 0), (0, -2), (0, 0), (0, 2), (2, 0)]


SPAWN_LOCATIONS = [(7,2), (7,5), (12,5), (17,4), (18,7), (1,7), (9,9), (14,11), (2,13), (5,17), (8,15),
                   (9,19), (17,15), (15,18), (2,10)]

data = [  # dense tiles which cannot be traversed
   # 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21   X
   #                                                                       Y
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 0
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 1
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],  # 2
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],  # 3
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 4
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 9
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 10
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 14
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 15
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 16
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],  # 17
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],  # 18
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],  # 19
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]   # 20
]


# A custom exception for some custom except logic
class MyException(Exception):
    pass


# The distance algorithm probably (I say) used by OSRS
def osrs_box_dist(x, y, x2, y2):
    return max([abs(x - x2), abs(y - y2)])


# Return a custom colour gradient depending on a float value from 0 to 1
def gradient(value):
    red = 0
    green = 0
    blue = 0
    if value < 0.5:
        green = 1
        red = value * 2
    elif value == 0.5:
        green = 1
        red = 1
    else:
        red = 1
        green = (1 - value) * 2
    if value > 0.9:
        blue = (value - 0.9) * 9.99
    if value > 0.95:
        red = 1 - ((value - 0.95) * 19.99)
    return red, green, blue, 1  # 1 = full opacity


# Keeps value i within iMin and iMax, optionally throwing an exception if it is out of bounds
def keep_within(i, iMin, iMax, throws=False):
    if i < iMin:
        if throws:
            raise MyException()
        return iMin
    if i > iMax:
        if throws:
            raise MyException()
        return iMax
    return i


# Access the data map (are the tiles dense or not (1 or 0)) with the option to throw an exception upon out of bounds
def data_access(x, y, offsetX=0, offsetY=0, throws=False):
    x += offsetX
    y += offsetY
    x = keep_within(x, 0, 21, throws)
    y = keep_within(y, 0, 20, throws)
    return data[y][x]


# Instantiate the spawn points as objects from their respective coordinates and what not
def theMaps():
    global spawn_points
    spawn_points = []
    spawns = [[False for _ in range(22)] for __ in range(21)]
    ferns = [[False for _ in range(22)] for __ in range(21)]
    f = [(5,3), (15,3), (2,7), (12,7), (19, 8), (8,10), (18,11), (10,14), (3,17), (6,17),
         (8,18), (17,18)]  # These are the locations of ferns. You cannot place traps on these locations.
    for i in SPAWN_LOCATIONS:
        spawns[i[1]][i[0]] = True
        spawn_points.append(SpawnPoint(i[0], i[1]))
    for i in f:
        ferns[i[1]][i[0]] = True
    heat = [[0 for _ in range(22)] for __ in range(21)]
    return spawns, ferns, heat


heat = []


# Accesses the heat map with either write or read functionality
def heat_access(x, y, offsetX=0, offsetY=0, write=0.0):
    x += offsetX
    y += offsetY
    try:
        # Or else the function may access heat from an out of bounds tile
        x = keep_within(x, 0, 21, throws=True)
        y = keep_within(y, 0, 20, throws=True)
        if write > 0.0:
            # If the tile is not traversable, don't even try to obtain heat from it
            if not data_access(x, y):
                heat[y][x] += write
        else:
            return heat[y][x]
    except MyException:
        return 0


# Returns the lowest and highest amounts of heat found, in order to exaggerate the heat colours to differentiate them
def get_heat_bounds(hot_spots):
    lowest = None
    highest = 0
    for y in range(len(hot_spots)):
        for x in range(len(hot_spots[0])):
            if hot_spots[y][x].available:
                # Or else lowest ends up always being 0, which defeats the purpose of the function
                # 0 is collected from inside the walls, for example
                if lowest is None:
                    lowest = hot_spots[y][x].heat
                else:
                    lowest = min([hot_spots[y][x].heat, lowest])
                highest = max([hot_spots[y][x].heat, highest])
    return lowest, highest


heat_distribution_intensity = 0.5


def new_heat_over_distance_scale(dissipation_intensity):
    return [100 * (dissipation_intensity ** i) for i in range(9)]


class SpawnPoint:
    total_tiles_to_distribute_to = 0
    heat_distribution_scale = 0
    x = 0
    y = 0
    heat_over_distance_scale = new_heat_over_distance_scale(heat_distribution_intensity)

    def __init__(self, x, y):
        if x == 0 and y == 0:
            return
        self.heat_over_distance_scale = new_heat_over_distance_scale(heat_distribution_intensity)
        self.x = x
        self.y = y
        for offset_x in range(-8, 9):
            for offset_y in range(-8, 9):
                try:
                    if not data_access(x, y, offset_x, offset_y, throws=True):
                        self.total_tiles_to_distribute_to += 1
                except MyException:
                    continue
        self.heat_distribution_scale = (17 * 17) / self.total_tiles_to_distribute_to

    def emanate(self):
        for offset_x in range(-8, 9):
            for offset_y in range(-8, 9):
                box_dist = osrs_box_dist(0, 0, offset_x, offset_y)
                _heat = self.heat_over_distance_scale[box_dist]
                heat_access(self.x, self.y, offset_x, offset_y, _heat * self.heat_distribution_scale)


ferns = []


class TrapFormation:
    locations = []
    boundaries = [0, 0, 0, 0]
    heat_share_map = []

    def __init__(self, formation):
        if not formation:
            raise MyException()
        self.locations = formation
        for i in formation:
            self.boundaries[0] = min([self.boundaries[0], i[0] - 2])
            self.boundaries[1] = min([self.boundaries[1], i[1] - 2])
            self.boundaries[2] = max([self.boundaries[2], i[0] + 2])
            self.boundaries[3] = max([self.boundaries[3], i[1] + 2])
        size = self.get_size()
        self.heat_share_map = [[0.0 for x in range(size[0])] for y in range(size[1])]
        for y in range(size[1]):
            for x in range(size[0]):
                for i in self.locations:
                    if x == keep_within(x, i[0] - 2, i[0] + 2) and y == keep_within(y, i[1] - 2, i[1] + 2):
                        self.heat_share_map[y][x] += 1
                if self.heat_share_map[y][x] > 0:
                    self.heat_share_map[y][x] = (8 - self.heat_share_map[y][x]) / 7

    def get_size(self):
        return self.boundaries[2] - self.boundaries[0], self.boundaries[3] - self.boundaries[1]

    def check_avail(self, x, y):
        try:
            for off in self.locations:
                if data_access(x, y, off[0], off[1], throws=True):
                    return False
                if ferns[y + off[1]][x + off[0]]:
                    return False
        except MyException:
            return False
        return True


class HotSpot:
    x = 0
    y = 0
    heat = 0
    available = False
    formation = None

    def __init__(self, x, y, formation):
        self.formation = formation
        self.x = x
        self.y = y
        self.available = self.formation.check_avail(x, y)
        if self.available:
            self.collect_heat()

    def collect_heat(self):
        offsets = self.formation.locations
        half_w = self.formation.boundaries[2] - 1
        half_h = self.formation.boundaries[3] - 1
        for off in offsets:
            for x in range(-2, 3):
                for y in range(-2, 3):
                    _x = x + off[0]
                    _y = y + off[1]
                    new_heat = heat_access(_x + self.x, _y + self.y)
                    new_heat *= self.formation.heat_share_map[y + half_h][x + half_w]
                    self.heat += new_heat


# Only build these once now, instead of every tick, or every iteration of trap placement
# CPU intensive in large quantities, built to only require 1 for use on all iterations of trap placement
XFORMATION = TrapFormation(FORMX)
PLUSFORMATION = TrapFormation(FORMPLUS)
DIAMONDFORMATION = TrapFormation(FORMDIAMOND)

spawn_points = [SpawnPoint(0, 0)]


def main_tick():
    global spawns, ferns, heat, plot_data_x, plot_data_y, plot_data_0_c, plot_data_1_c, plot_data_2_c, plot_data_3_c,\
           FORM_X_upper_heat_boundary, FORM_PLUS_upper_heat_boundary, FORM_DIAMOND_upper_heat_boundary
    spawns, ferns, heat = theMaps()

    [i.emanate() for i in spawn_points]

    FORM_X_hot_spots = [[HotSpot(x, y, XFORMATION) for x in range(22)] for y in range(21)]
    FORM_PLUS_hot_spots = [[HotSpot(x, y, PLUSFORMATION) for x in range(22)] for y in range(21)]
    FORM_DIAMOND_hot_spots = [[HotSpot(x, y, DIAMONDFORMATION) for x in range(22)] for y in range(21)]

    FORM_X_lower_heat_boundary, FORM_X_upper_heat_boundary = get_heat_bounds(FORM_X_hot_spots)
    FORM_PLUS_lower_heat_boundary, FORM_PLUS_upper_heat_boundary = get_heat_bounds(FORM_PLUS_hot_spots)
    FORM_DIAMOND_lower_heat_boundary, FORM_DIAMOND_upper_heat_boundary = get_heat_bounds(FORM_DIAMOND_hot_spots)

    # im sure might come in handy one day
    # lowest_heat_boundary = min([FORM_X_lower_heat_boundary,
    #                             FORM_PLUS_lower_heat_boundary,
    #                             FORM_DIAMOND_lower_heat_boundary])
    # highest_heat_boundary = max([FORM_X_upper_heat_boundary,
    #                             FORM_PLUS_upper_heat_boundary,
    #                             FORM_DIAMOND_upper_heat_boundary])

    heat_map_coolest = 0
    heat_map_hottest = 0

    for y in range(len(heat)):
        for x in range(len(heat[0])):
            heat_map_coolest = min([heat_map_coolest, heat[y][x]])
            heat_map_hottest = max([heat_map_hottest, heat[y][x]])

    plot_data_x = []
    plot_data_y = []
    plot_data_0_c = []
    plot_data_1_c = []
    plot_data_2_c = []
    plot_data_3_c = []

    # This is written weirdly because all 4 scatter plots access the same array for plot data coordinates
    # So every time 1 thing needs plotting in just 1 of the scatter plots but not the others, I then need to also add a
    #   blank colour (0,0,0,0) to all of the other plot data colour arrays
    # All of these arrays need to be the same length. It is just how matplotlib works. All of this because I made the
    #   mistake of not separating the plot_data_x and plot_data_y arrays into 4 separate pairs for each scatter plot
    for y in range(len(data)):
        for x in range(len(data[0])):
            # len(data) - y  because data on the Y-axis should be flipped when drawn, as 0 faces downwards in the plot
            _y = len(data) - y
            heat_append = False
            appending = False
            if data[y][x]:
                appending = True
                # Draw the walls in black
                plot_data_0_c.append((0, 0, 0, 1))
                plot_data_1_c.append((0, 0, 0, 1))
                plot_data_2_c.append((0, 0, 0, 1))
                plot_data_3_c.append((0, 0, 0, 1))
            elif heat[y][x] > 0:
                # Draw the tiles of the heat distribution map in scale of amount of heat on that tile.
                heat_append = True
                if heat[y][x]:
                    # For the gradient() calculations, subtracting the coolest heat as such will
                    #   allow for higher human ability of distinction between amounts of heat on each tile
                    plot_data_0_c.append(gradient((heat[y][x] - heat_map_coolest) /
                                                  (heat_map_hottest - heat_map_coolest)))
                else:
                    plot_data_0_c.append((0, 0, 0, 0))

            x_append = False
            plus_append = False
            diamond_append = False

            # Draw each tile in scale of how much heat is collected if that tile were the center of the trap formation
            if FORM_X_hot_spots[y][x].available:
                x_append = True
                plot_data_1_c.append(gradient((FORM_X_hot_spots[y][x].heat - FORM_X_lower_heat_boundary) /
                                                (FORM_X_upper_heat_boundary - FORM_X_lower_heat_boundary)))

            if FORM_PLUS_hot_spots[y][x].available:
                plus_append = True
                plot_data_2_c.append(gradient((FORM_PLUS_hot_spots[y][x].heat - FORM_PLUS_lower_heat_boundary) /
                                                (FORM_PLUS_upper_heat_boundary - FORM_PLUS_lower_heat_boundary)))

            if FORM_DIAMOND_hot_spots[y][x].available:
                diamond_append = True
                plot_data_3_c.append(gradient((FORM_DIAMOND_hot_spots[y][x].heat - FORM_DIAMOND_lower_heat_boundary) /
                                                (FORM_DIAMOND_upper_heat_boundary - FORM_DIAMOND_lower_heat_boundary)))

            if heat_append or x_append or plus_append or diamond_append:
                appending = True
                # Add the dummy blank colours if necessary to keep the arrays the same length
                if not heat_append:
                    plot_data_0_c.append((0,0,0,0))
                if not x_append:
                    plot_data_1_c.append((0,0,0,0))
                if not plus_append:
                    plot_data_2_c.append((0,0,0,0))
                if not diamond_append:
                    plot_data_3_c.append((0,0,0,0))

            if ferns[y][x]:
                plot_data_x.append(x)
                plot_data_y.append(_y)
                # Don't draw ferns for the heat distribution map, as it is still useful to know how much heat is under
                #   a fern
                plot_data_0_c.append((0, 0, 0, 0))
                # Draw the ferns in black. There is never a need to worry about the heat collected from this tile
                #   as the middle trap of the formation can never be placed on a fern.
                plot_data_1_c.append((0, 0, 0, 1))
                plot_data_2_c.append((0, 0, 0, 1))
                plot_data_3_c.append((0, 0, 0, 1))
            if appending:
                # If ANY data was appended to the colour arrays, now is the time to also append the current x and y
                #   the loop is working with.
                plot_data_x.append(x)
                plot_data_y.append(_y)

    axes[0][0].set_title('Heat distribution map')
    axes[0][1].set_title('Formation X (hottest: %d)' % FORM_X_upper_heat_boundary)
    axes[1][0].set_title('Formation + (hottest: %d)' % FORM_PLUS_upper_heat_boundary)
    axes[1][1].set_title('Formation MLG (hottest: %d)' % FORM_DIAMOND_upper_heat_boundary)
    axes[0][0].scatter(plot_data_x, plot_data_y, c=plot_data_0_c, marker='s')
    axes[0][1].scatter(plot_data_x, plot_data_y, c=plot_data_1_c, marker='s')
    axes[1][0].scatter(plot_data_x, plot_data_y, c=plot_data_2_c, marker='s')
    axes[1][1].scatter(plot_data_x, plot_data_y, c=plot_data_3_c, marker='s')

    for x in axes:
        for y in x:
            # Mark the spawn points as stars in all 4 scatter plots
            y.scatter([i[0] + 0.05 for i in SPAWN_LOCATIONS],
                      [(21 - i[1]) - 0.05 for i in SPAWN_LOCATIONS],
                      c=[[0, 0, 0, 1]] * 15,  # black, 15 spawn points
                      s=8,
                      marker='*')

            # Mark the gradient scale used to see what colour represents how much heat
            y.scatter(grad_scale_x_points, [0.2] * len(grad_scale_x_points), c=grad_scale, s=1, marker='s')
            # Needs setting every time
            y.set_ylim([0, 22])


plot_data_x = []
plot_data_y = []
plot_data_0_c = []
plot_data_1_c = []
plot_data_2_c = []
plot_data_3_c = []

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(950/96, 800/96))
grad_scale_ticks = 500
grad_scale = [gradient(i / grad_scale_ticks) for i in range(0, grad_scale_ticks)]
grad_scale_x_points = [i * (21 / grad_scale_ticks) for i in range(0, grad_scale_ticks)]
main_tick()


def slider_update(val):
    global heat_distribution_intensity
    heat_distribution_intensity = val
    axes[0][0].clear()
    axes[0][1].clear()
    axes[1][0].clear()
    axes[1][1].clear()
    main_tick()


distribution_slider = Slider(plt.axes([0.23, 0.95, 0.52, 0.02]), 'heat distribution intensity', 0.1, 0.9, valinit=0.5)
distribution_slider.on_changed(slider_update)

plt.show()
