from manim import *

config.background_color = "#0d0c1a"
class DefGelombangBerjalan(Scene):
  def construct(self):
    time = ValueTracker(0)
    land = NumberPlane((0,20),(-3,3)).scale(0.5).set_opacity(0)
    function = lambda x: -2*np.sin(((2*PI)/5)*time.get_value()-((2*PI)/8)*x)
    #Arrow
    arrow_samping = Arrow(start = land.c2p(0,0), end = land.c2p(21,0), buff = 0)
    arrow_atas = Arrow(start = land.c2p(0,-3), end = land.c2p(0,3), buff = 0)
    ax = VGroup(arrow_samping,arrow_atas)

    #Legend
    Berjalan_def = Tex("Gelombang Berjalan").shift(UP*3)
    Berjalan_def_sub = Tex("gelombang dengan amplitudo yang tetap").next_to(Berjalan_def,DOWN).scale(0.8)
    legend = VGroup(Berjalan_def,Berjalan_def_sub)

    #LineAmp
    Line1 = DashedLine(start = land.c2p(0,2), end = land.c2p(20,2), buff = 0)
    Line2 = DashedLine(start = land.c2p(0,-2), end = land.c2p(20,-2), buff = 0)
    Amp_Batas = VGroup(Line1,Line2)

    #AmpKet
    A_plus = Tex("A").next_to(Line1,RIGHT)
    A_minus = Tex("-A").next_to(Line2,RIGHT)
    A_ket = VGroup(A_plus,A_minus)
    #sin = always_redraw(lambda: land.plot(function).set_color(color=[PINK,YELLOW,PINK]))
    sin = always_redraw(lambda: land.plot(function).set_color(RED))
    #self.add(NumberPlane())
    self.add(land,sin,ax,Amp_Batas,legend,A_ket)
    self.play(time.animate(run_time=7,rate_func=linear).set_value(20))