import os
import fastf1.plotting
import myfastf1_plots

cache_path = 'cache'
if not os.path.exists(cache_path):
    os.mkdir('cache')

fastf1.Cache.enable_cache(cache_path)  # optional but recommended

fastf1.plotting.setup_mpl()

session = fastf1.get_session(2022, 'Sakir', 'Q')
session.load()

myfastf1_plots.speed_over_lap_plot(session,
                                   driver1='LEC',
                                   driver1_color='red',
                                   driver2='VER',
                                   driver2_color='blue',
                                   plot_title='LEC vs VER')
