import os
import fastf1.plotting
import myfastf1plots

cache_path = 'cache'
if not os.path.exists(cache_path):
    os.mkdir('cache')

fastf1.Cache.enable_cache(cache_path)  # optional but recommended
fastf1.plotting.setup_mpl()

race = fastf1.get_session(2022, 'Sakir', 'R')
race.load()

myplots = myfastf1plots.MyFastF1Plots()

myplots.laptime_over_race_plot(race, driver1='LEC', driver1_color='red', driver2='VER', driver2_color='blue', plot_title='LEC vs VER')

myplots.show_plots()
