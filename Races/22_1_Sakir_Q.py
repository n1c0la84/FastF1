import fastf1.plotting
import myfastf1plots
import os

cache_path = 'cache'
if not os.path.exists(cache_path):
    os.mkdir('cache')

fastf1.Cache.enable_cache(cache_path)  # optional but recommended
fastf1.plotting.setup_mpl()

session = fastf1.get_session(2022, 'Sakir', 'Q')
session.load()

myplots = myfastf1plots.MyFastF1Plots()
myplots.speed_plot(plot_title='LEC vs VER', session=session, driver1='LEC', driver1_color='red', driver2='VER',
                   driver2_color='blue')
myplots.telemetry_plot(plot_title='LEC vs VER', session=session, driver1='LEC', driver1_color='red',
                       # driver2='VER', driver2_color='blue'
                       )

myplots.show_plots()
