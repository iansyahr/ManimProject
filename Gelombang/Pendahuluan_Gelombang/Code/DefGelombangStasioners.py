from manim import *

config.background_color = "#0d0c1a"
class DefGelombangStasioners(Scene):
  def construct(self):
    time = ValueTracker(0)
    land = NumberPlane((0,20),(-3,3)).scale(0.5).set_opacity(0)
    function = lambda x: 2*np.sin(((2*PI)/8)*x)*np.cos(((2*PI)/5)*time.get_value())
    sin = always_redraw(lambda: land.plot(function, color=RED))
    #Arrow
    arrow_samping = Arrow(start = land.c2p(0,0), end = land.c2p(21,0), buff = 0)
    arrow_atas = Arrow(start = land.c2p(0,-3), end = land.c2p(0,3), buff = 0)

    #Legend
    Berjalan_def = Tex("Gelombang Stasioner").shift(UP*3)
    Berjalan_def_sub = Tex("gelombang dengan amplitudo yang berubah").next_to(Berjalan_def,DOWN).scale(0.8)
    legend = VGroup(Berjalan_def,Berjalan_def_sub)

    #LineAmp
    Line1 = DashedLine(start = land.c2p(0,2), end = land.c2p(20,2), buff = 0).set_color_by_gradient(BLUE, YELLOW)
    Line2 = DashedLine(start = land.c2p(0,-2), end = land.c2p(20,-2), buff = 0).set_color_by_gradient(YELLOW, GREEN)
    Line1.add_updater(lambda z : z.set_y(1*np.sin(((2*PI)/8)*2)*np.cos(((2*PI)/5)*time.get_value())))
    Line2.add_updater(lambda z : z.set_y(1*np.sin(((2*PI)/8)*6)*np.cos(((2*PI)/5)*time.get_value())))
    Amp_Batas = VGroup(Line1,Line2)

    #Decimal
    decimal = DecimalNumber(show_ellipsis=False,num_decimal_places=1,include_sign=True)
    decimal.add_updater(lambda d: d.next_to(Line1, RIGHT))
    decimal.add_updater(lambda d: d.set_value(Line1.get_center()[1]))
    decimal.add_updater(lambda d: d[0][0].set_color_by_gradient(BLUE, YELLOW))
    decimal.add_updater(lambda d: d[1][0].set_opacity(0))
    decimal.add_updater(lambda d: d[2][0].set_opacity(0))
    decimal.add_updater(lambda d: d[3][0].set_opacity(0))

    decimal_1 = DecimalNumber(show_ellipsis=False,num_decimal_places=1,include_sign=True)
    decimal_1.add_updater(lambda d: d.next_to(Line2, RIGHT))
    decimal_1.add_updater(lambda d: d.set_value(Line2.get_center()[1]))
    decimal_1.add_updater(lambda d: d[0][0].set_color_by_gradient(YELLOW, GREEN))
    decimal_1.add_updater(lambda d: d[1][0].set_opacity(0))
    decimal_1.add_updater(lambda d: d[2][0].set_opacity(0))
    decimal_1.add_updater(lambda d: d[3][0].set_opacity(0))

    #AmpKet
    A_plus = Tex("A").next_to(Line1,RIGHT*2.5).set_color(color = [BLUE, YELLOW])
    A_plus.add_updater(lambda d: d.next_to(Line1, RIGHT*2.5))
    A_minus = Tex("A").next_to(Line2,RIGHT*2.5).set_color(color = [YELLOW, GREEN])
    A_minus.add_updater(lambda d: d.next_to(Line2, RIGHT*2.5))
    A_ket = VGroup(A_plus,A_minus)


    ax = VGroup(arrow_samping,arrow_atas,Amp_Batas,decimal,decimal_1,legend,A_ket)
    #self.add(NumberPlane())
    self.add(land,sin,ax)
    self.play(time.animate(run_time=7,rate_func=linear).set_value(20))