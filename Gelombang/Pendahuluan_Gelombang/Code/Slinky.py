from manim import *

class Slinky(MovingCameraScene):
    def construct(self):
      T = 1.7
      v = ValueTracker(0)#2.29
      c = 7.6
      a = 0.15
      k = 0.15
      b = 6
      def func(t):
        return np.array((a*t-k*np.sin(c*t+b*np.sin((t-3*v.get_value())/T)),0.25*np.cos(c*t+b*np.sin((t-3*v.get_value())/T)), 0))

      graph = always_redraw(lambda : ParametricFunction(func, t_range = np.array([0, 20]), fill_opacity=0).set_color([RED,BLUE,GREEN]))
      #self.add(NumberPlane())
      self.add(graph)
      self.camera.frame.scale(0.5).shift(RIGHT*1.5)
      self.play(v.animate(run_time = 3,rate_func = linear).set_value(6))
