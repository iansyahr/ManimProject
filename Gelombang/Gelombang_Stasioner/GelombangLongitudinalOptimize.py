from manim import *

class GelombangLongitudinalOptimize(Scene):
  def construct(self):
    tracker = ValueTracker(0)
    d = VGroup()
    for i in np.arange(-5,5,0.1):
      T = 0.5
      A = 0.15
      varup = 0.5
      garis = Line(start = ORIGIN, end = UP*varup,color=BLUE)
      #garis.set_x(i + A*np.sin(2*PI*(tracker.get_value()-i)*T))
      garis.add_updater(lambda z, i=i: z.set_x(i + A*np.sin(2*PI*(tracker.get_value()-i)*T)))
      d.add(garis)
    self.add(d)
    self.play(tracker.animate(run_time=2).set_value(2))