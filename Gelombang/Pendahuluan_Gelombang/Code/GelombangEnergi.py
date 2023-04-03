from manim import *

config.background_color = "#0d0c1a"
class GelombangEnergi(Scene):
  def construct(self):
    bruh  = ImageMobject("/content/ManimProject/Gelombang/Pendahuluan_Gelombang/bebek.png").scale(0.5)
    f=0.85
    A=1.0
    q=4.2
    s=2.1
    h=ValueTracker(15.5)

    def fun(x):
      return (A*np.exp(-(((f*x+s)-q)+h.get_value())**2)+A*np.exp(-(((f*x-s)-q)+h.get_value())**2))-(-A*np.exp(-(((f*x-s)+q)+h.get_value())**2)-A*np.exp(-(((f*x+s)+q)+h.get_value())**2))

    def d_fun(x):
      j = 0.0001
      return (fun(x+j)-fun(x))/j
    
    hai = NumberPlane().set_stroke(opacity=0)
    laut = Rectangle(height = 5, width = 16,color = BLUE, fill_opacity = 0.5).shift(DOWN*2.5).set_stroke(opacity = 0)
    function = lambda x : (A*np.exp(-(((f*x+s)-q)+h.get_value())**2)+A*np.exp(-(((f*x-s)-q)+h.get_value())**2))-(-A*np.exp(-(((f*x-s)+q)+h.get_value())**2)-A*np.exp(-(((f*x+s)+q)+h.get_value())**2))
    insane = always_redraw(lambda :hai.plot(fun))
    area_bukit = always_redraw(lambda :hai.get_area(insane,color = BLUE).set_fill(opacity = 0.5).set_stroke(opacity = 0))
    #bruh.add_updater(lambda z: z)
    bruh.add_updater(lambda z: z.become(ImageMobject("/content/ManimProject/Gelombang/Pendahuluan_Gelombang/bebek.png").scale(0.5).rotate(d_fun(0)*30*DEGREES).set_y(fun(0)+0.75)))
    #Line1.add_updater(lambda z: z.set_y(0 + A*np.sin(2*PI*(tracker.get_value()-0)*T)))
    self.add(hai,insane,bruh,area_bukit,laut)
    self.play(h.animate(run_time = 5, rate_func = linear).set_value(-15.5))
