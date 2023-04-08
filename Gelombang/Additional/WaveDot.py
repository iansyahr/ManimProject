from manim import *
config.background_color = "#0d0c1a"
class WaveDot(Scene):
  def construct(self):
    bruh = VGroup()
    druh = VGroup()
    for i in range(-4,5):
      time = ValueTracker(5)
      w = 0.1
      func = lambda x, i=i: np.sin((2*PI*(w*time.get_value() + (1+(0.1*i)))-x))+i 
      #np.sin((2*PI*(w*time.get_value() + (1+(0.1*i)))-x))+i))
      hai = FunctionGraph(lambda x, i=i : np.sin(time.get_value()-x)+i)
      hai.add_updater(lambda z,i=i: z.become(FunctionGraph(lambda x, i=i : np.sin((2*PI*(w*time.get_value() + (1+(0.1*i)))-x))+i).set_opacity(0)))
      bruh.add(hai)
      for j in np.arange(-7,7,0.25):
        titik = Dot(radius = 0.05)
        titik.add_updater(lambda y, j=j, i=i : y.become(Dot(radius = 0.05).set_color(BLUE).shift([j,func(j,i),0])))
        druh.add(titik)

    self.add(bruh,druh)
    self.play(time.animate(run_time = 5,rate_func = linear).set_value(10))