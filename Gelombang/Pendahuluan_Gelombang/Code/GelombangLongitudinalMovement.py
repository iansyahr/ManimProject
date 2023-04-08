from manim import *

config.background_color = "#0d0c1a"
class GelombangLongitudinalMovement(MovingCameraScene):
  def construct(self):
    tracker = ValueTracker(0)
    def func_square(x):
      d = 0
      p = -1.56
      f = 0.35
      s = 15 #30
      A = 1
      return -(A/(abs(s)**(s*np.sin(f*x-p)-d*s) + 1)-1)

    d = VGroup()
    for i in np.arange(-5,5,0.125):
      T = 0.5 #0.5
      A = 0.15 #0.15
      garis = Line(start = DOWN*0.5, end = UP*0.5,color=BLUE).set_stroke(width = 5)
      garis.add_updater(lambda z, i=i: z.set_x(i + A*np.sin(2*PI*(tracker.get_value()-i)*T)))
      d.add(garis)
    
    f = VGroup()
    for j in np.arange(-40,50,1):
      garis = Arrow(start = ORIGIN, end = RIGHT,color=YELLOW).scale(1.5).shift(DOWN)
      garis.add_updater(lambda z, j=j: z.set_x(j + tracker.get_value()))
      garis.add_updater(lambda z, j=j: z.set_opacity(func_square(j + tracker.get_value())))
      f.add(garis)

    Tra_Judul = Tex("Gelombang Longitudinal").scale(1.2).shift(UP*3)
    Sub_Judul = Tex(r"adalah gelombang dengan arah getarannya \\ sejajar dengan arah rambat gelombang").next_to(Tra_Judul,DOWN*0.1).scale(0.8)
    Arah_Getar = Tex("Arah Getar").shift(DOWN*3+LEFT*3)
    arrow_getar = DoubleArrow(start = ORIGIN, end = RIGHT, buff = 0).set_color(RED).next_to(Arah_Getar,RIGHT)
    arrow_getar_1 = DoubleArrow(start = LEFT*0.25, end = RIGHT*0.25, buff = 0).set_color(RED).next_to(d,UP)
    
    Arah_Rambat = Tex("Arah Rambat").shift(DOWN*3+RIGHT*2.5)
    arrow_rambat = Arrow(start = ORIGIN, end = RIGHT, buff = 0).next_to(Arah_Rambat,RIGHT).set_color(YELLOW)
    context_group = VGroup(Tra_Judul,Arah_Getar,Arah_Rambat,Sub_Judul,arrow_getar,arrow_getar_1,arrow_rambat)

    d[40].set_color(RED)
    #self.add(NumberPlane())
    #self.play(Create(d),Create(f),Create(context_group))
    self.add(d,f)
    #self.camera.frame.animate.shift(RIGHT*2)
    self.play(AnimationGroup(tracker.animate(run_time=10,rate_func = linear).set_value(20),Write(context_group[0:4]),Create(context_group[4:7]),lag_ratio = 0.13))