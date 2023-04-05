from manim import *
config.background_color = "#0d0c1a"
class GelombangTransversalMovement(Scene):
  def construct(self):
    tracker = ValueTracker(0)
    
    def func_square(x):
      d = 0
      p = -1.56
      f = 0.4
      s = 15 #30
      A = 1
      return -(A/(abs(s)**(s*np.sin(f*x-p)-d*s) + 1)-1)

    hai = NumberPlane(x_range=(0, 8, 1),y_range=(-1, 1, 1)).set_stroke(opacity = 0).scale(1).shift(DOWN*0.5)
    sine_function = lambda x: (1*np.sin(1.6*tracker.get_value()-(0.5)*PI*x))
    correct = always_redraw(lambda: hai.plot(sine_function,color=BLUE, x_range=[0,8]))
    #sine_plot = always_redraw(lambda : ax.plot(sine_function, color=RED))
    arrowup = Arrow(start = hai.c2p(0,-1), end = hai.c2p(0,1.5), buff = 0)
    arrowdown = Arrow(start = hai.c2p(0,0), end = hai.c2p(8.5,0), buff = 0)
    dot_travel = Dot(radius = 0.2)
    
    d = VGroup()
    for i in np.arange(-40,50,1):
      garis = Arrow(start = ORIGIN, end = RIGHT,color=YELLOW).scale(1.5).shift(DOWN*2)
      garis.add_updater(lambda z, i=i: z.set_x(i + tracker.get_value()))
      garis.add_updater(lambda z, i=i: z.set_opacity(func_square(i + tracker.get_value())))
      d.add(garis)
    
    g = VGroup()
    for j in np.arange(0,8.25,0.25):
      l1=Arrow(hai.c2p(j,0),hai.c2p(j,1*np.sin(1.6*tracker.get_value()-(0.5)*PI*j)),buff = 0,max_tip_length_to_length_ratio=0.15).set_color(RED)
      l1.add_updater(lambda z, j=j: z.become(Arrow(hai.c2p(j,0),hai.c2p(j,1*np.sin(1.6*tracker.get_value()-(0.5)*PI*j)),buff = 0,max_tip_length_to_length_ratio=0.15).set_color(RED)))
      g.add(l1)

    Tra_Judul = Tex("Gelombang Transversal").scale(1.2).shift(UP*3)
    Sub_Judul = Tex(r"adalah gelombang dengan arah getarannya \\ tegak lurus dengan arah rambat gelombang").next_to(Tra_Judul,DOWN*0.1).scale(0.8)
    Arah_Getar = Tex("Arah Getar").shift(DOWN*3+LEFT*3)
    arrow_getar = DoubleArrow(start = ORIGIN, end = UP, buff = 0).set_color(RED).next_to(Arah_Getar,RIGHT)
    
    Arah_Rambat = Tex("Arah Rambat").shift(DOWN*3+RIGHT*2.5)
    arrow_rambat = Arrow(start = ORIGIN, end = RIGHT, buff = 0).next_to(Arah_Rambat,RIGHT).set_color(YELLOW)
    context_group = VGroup(Tra_Judul,Arah_Getar,arrow_getar,Arah_Rambat,arrow_rambat)

    #self.add(NumberPlane())
    self.add(d,hai,correct,arrowup,arrowdown,g)
    #self.play(tracker.animate(run_time=5*2, rate_func = linear).set_value(10*2))
    self.play(AnimationGroup(tracker.animate(run_time=5*2, rate_func = linear).set_value(10*2),Write(context_group),Write(Sub_Judul),lag_ratio = 0.13))
    self.wait()